#!/usr/bin/env python3
"""Generate a journal template (.docx and .tex) from a spec.

The generated template is our own artefact: it encodes the spec's page setup,
typography, section order and line numbering, so a manuscript can be assembled
into a format-correct document even when the publisher's own template is not on
hand. When the publisher's template is present (see fetch_journal_templates.py),
the builder uses it instead and only borrows its styles.
"""
import argparse
import json
import os
import sys

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt, Inches

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import journal_spec as js  # noqa: E402

PAGE_MM = {"A4": (210, 297), "Letter": (215.9, 279.4)}
STYLE_NAMES = {
    "title": "NSC Title",
    "authors": "NSC Authors",
    "affiliations": "NSC Affiliations",
    "heading1": "NSC Heading 1",
    "heading2": "NSC Heading 2",
    "body": "NSC Body",
    "abstract": "NSC Abstract",
    "caption": "NSC Caption",
    "reference": "NSC Reference",
    "table": "NSC Table",
}


def set_line_numbers(section, on=True):
    """Turn continuous line numbering on or off for one section."""
    sect_pr = section._sectPr
    for existing in sect_pr.findall(qn("w:lnNumType")):
        sect_pr.remove(existing)
    if not on:
        return
    node = OxmlElement("w:lnNumType")
    node.set(qn("w:countBy"), "1")
    node.set(qn("w:start"), "1")
    node.set(qn("w:restart"), "continuous")
    sect_pr.append(node)


def add_page_number_footer(section):
    """Put a centred page number in the footer."""
    footer = section.footer
    para = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = para.add_run()
    for tag, text in (("begin", None), (None, " PAGE "), ("end", None)):
        if tag:
            fld = OxmlElement("w:fldChar")
            fld.set(qn("w:fldCharType"), tag)
            run._r.append(fld)
        else:
            instr = OxmlElement("w:instrText")
            instr.set(qn("xml:space"), "preserve")
            instr.text = text
            run._r.append(instr)


def apply_font(style, spec):
    """Apply font, size, weight and spacing from a typography entry."""
    style.font.name = spec["font"]
    style.font.size = Pt(spec.get("size_pt", 12))
    style.font.bold = bool(spec.get("bold"))
    if spec.get("italic") is not None:
        style.font.italic = bool(spec.get("italic"))
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), spec["font"])
    spacing = float(spec.get("line_spacing", 1.0))
    style.paragraph_format.line_spacing = spacing
    style.paragraph_format.space_before = Pt(spec.get("space_before_pt", 0))
    style.paragraph_format.space_after = Pt(spec.get("space_after_pt", 0))
    align = (spec.get("align") or "left").upper()
    style.paragraph_format.alignment = getattr(WD_ALIGN_PARAGRAPH, align, WD_ALIGN_PARAGRAPH.LEFT)


def build_docx(spec, out_path, placeholders=True):
    """Create a .docx template that encodes the spec."""
    doc = Document()
    page = spec["page"]
    w_mm, h_mm = PAGE_MM.get(page.get("size", "A4"), PAGE_MM["A4"])
    sec = doc.sections[0]
    sec.page_width = Mm(w_mm)
    sec.page_height = Mm(h_mm)
    for side in ("top", "bottom", "left", "right"):
        setattr(sec, side + "_margin", Inches(page["margins_in"][side]))
    set_line_numbers(sec, page.get("line_numbers", True))
    if page.get("page_numbers", True):
        add_page_number_footer(sec)

    typo = spec["typography"]
    styles = doc.styles
    for key, name in STYLE_NAMES.items():
        if key not in typo:
            continue
        style = styles.add_style(name, 1)  # WD_STYLE_TYPE.PARAGRAPH
        style.base_style = styles["Normal"]
        apply_font(style, typo[key])

    if placeholders:
        doc.add_paragraph("Manuscript title", style=STYLE_NAMES["title"])
        doc.add_paragraph("Author One, Author Two, Author Three", style=STYLE_NAMES["authors"])
        doc.add_paragraph("Affiliation one; affiliation two", style=STYLE_NAMES["affiliations"])
        for item in spec["sections"]:
            heading = item.get("heading")
            if not heading:
                continue
            doc.add_paragraph(heading, style=STYLE_NAMES["heading1"])
            if item["kind"] == "references":
                doc.add_paragraph("[1] Author, A. B. et al. Title. Journal 1, 1-9 (2020).", style=STYLE_NAMES["reference"])
            else:
                doc.add_paragraph("[fill: %s]" % item["id"], style=STYLE_NAMES["body"])
    doc.save(out_path)
    return out_path


def build_tex(spec, out_path):
    """Create a LaTeX skeleton that mirrors the spec."""
    typo = spec["typography"]["body"]
    head = "% " + spec["display_name"] + " -- generated by NatSci-Writing-skills (" + spec["version"] + ")"
    page = "% Page and type: " + spec["page"]["size"] + ", " + typo["font"] + " " + str(typo["size_pt"]) + "pt, line spacing " + str(typo["line_spacing"])
    lines = [
        head,
        page,
        "\\documentclass[12pt]{article}",
        "\\usepackage[a4paper,margin=1in]{geometry}",
        "\\usepackage{setspace}",
        "\\usepackage{lineno}",
        "\\usepackage{times}",
        "\\doublespacing",
        "\\linenumbers",
        "\\begin{document}",
        "",
        "\\title{%s}%% fill" % "Manuscript title",
        "\\author{%s}%% fill" % "Author One \\and Author Two",
        "\\date{}",
        "\\maketitle",
        "",
    ]
    for item in spec["sections"]:
        heading = item.get("heading")
        if item["id"] == "title":
            continue
        if heading:
            if item["kind"] == "abstract":
                lines += ["\\begin{abstract}", "[fill: abstract]", "\\end{abstract}", ""]
            else:
                lines += ["\\section*{%s}" % heading, "[fill: %s]" % item["id"], ""]
    lines += ["\\end{document}", ""]
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    return out_path


def main():
    ap = argparse.ArgumentParser(description="Generate journal templates from a spec")
    ap.add_argument("--journal", default="nature", choices=list(js.JOURNALS) + ["all"])
    ap.add_argument("--out", default=None, help="output directory (default: assets/journal-templates/generated)")
    ap.add_argument("--blank", action="store_true", help="no placeholder paragraphs")
    args = ap.parse_args()
    journals = list(js.JOURNALS) if args.journal == "all" else [args.journal]
    out_dir = args.out or os.path.join(os.path.dirname(HERE), "skills", "natsci-writing",
                                       "assets", "journal-templates", "generated")
    os.makedirs(out_dir, exist_ok=True)
    for journal in journals:
        spec = js.load(journal)
        docx_path = os.path.join(out_dir, "%s-%s.docx" % (journal, spec["article_type"]))
        tex_path = os.path.join(out_dir, "%s-%s.tex" % (journal, spec["article_type"]))
        build_docx(spec, docx_path, placeholders=not args.blank)
        build_tex(spec, tex_path)
        print("wrote %s" % docx_path)
        print("wrote %s" % tex_path)


if __name__ == "__main__":
    main()
