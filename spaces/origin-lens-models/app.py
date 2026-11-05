"""Origin Lens open-model API, a planetAI LLP Hugging Face Space.

Runs open-source AI-content detectors on CPU and returns AI-likelihood
scores to the Origin Lens page on world-of-ai.co.in. Nothing is stored or
logged: requests are scored in memory and discarded.

Models are set with Space variables, so they can be swapped without code:
  TEXT_MODEL       a text-classification model (default below)
  IMAGE_MODEL      an image-classification model (default below)
  ALLOWED_ORIGINS  comma-separated sites allowed to call the API
"""
import base64
import io
import os
import re
import threading

import torch
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from PIL import Image
from pydantic import BaseModel
from transformers import pipeline

TEXT_MODEL = os.getenv("TEXT_MODEL", "fakespotailabs/roberta-base-ai-text-detection-v1")
IMAGE_MODEL = os.getenv("IMAGE_MODEL", "dima806/ai_vs_real_image_detection")
ALLOWED_ORIGINS = [o.strip() for o in os.getenv(
    "ALLOWED_ORIGINS",
    "https://world-of-ai.co.in,https://www.world-of-ai.co.in,https://pawan-maheshwari.github.io",
).split(",") if o.strip()]

MAX_TEXT_CHARS = 60_000
MAX_SENTENCES = 120
MIN_SENTENCE_WORDS = 8
CHUNK_WORDS = 300
MAX_CHUNKS = 8
MAX_IMAGE_B64 = 8_000_000

torch.set_num_threads(max(1, os.cpu_count() or 1))
text_clf = pipeline("text-classification", model=TEXT_MODEL, top_k=None, truncation=True, max_length=512)
image_clf = pipeline("image-classification", model=IMAGE_MODEL, top_k=None)
lock = threading.Lock()  # one inference at a time keeps memory flat on the free CPU tier

AI_WORDS = {"ai", "fake", "artificial", "generated", "machine", "synthetic", "gpt", "llm", "bot"}
HUMAN_WORDS = {"human", "real", "authentic", "natural", "original"}


def ai_probability(scores):
    """Map a classifier's labels to one AI probability, whatever the labels are called."""
    ai = human = None
    for s in scores:
        label = s["label"].lower().replace("_", " ").strip()
        words = set(re.split(r"[^a-z0-9]+", label))
        if words & AI_WORDS or label in ("label 1", "1"):
            ai = (ai or 0.0) + float(s["score"])
        elif words & HUMAN_WORDS or label in ("label 0", "0"):
            human = (human or 0.0) + float(s["score"])
    if ai is not None:
        return ai if human is None else ai / max(ai + human, 1e-9)
    if human is not None:
        return 1.0 - human
    raise ValueError("Unrecognised labels: " + ", ".join(s["label"] for s in scores))


def as_lists(out):
    """A pipeline returns a list of dicts for one input and a list of lists for many."""
    return [out] if out and isinstance(out[0], dict) else out


def chunks(text):
    words = text.split()
    parts = [" ".join(words[i:i + CHUNK_WORDS]) for i in range(0, len(words), CHUNK_WORDS)]
    if len(parts) > MAX_CHUNKS:  # spread the sample across the whole document
        step = len(parts) / MAX_CHUNKS
        parts = [parts[int(i * step)] for i in range(MAX_CHUNKS)]
    return parts


class TextIn(BaseModel):
    text: str
    sentences: list[str] = []


class ImageIn(BaseModel):
    image: str  # base64 JPEG or PNG, with or without a data: prefix


app = FastAPI(title="Origin Lens open-model API", docs_url="/docs", redoc_url=None)
app.add_middleware(CORSMiddleware, allow_origins=ALLOWED_ORIGINS, allow_methods=["POST", "GET"],
                   allow_headers=["content-type"], max_age=86400)


@app.get("/", response_class=HTMLResponse)
def home():
    return f"""<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Origin Lens models</title>
<body style="margin:0;background:#05070F;color:#F2EFE6;font:16px/1.6 system-ui,sans-serif;padding:40px 20px">
<main style="max-width:640px;margin:0 auto">
<p style="font:12px monospace;letter-spacing:.2em;color:#E8B85C">PLANETAI LLP · WORLD OF AI</p>
<h1 style="font-family:Georgia,serif;font-weight:600">Origin Lens open-model API</h1>
<p>This Space scores content for <a style="color:#E8B85C" href="https://world-of-ai.co.in/origin-lens.html">Origin Lens</a>.
Content is scored in memory and discarded; nothing is stored or logged.</p>
<ul><li>Text model: <code>{TEXT_MODEL}</code></li><li>Image model: <code>{IMAGE_MODEL}</code></li></ul>
<p>Endpoints: <code>POST /api/text</code>, <code>POST /api/image</code>, <code>GET /health</code>. Schema at <a style="color:#E8B85C" href="docs">/docs</a>.</p>
</main></body>"""


@app.get("/health")
def health():
    return {"ok": True, "text_model": TEXT_MODEL, "image_model": IMAGE_MODEL}


@app.post("/api/text")
def score_text(body: TextIn):
    text = re.sub(r"\s+", " ", body.text or "").strip()[:MAX_TEXT_CHARS]
    if len(text.split()) < 5:
        raise HTTPException(422, "Send at least a sentence of text.")
    parts = chunks(text)
    sents = body.sentences[:MAX_SENTENCES]
    keep = [i for i, s in enumerate(sents) if len(s.split()) >= MIN_SENTENCE_WORDS]
    with lock:
        doc = as_lists(text_clf(parts, batch_size=4))
        per = as_lists(text_clf([sents[i] for i in keep], batch_size=16)) if keep else []
    weights = [len(p.split()) for p in parts]
    p_doc = sum(ai_probability(o) * w for o, w in zip(doc, weights)) / sum(weights)
    sentence_scores = [None] * len(sents)
    for i, o in zip(keep, per):
        sentence_scores[i] = round(ai_probability(o), 4)
    return {"ai_probability": round(p_doc, 4), "chunks": len(parts), "sentences": sentence_scores, "model": TEXT_MODEL}


@app.post("/api/image")
def score_image(body: ImageIn):
    data = body.image.split(",", 1)[-1]
    if len(data) > MAX_IMAGE_B64:
        raise HTTPException(413, "Image too large; send at most about 6 MB.")
    try:
        img = Image.open(io.BytesIO(base64.b64decode(data))).convert("RGB")
    except Exception:
        raise HTTPException(422, "That is not a readable JPEG or PNG image.")
    with lock:
        out = image_clf(img)
    return {"ai_probability": round(ai_probability(out), 4), "model": IMAGE_MODEL}
