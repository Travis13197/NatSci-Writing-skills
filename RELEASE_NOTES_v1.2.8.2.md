# NatSci-Writing-skills v1.2.8.2

Results-as-discovery release, derived from a manuscript revision where the Results read as a pipeline and the headings had been truncated to satisfy a character limit.

## New

- **Results architecture** (EN/ZH): six-move Results narrative (existence, mechanism, diversity, coverage, origin, boundary), a five-function paragraph contract (question, design, observation, interpretation, boundary), and a rule that Results must not open with software or an analysis inventory.
- **Results heading language** (EN/ZH, 1.2.8.1): object/process/finding rule, parallelism, no metaphor, no undefined local shorthand, no verb-only slogan, no first-person opener, evidence matching and an audit procedure.
- SKILL sections 19 and 20 (十九 and 二十) state the operative rules with bad/good pairs.

## Changed

- The Results heading limit is now 60 characters and twelve words (was 40 and eight): completeness takes priority over brevity.
- Heading language is a named audit item, separate from the prose gate.

## Verification

- `python tools/validate_package.py --strict`: PASS; manifest current.
- `python tools/check_prose_style.py README.md README.zh-CN.md --fail-on error`: 0 hits.
- Installed copies, plugin library and delivery copy synced to 1.2.8.2.
