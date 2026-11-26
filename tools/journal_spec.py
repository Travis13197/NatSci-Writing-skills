#!/usr/bin/env python3
"""Shared spec handling for journal templates, assembly and format checking.

A journal spec is the single source of truth: the template generator, the
manuscript builder and the format checker all read the same JSON, so a style
cannot drift between what we generate and what we verify.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(HERE)
SPEC_DIR = os.path.join(PKG, "skills", "natsci-writing", "assets", "journal-templates", "specs")

JOURNALS = ("nature", "science")

DEFAULT_SPECS = {
    "nature": "nature-article.json",
    "science": "science-research-article.json",
}


def spec_path(journal):
    """Return the spec path for a journal key."""
    return os.path.join(SPEC_DIR, DEFAULT_SPECS[journal])


def load(journal="nature"):
    """Load a journal spec by key or by path."""
    path = journal if journal.endswith(".json") else spec_path(journal)
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def word_count(text):
    """Count words in a string, treating CJK characters as one word each."""
    text = re.sub(r"\[\d+\]", "", text or "")
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    latin = len(re.findall(r"[A-Za-z][A-Za-z'-]*", text))
    return cjk + latin


def section_ids(spec):
    """Ordered section ids declared by the spec."""
    return [s["id"] for s in spec["sections"]]


def required_sections(spec):
    """Section ids the spec marks as required."""
    return [s["id"] for s in spec["sections"] if s.get("required")]


def check_section_order(spec, found):
    """Return a list of order violations: sections present but out of spec order."""
    order = {sid: i for i, sid in enumerate(section_ids(spec))}
    seq = [order[s] for s in found if s in order]
    problems = []
    for a, b in zip(seq, seq[1:]):
        if b < a:
            problems.append("section order: %s appears before an earlier section" % found[seq.index(b)])
            break
    return problems
