#!/usr/bin/env python3
"""Assemble a manuscript into a journal template.

Input is a markdown file whose level-2 headings name manuscript sections
("## Abstract", "## Results", "## Methods", "## References", ...) or a JSON file
with the same structure. Output is a .docx built on the journal template: the
spec's styles, page setup, line numbering and section order are applied, in-text
citations become superscripts, and a build report records what was found, what
was missing and what the word counts are.

Default journal: nature.
"""
import argparse
import json
import os
import re
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import journal_spec as js  # noqa: E402

STYLE = {
    "title": "NSC Title",
    "authors": "NSC Authors",
    "affiliations": "NSC Affiliations",
    "heading1": "NSC Heading 1",
    "heading2": "NSC Heading 2",
    "body": "NSC Body",
    "abstract": "NSC Abstract",
    "caption": "NSC Caption",
    "reference": "NSC Reference",
}

ALIASES = {
    "abstract": "abstract", "summary": "abstract",
    "introduction": "main", "background": "main", "results": "main", "discussion": "main",
    "conclusion": "main", "conclusions": "main", "main text": "main", "main": "main",
    "methods": "methods", "materials and methods": "methods", "online methods": "methods",
    "references": "references", "references and notes": "references", "bibliography": "references",
    "acknowledgements": "acknowledgements", "acknowledgments": "acknowledgements",
    "author contributions": "author_contributions", "contributions": "author_contributions",
    "competing interests": "competing_interests", "conflict of interest": "competing_interests",
    "declaration of interests": "competing_interests",
    "data availability": "data_availability", "data and materials availability": "data_availability",
    "code availability": "code_availability",
    "figure legends": "figure_legends", "figure captions": "figure_legends", "legends": "figure_legends",
    "funding": "funding", "supplementary materials": "supplementary",
    "tables": "tables", "extended data": "extended_data",
}

CITE = re.compile(r"\[(\d[\d,\s\u2013-]*)\]")


def parse_markdown(path):
    """Split a markdown manuscript into front matter, title, ordered sections and bodies.

    Repeated level-2 headings that map to the same spec section (Introduction,
    Results and Discussion all belong to the main text) are folded into that
    section and kept as level-3 subheadings, so nothing is emitted twice.
    """
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    meta = {}
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                for raw in lines[1:i]:
                    if ":" in raw:
                        k, v = raw.split(":", 1)
                        meta[k.strip().lower()] = v.strip()
                lines = lines[i + 1:]
                break
    title, sections, order, current = None, {}, [], None
    for raw in lines:
        line = raw.rstrip()
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
            continue
        if line.startswith("## "):
            name = line[3:].strip()
            key = ALIASES.get(name.lower(), name.lower().replace(" ", "_"))
            if key in sections:
                sections[key].append("### " + name)
                sections[key].append("")
                current = key
                continue
            current = key
            sections.setdefault(key, [])
            order.append(key)
            continue
        if current is not None:
            sections[current].append(line)
    return title, sections, order, meta


def parse_json(path):
    """Read a JSON manuscript: {title, sections: {name: text or [lines]}}."""
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    title = data.get("title")
    sections, order = {}, []
    for name, body in (data.get("sections") or {}).items():
        key = ALIASES.get(name.lower(), name.lower().replace(" ", "_"))
        sections[key] = body if isinstance(body, list) else str(body).splitlines()
        order.append(key)
    return title, sections, order


def clean(lines):
    """Collapse blank-line runs and strip trailing whitespace."""
    out, blank = [], False
    for line in lines:
        if not line.strip():
            if not blank:
                out.append("")
            blank = True
        else:
            out.append(line.rstrip())
            blank = False
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return out


def ensure_style(doc, name, spec_typo):
    """Return a style by name, creating it with direct formatting when absent."""
    try:
        return doc.styles[name]
    except KeyError:
        from docx.enum.style import WD_STYLE_TYPE
        style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        style.font.name = spec_typo["font"]
        style.font.size = Pt(spec_typo.get("size_pt", 12))
        style.font.bold = bool(spec_typo.get("bold"))
        style.paragraph_format.line_spacing = float(spec_typo.get("line_spacing", 1.0))
        style.paragraph_format.space_before = Pt(spec_typo.get("space_before_pt", 0))
        style.paragraph_format.space_after = Pt(spec_typo.get("space_after_pt", 0))
        return style


def add_paragraph(doc, text, style_name, typo):
    """Add one paragraph with the style and, defensively, direct formatting."""
    para = doc.add_paragraph(style=ensure_style(doc, style_name, typo))
    parts = CITE.split(text)
    for i, part in enumerate(parts):
        if not part:
            continue
        run = para.add_run(part)
        run.font.name = typo["font"]
        run.font.size = Pt(typo.get("size_pt", 12))
        run.font.bold = bool(typo.get("bold"))
        if i % 2 == 1:
            run.font.superscript = True
    return para


