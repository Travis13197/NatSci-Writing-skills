#!/usr/bin/env python3
"""Check a manuscript against a journal spec.

Reads the .docx the builder produced and verifies page setup, typography,
continuous line numbering, section presence and order, abstract length,
reference cap and citation superscripts. Critical failures exit 1; advisory
findings are reported without failing the run.

Default journal: nature.
"""
import argparse
import json
import os
import re
import sys

from docx import Document
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import journal_spec as js  # noqa: E402

PAGE_MM = {"A4": (210.0, 297.0), "Letter": (215.9, 279.4)}
STYLE = {
    "title": "NSC Title", "authors": "NSC Authors", "affiliations": "NSC Affiliations",
    "heading1": "NSC Heading 1", "heading2": "NSC Heading 2", "body": "NSC Body",
    "abstract": "NSC Abstract", "caption": "NSC Caption", "reference": "NSC Reference",
}
CITE = re.compile(r"\[(\d[\d,\s\u2013-]*)\]")


def mm(value):
    """EMU to millimetres."""
    return round(value / 36000.0, 1)


def collect(doc):
    """Return heading names in order, section text, and the paragraphs by style."""
    headings, texts, by_style = [], {}, {}
    current = None
    for para in doc.paragraphs:
        style = para.style.name if para.style is not None else ""
        by_style.setdefault(style, []).append(para)
        if style == STYLE["heading1"]:
            current = para.text.strip()
            headings.append(current)
            texts.setdefault(current, [])
            continue
        if current is not None and para.text.strip():
            texts[current].append(para.text)
    return headings, texts, by_style


def main():
    ap = argparse.ArgumentParser(description="Check a manuscript against a journal spec")
    ap.add_argument("docx")
    ap.add_argument("--journal", default="nature", choices=list(js.JOURNALS))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    spec = js.load(args.journal)
    doc = Document(args.docx)
    headings, texts, by_style = collect(doc)
    results = []

    def check(name, ok, detail, critical=True):
        results.append({"check": name, "pass": bool(ok), "detail": detail, "critical": critical})

    # page setup
    sec = doc.sections[0]
    want = spec["page"]
    got = {"w_mm": mm(sec.page_width), "h_mm": mm(sec.page_height),
           "margins_in": {k: round(getattr(sec, k + "_margin").inches, 2) for k in ("top", "bottom", "left", "right")}}
    size_ok = abs(got["w_mm"] - PAGE_MM[want["size"]][0]) < 3 and abs(got["h_mm"] - PAGE_MM[want["size"]][1]) < 3
    check("page size", size_ok, "%s (%.0fx%.0f mm) vs %s" % (want["size"], got["w_mm"], got["h_mm"], "ok" if size_ok else "mismatch"))
    margin_bad = [k for k, v in want["margins_in"].items() if abs(got["margins_in"][k] - v) > 0.05]
    check("margins", not margin_bad, "1.0 in all sides" if not margin_bad else "off: " + ",".join(margin_bad))

    # line numbers
    ln = sec._sectPr.find(qn("w:lnNumType"))
    cont = ln is not None and ln.get(qn("w:restart")) in ("continuous", None)
    check("continuous line numbers", cont, "present" if cont else "missing w:lnNumType")

    # typography on body and abstract paragraphs
    for key in ("body", "abstract"):
        paras = by_style.get(STYLE[key]) or []
        if not paras:
            check("%s paragraphs present" % key, False, "no paragraph with style " + STYLE[key])
            continue
        want_t = spec["typography"][key]
        bad_font, bad_size, bad_space = set(), set(), set()
        for para in paras:
            for run in para.runs:
                if run.font.name and run.font.name != want_t["font"]:
                    bad_font.add(run.font.name)
                if run.font.size and abs(run.font.size.pt - want_t["size_pt"]) > 0.5:
                    bad_size.add(run.font.size.pt)
            sp = para.paragraph_format.line_spacing or (para.style.paragraph_format.line_spacing)
            if sp and abs(float(sp) - float(want_t["line_spacing"])) > 0.01:
                bad_space.add(float(sp))
        check("%s font" % key, not bad_font, want_t["font"] if not bad_font else "found " + ",".join(map(str, bad_font)))
        check("%s size" % key, not bad_size, "%dpt" % want_t["size_pt"] if not bad_size else "found " + ",".join(map(str, bad_size)))
        check("%s line spacing" % key, not bad_space, "%.1f" % want_t["line_spacing"] if not bad_space else "found " + ",".join("%.2f" % x for x in bad_space))

    # sections: presence, order, required
    declared = [s for s in spec["sections"] if s.get("heading")]
    found_ids = []
    for item in declared:
        if item["heading"] in headings:
            found_ids.append(item)
    missing = [s for s in spec["sections"] if s.get("required") and s.get("heading") and s["heading"] not in headings]
    check("required sections present", not missing, "all present" if not missing else "missing: " + ", ".join(s["id"] for s in missing))

    order = {s["id"]: i for i, s in enumerate(spec["sections"])}
    seq = [order[s["id"]] for s in found_ids]
    order_ok = all(b >= a for a, b in zip(seq, seq[1:]))
    check("section order", order_ok, "matches spec" if order_ok else "out of order")

    # abstract length
    abstract = " ".join(x.text for x in by_style.get(STYLE["abstract"], []))
    n_abs = js.word_count(abstract)
    lo, hi = spec["checks"]["abstract_word_range"]
    check("abstract length", lo <= n_abs <= hi, "%d words (spec %d-%d)" % (n_abs, lo, hi), critical=False)

    # references
    refs = [p.text for p in by_style.get(STYLE["reference"], []) if p.text.strip()]
    cap = spec["checks"]["reference_cap"]
    check("reference count", len(refs) <= cap, "%d items (cap %d)" % (len(refs), cap), critical=False)

    # citations superscripted
    sup = 0
    plain = 0
    for para in by_style.get(STYLE["body"], []) + by_style.get(STYLE["abstract"], []):
        for run in para.runs:
            if run.font.superscript and run.text.strip():
                sup += 1
            if CITE.search(run.text or "") and not run.font.superscript:
                plain += len(CITE.findall(run.text))
    check("citations superscript", plain == 0, "%d superscript runs, %d plain bracketed citations" % (sup, plain))

    failed = [r for r in results if not r["pass"] and r["critical"]]
    if args.json:
        print(json.dumps({"file": args.docx, "journal": args.journal, "results": results,
                          "pass": not failed, "critical_failures": len(failed)}, indent=2, ensure_ascii=False))
    else:
        print("Journal format check: %s (%s)" % (os.path.basename(args.docx), spec["display_name"]))
        for r in results:
            tag = "PASS" if r["pass"] else ("FAIL" if r["critical"] else "WARN")
            print("  %-4s %-28s %s" % (tag, r["check"], r["detail"]))
        print("\nRESULT: %s (%d critical failures)" % ("PASS" if not failed else "FAIL", len(failed)))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
