# NatSci-Writing-skills v1.2.7.0

Defensive-writing control and anti-AI-prose release, integrating the open-source anti-defensive-writing skill.

## New

- **Defensive writing and argument selection** (EN/ZH reference): the press-release principle (a paper is a press conference, not a project summary, lab log or self-audit); argument selection before wording; the three-question test (what do we win, by how much, on what ground); battlefield choice; space follows argument, not effort; one duty per experiment; a ban on chronology; permission to restructure the story; a per-section defensive audit; a seven-pass revision protocol; a reader test.
- **The boundary that prevents overclaiming**: rhetorical hedging versus epistemic calibration, decided by a deletion test; a hedge-diagnosis table; and six absolute prohibitions (no claim without evidence; no deletion of a reading-changing limitation; no null rewritten as a positive; no generalisation past the system; no hidden comparator; integrity rules override style).
- **Structure-level AI tells** (writing-diagnostics section 4A, both languages): uniform sentence length, the template paragraph (topic, three supports, recap), glue sentences — with a before/after pair and a metric table.
- **Measurable gates**: sentence-length CV, hedge, recap, limitation, triad, nominalisation and em-dash densities, reported by `--metrics` and enforced by `--gate`, with `--genre paper|perspective|report` so proposal modality is not punished as hedging.
- **SKILL section 17 / 十七** and a defensive-argument bullet in the final check.

## Changed

- `tools/check_prose_style.py`: defensive and AI rule families (including comma negation and the proposal/objection patterns), an advisory tier for marks that are sometimes legitimate, `--metrics`, `--gate`, `--genre`, a prose-only filter for metric calculation, and UTF-8-safe JSON output on Windows consoles.
- `tools/validate_package.py`: `display_path()` so validation works when a skill is installed on another drive or volume.
- Attribution: `NOTICE.md` and `LICENSES/MIT-anti-defensive-writing.txt` for the MIT-licensed upstream skill.

## Fixed

- `skills/natsci-writing-zh/VERSION` still read 1.2.6.6.
- `CITATION.cff` still carried placeholder repository URLs.

## Verification

- `python tools/validate_package.py --strict`: PASS. Manifest 141 files, version 1.2.7.0.
- `python tools/check_prose_style.py README.md README.zh-CN.md --fail-on error`: 0 hits.
- Gate regression: AI-flavoured synthetic paragraphs fail in both languages; rewritten versions pass; `16. SynBio-New/Nature_Perspective/EN.md` passes with CV 0.516, hedge 3.49/1k, triads 0, nominalisation 10.5%.
