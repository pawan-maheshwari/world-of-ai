# World of AI — Claude working guide

Static site on GitHub Pages → **world-of-ai.co.in** (CNAME). Hub for planetAI LLP's
single-file AI products. No build step: committed files are served as-is.
Owner: Pawan Maheshwari (planetAI LLP).

## Token rules (read first)
- Every product is one self-contained HTML file (inline CSS + JS). Work on one file at a
  time; never read the others "for context".
- Sizes: `harmonia.html` 220 KB, `green-llm.html` 157 KB, `index.html` 140 KB,
  `origin-lens.html` 86 KB, `assay.html` 41 KB, `range-studio.html` 37 KB.
  Use `docs/CODEMAP.md` + `tools/claude/peek.sh` to jump to anchors; read ≤150 lines at once.
- `media/` is binary — never read it.

## Architecture
- `index.html` — hub. Products appear in **four places** (grep the file name to find them):
  top nav (`<a class="prem" …>`), hero/feature cards, footer links, and the JS product
  registry `{id, name, dom, url, status, …}` + search-keyword index `{k:[…]}` used by the
  hub's search/assistant.
- Each product page carries a shared top ribbon (`woa-…` classes: "A World of AI product ·
  planetAI LLP" + links to Home and sibling products). **When adding a product, add its
  link to the ribbon on every product page** (grep `woa-right`; index.html has its own nav).
- Products: `assay.html` (LLM claim validator), `green-llm.html` (GREEN-LLM sustainability
  index), `harmonia.html` (responsible-AI index, Fibonacci gauge + sonification),
  `origin-lens.html` (AI-content detector), `range-studio.html` (premium range planning).
- `spaces/origin-lens-models/` — Hugging Face Docker Space (`app.py`, FastAPI, port 7860)
  serving `POST /api/text` for Origin Lens. Deployed by
  `.github/workflows/deploy-origin-lens-space.yml` on push to that folder.
- Dark theme tokens in index.html: `--void #05070F`, `--deep`, `--panel`, `--raise`,
  `--line`. Reuse them; don't invent new palettes.

## Recipes
- **New product** → `new-product.html` as one self-contained file (copy the ribbon + head
  from `assay.html`, the smallest page), then register it in the 4 places in `index.html`
  and the ribbon on every page.
- **Verify** → `python3 tools/claude/check_html.py *.html`; Space →
  `python3 -m py_compile spaces/origin-lens-models/app.py`.
- After structural changes → `python3 tools/claude/codemap.py`.

Slash commands: `/feature <ask>`, `/fix <symptom>`.
