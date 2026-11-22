# Henry Okechi — Portfolio (Obsidian & Ivory Editorial Redesign)

An editorial, minimalist personal portfolio built around the **Obsidian & Ivory** design system (`Instrument Serif` + `Manrope` + `IBM Plex Mono`).

## Preview Locally
```bash
python -m http.server 4173
```
Then visit `http://localhost:4173`.

## Regenerating Static Pages
`projects.json` is the single source of truth for all 12 project entries and case studies. After editing `projects.json` or `build.py`, run:
```bash
python build.py
```
