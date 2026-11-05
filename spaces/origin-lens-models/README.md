---
title: Origin Lens Models
emoji: 🔍
colorFrom: yellow
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
short_description: Open-model AI detection API for Origin Lens
---

# Origin Lens open-model API

A planetAI LLP Space that runs open-source AI-content detectors for [Origin Lens](https://world-of-ai.co.in/origin-lens.html), so visitors get a model-based check without an API key of their own.

Content is scored in memory and discarded. Nothing is stored or logged.

## Endpoints

- `POST /api/text` with `{"text": "...", "sentences": ["...", "..."]}` returns `{"ai_probability": 0.0–1.0, "sentences": [p or null, ...], "model": "..."}`. Sentences under 8 words get `null`.
- `POST /api/image` with `{"image": "<base64 JPEG or PNG>"}` returns `{"ai_probability": 0.0–1.0, "model": "..."}`.
- `GET /health`

## Settings (Space variables)

| Variable | Default | Purpose |
|---|---|---|
| `TEXT_MODEL` | `fakespotailabs/roberta-base-ai-text-detection-v1` | Any Hugging Face text-classification detector |
| `IMAGE_MODEL` | `dima806/ai_vs_real_image_detection` | Any Hugging Face image-classification detector |
| `ALLOWED_ORIGINS` | world-of-ai.co.in and pawan-maheshwari.github.io | Sites allowed to call the API |

Labels are mapped automatically (AI, Fake, Generated → AI; Human, Real → human), so most detectors work without code changes. Changing a variable restarts the Space.

## Limits

Open detectors are trained on older generators and can miss content from newer models or flag polished human work. Origin Lens uses this as one signal among several, never as the verdict.

This folder is deployed from the [world-of-ai](https://github.com/pawan-maheshwari/world-of-ai) repository by a GitHub Action. Edit it there, not here.