def clear_body(doc):
    """Remove every body element except the final section properties."""
    body = doc.element.body
    for child in list(body):
        if child.tag == qn("w:sectPr"):
            continue
        body.remove(child)


def build(md_or_json, journal="nature", template=None, out=None):
    """Assemble the manuscript and return (output path, report dict)."""
    spec = js.load(journal)
    typo = spec["typography"]
    if out is None:
        stem = os.path.splitext(os.path.basename(md_or_json))[0]
        out = os.path.join(os.getcwd(), "%s-%s.docx" % (stem, journal))
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    meta = {}
    if md_or_json.lower().endswith(".json"):
        title, sections, order = parse_json(md_or_json)
    else:
        title, sections, order, meta = parse_markdown(md_or_json)

    if template and os.path.exists(template):
        doc = Document(template)
        clear_body(doc)
        base = template
    else:
        doc = Document()
        base = "generated"
        from make_journal_template import build_docx as gen
        tmp = os.path.join(os.path.dirname(out or "."), "_base.docx")
        gen(spec, tmp, placeholders=False)
        doc = Document(tmp)
        clear_body(doc)

    # title block: title, authors, affiliations (front matter supplies the latter two)
    if title:
        add_paragraph(doc, title, STYLE["title"], typo["title"])
    if meta.get("authors"):
        add_paragraph(doc, meta["authors"], STYLE["authors"], typo["authors"])
    if meta.get("affiliations"):
        add_paragraph(doc, meta["affiliations"], STYLE["affiliations"], typo["affiliations"])
    section_map = {s["id"]: s for s in spec["sections"]}

    report = {"journal": journal, "article_type": spec["article_type"], "base": base,
              "sections_found": [], "sections_missing": [], "word_counts": {},
              "citations": 0, "references": 0, "output": out}

    def emit_body(lines, style="body", heading=None):
        buf = []
        for line in lines:
            if line.startswith("### "):
                if heading:
                    add_paragraph(doc, heading, STYLE["heading1"], typo["heading1"])
                    heading = None
                for sent in clean(buf):
                    if sent:
                        add_paragraph(doc, sent, STYLE[style], typo[style if style in typo else "body"])
                buf = []
                add_paragraph(doc, line[4:].strip(), STYLE["heading2"], typo["heading2"])
                continue
            if line.startswith("- "):
                buf.append(line[2:].strip())
                continue
            buf.append(line)
        if heading:
            add_paragraph(doc, heading, STYLE["heading1"], typo["heading1"])
        for sent in clean(buf):
            if not sent:
                continue
            style_key = "reference" if style == "reference" else ("abstract" if style == "abstract" else "body")
            add_paragraph(doc, sent, STYLE[style_key], typo[style_key])

    for key in order:
        body = sections.get(key, [])
        sec_meta = section_map.get(key)
        text = "\n".join(body)
        report["word_counts"][key] = js.word_count(text)
        report["citations"] += len(CITE.findall(text))
        if sec_meta is None:
            emit_body(body)
            continue
        report["sections_found"].append(key)
        if key in ("authors", "affiliations") and meta.get(key):
            continue
        if key == "title":
            continue
        if sec_meta["kind"] == "references":
            refs = [l for l in clean(body) if l.strip()]
            report["references"] = len(refs)
            emit_body(refs, style="reference", heading=sec_meta.get("heading"))
        elif sec_meta["kind"] == "abstract":
            emit_body(body, style="abstract", heading=sec_meta.get("heading"))
        else:
            emit_body(body, style="body", heading=sec_meta.get("heading"))

    if title:
        report["sections_found"].append("title")
    for key in ("authors", "affiliations"):
        if meta.get(key):
            report["sections_found"].append(key)

    for item in spec["sections"]:
        if item.get("required") and item["id"] not in report["sections_found"]:
            report["sections_missing"].append(item["id"])

    doc.save(out)
    report["output"] = out
    return out, report


def main():
    ap = argparse.ArgumentParser(description="Assemble a manuscript into a journal template")
    ap.add_argument("manuscript", help="markdown or json manuscript")
    ap.add_argument("--journal", default="nature", choices=list(js.JOURNALS))
    ap.add_argument("--template", default=None, help="publisher .docx template (preferred when present)")
    ap.add_argument("--out", default=None, help="output .docx path")
    ap.add_argument("--report", default=None, help="write a JSON build report here")
    args = ap.parse_args()
    out, report = build(args.manuscript, args.journal, args.template, args.out)
    if args.report:
        with open(args.report, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2, ensure_ascii=False)
    print("wrote " + out)
    print("journal=%s base=%s sections=%d missing=%s references=%d citations=%d" % (
        report["journal"], report["base"], len(report["sections_found"]),
        ",".join(report["sections_missing"]) or "none", report["references"], report["citations"]))
    print("word counts: " + json.dumps(report["word_counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
