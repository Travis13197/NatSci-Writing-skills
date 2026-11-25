#!/usr/bin/env python3
"""Validate the NatSci-Writing-skills package.

Checks package documents, skill frontmatter, reference links, absolute paths,
stale names, required assets and (optionally) installed copies.
No third-party dependency is required.
"""
import argparse
import hashlib
import json
import os
import re
import sys

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = [("natsci-writing", "en"), ("natsci-writing-zh", "zh")]
SYSTEM = "NatSci-Writing-skills"
OLD_NAMES = ["natlcy-skills", "NatLCY-skills",
             "nature-biology-manuscript-writing-zh",
             "nature-biology-manuscript-writing"]
ABS_PATTERNS = [re.compile(r"[A-Za-z]:\\\\"), re.compile(r"/Users/"), re.compile(r"/home/")]
PLACEHOLDER = re.compile(r"\b(TODO|TBD|FIXME)\b")
VERSION = open(os.path.join(PKG, "VERSION"), encoding="utf-8").read().strip() if os.path.exists(os.path.join(PKG, "VERSION")) else ""
PACKAGE_DOCS = [
    "README.md", "README.zh-CN.md", "CHANGELOG.md", "VERSION", "LICENSE",
    "NOTICE.md", "AUTHORS.md", "CITATION.cff",
    "docs/ARCHITECTURE.md", "docs/ARCHITECTURE.zh-CN.md",
    "docs/USAGE.md", "docs/USAGE.zh-CN.md", "docs/MIGRATION.md",
    "docs/MIGRATION.zh-CN.md", "docs/PUBLISHING.md", "docs/COVERAGE-AUDIT.md", "docs/COVERAGE-AUDIT.zh-CN.md",
    "examples/prompts-en.md",
    "examples/prompts-zh.md", "tools/validate_package.py", "tools/install.py",
    "tools/build_manifest.py", "manifest.json",
]


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None
    block = m.group(1)
    data = {}
    for line in block.splitlines():
        m2 = re.match(r"^\s*([A-Za-z_]+):\s*(.+?)\s*$", line)
        if not m2:
            continue
        key, val = m2.group(1), m2.group(2).strip()
        if val.startswith(('"', "'")) and val[-1:] == val[0]:
            val = val[1:-1]
        data[key] = val
    return data


def read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def display_path(path):
    """Return a package-relative path, or the absolute path when it lives elsewhere.

    Installs land outside PKG (often on another drive, where os.path.relpath
    raises ValueError); validation must still report the offending file.
    """
    try:
        return os.path.relpath(path, PKG)
    except ValueError:
        return path


def check_text(path, errors, warnings, strict_placeholders=True):
    text = read(path)
    rel = display_path(path)
    if not text.strip():
        errors.append(rel + ": empty file")
        return text
    for pattern in ABS_PATTERNS:
        if pattern.search(text):
            errors.append(rel + ": absolute path found")
            break
    for old in OLD_NAMES:
        if old in text:
            errors.append(rel + ": stale name " + old)
    if strict_placeholders and PLACEHOLDER.search(text):
        warnings.append(rel + ": TODO/TBD/FIXME marker")
    return text


