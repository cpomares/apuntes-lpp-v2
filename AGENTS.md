# AGENTS.md

## Scope

This repository contains teaching notes built with MkDocs Material.
Work is split between:

- `docs/` for published content
- `docs/teoria/`, `docs/practicas/`, `docs/seminarios/` for the Spanish source
- `docs/en/` for the English version
- `mkdocs.yml` for navigation and multilingual configuration

## Bilingual Structure

The Spanish tree is the source structure and must be preserved.

- Do not move, rename, or delete existing Spanish files or folders.
- Do not refactor the Spanish content tree.
- English content lives only under `docs/en/`.
- Keep the English structure parallel to the Spanish one:
  - `docs/en/theory/`
  - `docs/en/labs/`
  - `docs/en/seminars/`

### Topic Pattern

Theory topics follow this pattern:

- Spanish: `docs/teoria/temaXX-.../temaXX-....md`
- English: `docs/en/theory/topicXX-.../topicXX-....md`

Seminars follow this pattern:

- Spanish: `docs/seminarios/seminarioX-.../seminarioX-....md`
- English: `docs/en/seminars/seminarXX-.../seminarXX-....md`

Labs follow this pattern:

- Spanish: `docs/practicas/practicaXX/practicaXX.md`
- English: `docs/en/labs/labXX-.../labXX-....md`

## Images

- Spanish theory and seminars use `imagenes/` folders.
- English theory and seminars should keep relative image paths working.
- If an English page uses the same images as the Spanish original, copy the
  needed files into the matching English `imagenes/` folder.
- Do not reorganize shared image assets unless explicitly requested.

## Translation Rules

- Translate one unit at a time unless asked otherwise.
- Do not translate unrelated topics.
- Preserve Markdown structure, headings, admonitions, code fences, links, and
  image references.
- Keep code examples unchanged unless the user explicitly asks for translated
  comments or strings.
- Prefer natural technical English, but stay close to the teaching intent of
  the Spanish source.

## MkDocs Rules

- Keep `mkdocs.yml` changes minimal and intentional.
- When English pages are added, update the English `nav` in `mkdocs.yml` so the
  language switcher exposes them.
- This repo uses directory URLs for publication.
- The Spanish and English homepages should both exist in navigation.

## Local Environment

Use the project virtual environment at:

- `/Users/cristina/Documents/lpp-env`

Preferred commands:

```bash
source /Users/cristina/Documents/lpp-env/bin/activate
python -m mkdocs build
python -m mkdocs serve
python -m mkdocs gh-deploy
```

## Validation

Before publishing, prefer this sequence:

1. Build with `python -m mkdocs build`
2. Check the local English route under `/en/`
3. If requested, publish with `python -m mkdocs gh-deploy`

Warnings about old Spanish pages not included in `nav` or legacy broken anchors
may already exist in the project. Do not fix them unless requested.

## Git Guidance

- Make focused commits.
- Do not include unrelated edits.
- If changing both content and navigation, keep them in the same commit only if
  they belong to the same user task.

