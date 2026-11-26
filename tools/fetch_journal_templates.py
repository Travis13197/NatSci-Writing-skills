#!/usr/bin/env python3
"""Import the publisher's own manuscript templates.

Publishers serve their Word and LaTeX templates behind interactive pages, so this
tool never pretends to bypass that: it records the official locations and hashes,
copies files you downloaded in a browser into the skill's template folder, and
verifies that a file is the expected artefact before the builder will use it.

  python tools/fetch_journal_templates.py --list
  python tools/fetch_journal_templates.py --from-dir ~/Downloads
  python tools/fetch_journal_templates.py --check

When a template is present the assembler uses it (--template), borrowing its
styles; otherwise it falls back to the generated template from
make_journal_template.py.
"""
import argparse
import hashlib
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(HERE)
DEST = os.path.join(PKG, "skills", "natsci-writing", "assets", "journal-templates", "official")
MANIFEST = os.path.join(HERE, "journal_template_sources.json")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load():
    with open(MANIFEST, encoding="utf-8") as fh:
        return json.load(fh)


def cmd_list():
    data = load()
    print("Official template sources (download in a browser, then import):\n")
    for item in data["templates"]:
        print("- %s [%s]" % (item["id"], item["journal"]))
        print("    page : %s" % item["page"])
        print("    file : %s" % item.get("file", "(linked from the page)"))
        print("    note : %s" % item["note"])
        print("    dest : official/%s" % item["dest"])
    print("\nImport with: --from-dir <folder containing the downloaded files>")


def cmd_import(folder):
    data = load()
    os.makedirs(DEST, exist_ok=True)
    imported, missing = [], []
    for item in data["templates"]:
        src = os.path.join(folder, os.path.basename(item["dest"]))
        if not os.path.exists(src):
            missing.append(item["dest"])
            continue
        dst = os.path.join(DEST, os.path.basename(item["dest"]))
        shutil.copy2(src, dst)
        digest = sha256(dst)
        expected = item.get("sha256")
        status = "verified" if expected and expected == digest else ("recorded" if not expected else "HASH MISMATCH")
        imported.append({"id": item["id"], "path": dst, "sha256": digest, "status": status})
        item["sha256"] = item.get("sha256") or digest
    if imported:
        with open(MANIFEST, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
    for row in imported:
        print("imported %-22s %s" % (row["id"], row["status"]))
    for name in missing:
        print("missing  %s (download it from the page listed by --list)" % name)
    return 0 if imported else 2


def cmd_check():
    data = load()
    ok = True
    for item in data["templates"]:
        path = os.path.join(DEST, os.path.basename(item["dest"]))
        if not os.path.exists(path):
            print("absent   %-22s -> generated template will be used" % item["id"])
            continue
        digest = sha256(path)
        if item.get("sha256") and digest != item["sha256"]:
            print("MISMATCH %-22s expected %s got %s" % (item["id"], item["sha256"][:12], digest[:12]))
            ok = False
        else:
            print("present  %-22s %s" % (item["id"], digest[:12]))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="Import publisher manuscript templates")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--from-dir", default=None)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if args.list or not (args.from_dir or args.check):
        cmd_list()
        return 0
    if args.from_dir:
        return cmd_import(args.from_dir)
    return cmd_check()


if __name__ == "__main__":
    sys.exit(main())