def validate_skill(skill_dir, name, lang):
    errors, warnings = [], []
    sp = os.path.join(skill_dir, "SKILL.md")
    if not os.path.exists(sp):
        return ["missing SKILL.md"], []
    text = check_text(sp, errors, warnings)
    fm = parse_frontmatter(text)
    if not fm:
        errors.append(name + ": missing frontmatter")
    else:
        if fm.get("name") != name:
            errors.append(name + ": frontmatter name is " + str(fm.get("name")))
        if fm.get("version") != VERSION:
            errors.append(name + ": version is " + str(fm.get("version")))
        if fm.get("system") != SYSTEM:
            errors.append(name + ": system is " + str(fm.get("system")))
        if fm.get("language") != lang:
            errors.append(name + ": language is " + str(fm.get("language")))
        companion = "natsci-writing-zh" if lang == "en" else "natsci-writing"
        if fm.get("companion") != companion:
            errors.append(name + ": companion is " + str(fm.get("companion")))
    refs = re.findall(r"references/[A-Za-z0-9_.-]+\.md", text)
    for ref in sorted(set(refs)):
        if not os.path.exists(os.path.join(skill_dir, ref)):
            errors.append(name + ": missing reference " + ref)
    refdir = os.path.join(skill_dir, "references")
    if not os.path.isdir(refdir):
        errors.append(name + ": missing references/")
    else:
        files = [f for f in os.listdir(refdir) if f.endswith(".md")]
        if len(files) < 10:
            errors.append(name + ": too few reference files (" + str(len(files)) + ")")
        for f in files:
            check_text(os.path.join(refdir, f), errors, warnings, strict_placeholders=False)
    tdir = os.path.join(skill_dir, "assets", "templates")
    templates = [f for f in os.listdir(tdir)] if os.path.isdir(tdir) else []
    if len(templates) < 5:
        errors.append(name + ": fewer than five templates")
    cdir = os.path.join(skill_dir, "assets", "code")
    code = [f for f in os.listdir(cdir)] if os.path.isdir(cdir) else []
    if not any(f.endswith(".py") for f in code):
        errors.append(name + ": missing Python figure starter")
    if not any(f.endswith(".R") for f in code):
        errors.append(name + ": missing R figure starter")
    if os.path.exists(os.path.join(skill_dir, "_test_out")):
        errors.append(name + ": stray _test_out directory")
    cl = os.path.join(skill_dir, "CHANGELOG.md")
    if not os.path.exists(cl):
        warnings.append(name + ": missing per-skill CHANGELOG.md")
    return errors, warnings


def validate_package():
    errors, warnings = [], []
    for rel in PACKAGE_DOCS:
        if not os.path.exists(os.path.join(PKG, rel)):
            errors.append("missing package document: " + rel)
    version = VERSION
    if not version:
        errors.append("VERSION is " + version)
    if os.path.exists(os.path.join(PKG, "LICENSE")):
        lic = read(os.path.join(PKG, "LICENSE"))
        if "Non-Commercial" not in lic:
            errors.append("LICENSE is not the NatSci non-commercial license")
        if "Chuanyang Liu" not in lic:
            errors.append("LICENSE does not name the author")
    apache = os.path.join(PKG, "LICENSES", "Apache-2.0.txt")
    if not os.path.exists(apache) or "Apache License" not in read(apache):
        errors.append("missing third-party Apache-2.0 license text")
    if os.path.exists(os.path.join(PKG, "CITATION.cff")):
        cite = read(os.path.join(PKG, "CITATION.cff"))
        if ("Chuanyang" not in cite) or ("Liu" not in cite):
            errors.append("CITATION.cff does not name the author")
        if not version or version not in cite:
            errors.append("CITATION.cff version does not match VERSION")
    for name, lang in SKILLS:
        sd = os.path.join(PKG, "skills", name)
        if not os.path.isdir(sd):
            errors.append("missing skill directory: " + name)
            continue
        e, w = validate_skill(sd, name, lang)
        errors += e
        warnings += w
    if os.path.exists(os.path.join(PKG, "manifest.json")):
        try:
            man = json.loads(read(os.path.join(PKG, "manifest.json")))
            if man.get("version") != version:
                errors.append("manifest version does not match VERSION")
            names = {s.get("name") for s in man.get("skills", [])}
            if names != {s[0] for s in SKILLS}:
                errors.append("manifest skills do not match package skills")
        except Exception as exc:
            errors.append("manifest.json unreadable: " + str(exc))
    return errors, warnings


def validate_installed(target):
    errors, warnings = [], []
    for name, lang in SKILLS:
        sd = os.path.join(target, name)
        if not os.path.isdir(sd):
            errors.append("installed skill missing: " + name)
            continue
        e, w = validate_skill(sd, name, lang)
        errors += e
        warnings += w
    return errors, warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--installed", metavar="DIR", help="validate skill copies in this skills directory")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()
    if args.installed:
        errors, warnings = validate_installed(os.path.abspath(os.path.expanduser(args.installed)))
        scope = "installed copies at " + args.installed
    else:
        errors, warnings = validate_package()
        scope = "package " + PKG
    if args.strict:
        errors += warnings
        warnings = []
    result = {"scope": scope, "ok": not errors, "errors": errors, "warnings": warnings}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("NatSci-Writing-skills validator")
        print("scope:", scope)
        print("status:", "PASS" if not errors else "FAIL")
        for item in errors:
            print("  ERROR:", item)
        for item in warnings:
            print("  WARN :", item)
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())