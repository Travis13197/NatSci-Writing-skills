# Journal templates

This folder holds everything needed to assemble a manuscript into a journal format and to verify the result. Default journal: **Nature**; Science is the second target.

## Layout

~~~text
specs/                 nature-article.json, science-research-article.json   (single source of truth)
generated/             nature-article.docx/.tex, science-research-article.docx/.tex  (built from the specs)
official/              publisher templates you imported (created on first import; not shipped)
~~~

## Regenerate the generated templates

~~~bash
python tools/make_journal_template.py --journal all
~~~

Every time a spec changes, regenerate; the checker compares the produced document against the spec, not against a stale template.

## Import the publisher's own template

~~~bash
python tools/fetch_journal_templates.py --list        # where to download each file
python tools/fetch_journal_templates.py --from-dir ~/Downloads
python tools/fetch_journal_templates.py --check       # sha256 recorded on import, verified afterwards
python tools/build_manuscript.py draft.md --journal nature \
  --template assets/journal-templates/official/nature-template.docx
~~~

## What is shipped and what is not

- Shipped: the specs, the generated .docx/.tex templates, and the source registry. These are our own artefacts and follow the repository licence.
- Not shipped: the publisher's Word and LaTeX templates. They are downloaded by the author in a browser, imported locally, and verified by sha256. Nothing here redistributes publisher files or bypasses their interstitials.

## Confidence

Each spec block is tagged `official`, `secondary` or `default`. Re-verify the values against the current author guidelines before submission and update the spec; the manuscript should not be hand-tweaked to compensate.
