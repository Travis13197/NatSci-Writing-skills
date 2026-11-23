#!/usr/bin/env python3
"""Scan prose for AI-tone, defensive/self-limiting and template-contrast language."""
import argparse
import json
import os
import re
import sys

EN_ERROR = [
    ("contrast.not_only_but", r"\bnot only\b[^.!?]{0,90}\bbut also\b"),
    ("contrast.not_just_but", r"\bnot just\b[^.!?]{0,90}\bbut\b"),
    ("contrast.not_merely_but", r"\bnot merely\b[^.!?]{0,90}\bbut\b"),
    ("contrast.not_x_but_y", r"\bnot\b[^.!?]{0,70}\bbut (rather )?\b"),
    ("contrast.it_is_not_x_it_is_y", r"\b(it is|it's) not\b[^.!?]{0,90}\bit('s| is)\b"),
    ("contrast.not_because_but", r"\bnot because\b[^.!?]{0,80}\bbut because\b"),
    ("contrast.not_x_but_rather", r"\bnot\b[^.!?]{0,70}\bbut rather\b"),
    ("contrast.not_rather_than", r"\bnot\b[^.!?]{0,70}\brather than\b"),
    ("contrast.rather_than", r"\brather than\b"),
    ("contrast.far_from", r"\bfar from\b[^.!?]{0,50},"),
    ("defensive.important_to_note", r"\bit is (important|worth|crucial|necessary) to (note|mention|emphasize|highlight)\b"),
    ("defensive.it_should_be_noted", r"\bit should be noted\b"),
    ("defensive.to_some_extent", r"\b(to some extent|to a certain extent|in some sense|arguably|presumably|seemingly)\b"),
    ("defensive.further_research", r"\bfurther (research|work|studies) (is|are) (needed|required|warranted)\b"),
    ("defensive.interpret_with_caution", r"\b(the findings|results) should be interpreted with caution\b"),
    ("defensive.cannot_be_overstated", r"\bcannot be overstated\b"),
    ("defensive.available_information", r"\bbased on (the )?available (information|data|sources)\b"),
    ("defensive.does_not_establish", r"\bdoes not (by itself )?(establish|prove|imply)\b"),
    ("defensive.while_limited", r"\bwhile (the )?(data|evidence|results|study|sample) (are|is) limited\b"),
    ("structural.in_conclusion", r"(?m)^\s*(In conclusion|In summary|Overall)\b"),
]
ZH_ERROR = [
    ("contrast.bushi_ershi", r"不是[^。！？]{0,45}(而是|是)"),
    ("contrast.bingfei_ershi", r"并非[^。！？]{0,45}而是"),
    ("contrast.bingbu_ershi", r"并不[^。！？]{0,45}，?而是"),
    ("contrast.bu_ershi_comma", r"不[^。！？]{0,45}，\s*而是"),
    ("contrast.bu_ershi", r"不[^。！？]{0,45}而是"),
    ("contrast.yuqishuo", r"与其说[^。！？]{0,35}不如说"),
    ("contrast.bujin_erqie", r"不仅[^。！？]{0,45}(而且|更是|还)"),
    ("contrast.buzhishi_gengshi", r"不只是[^。！？]{0,35}更是"),
    ("contrast.buxuyao_zhi", r"不需要[^。！？]{0,35}只需要"),
    ("contrast.kan si_shize", r"看似[^。！？]{0,35}(实则|其实)"),
    ("contrast.biaomian_shiji", r"表面(上)?[^。！？]{0,35}(实际上|实则)"),
    ("contrast.suowei_bushi", r"所谓[^。！？]{0,35}并不是"),
    ("contrast.comma_bushi", r"[^。！？]{2,45}，\s*(而不是|并非|不是|而非)"),
    ("contrast.bu_er", r"不(是|仅|只|再|会|能|应)[^。！？]{0,30}(而|，)"),
    ("defensive.zhide_zhuyi", r"(值得注意的是|需要指出的是|需要强调的是|必须承认|不可否认|毋庸置疑|毋庸讳言|众所周知)"),
    ("defensive.chengran", r"(诚然|固然)"),
    ("defensive.hedge", r"(在一定程度上|在某种意义上|某种意义上|或许|也许|有望|尚需|有待|仅供参考)"),
    ("defensive.self_limiting", r"(不成熟|浅析|抛砖引玉|难免|限于篇幅|不再赘述|以期|试图|旨在)"),
    ("structural.lubiao", r"(?m)^\s*(首先|其次|最后|总而言之|综上所述|由此可见|不难看出|总的来说|总之)[，,：:]"),
    ("structural.info_repeat", r"(换句话说|也就是说)"),
    ("structural.symbol_inflation", r"(见证了|承载着|彰显了|标志着|意味着)"),
    ("structural.let_chain", r"(让[^。！？]{0,25}(能够|拥有|可以)|使得)"),
]
AI_WORDS = ["delve", "underscore", "intricate", "intricacies", "realm", "tapestry", "testament",
            "nuanced", "multifaceted", "meticulous", "commendable", "garner", "boast", "leverage",
            "robust", "pivotal", "crucial", "vital", "foster", "navigate", "landscape", "showcase",
            "underpin", "notably", "comprehensive", "seamless", "holistic", "paradigm",
            "transformative", "groundbreaking", "unprecedented", "state-of-the-art", "cutting-edge"]
ZH_AI_WORDS = ["赋能", "助力", "闭环", "抓手", "生态", "范式", "图景", "底层逻辑", "组合拳", "破局",
               "重塑", "颠覆", "革命性", "里程碑", "新篇章", "注入新动能", "按下加速键", "提供新思路",
               "奠定基础", "开辟新方向", "具有广阔前景", "具有重要意义", "发挥关键作用", "至关重要",
               "全面", "深度", "高度", "系统性地", "有效地", "显著地"]


def strip_fences(text):
    fence = chr(96) * 3
    return re.sub(r"(?ms)^(~~~|" + fence + r").*?^\1\s*$", "", text)


def scan(text, lang="auto"):
    text = strip_fences(text)
    hits = []
    checks = EN_ERROR + ZH_ERROR if lang == "auto" else (EN_ERROR if lang == "en" else ZH_ERROR)
    for i, line in enumerate(text.splitlines(), 1):
        for rule, pattern in checks:
            for m in re.finditer(pattern, line, re.I if lang != "zh" else 0):
                hits.append({"line": i, "rule": rule, "severity": "ERROR",
                             "match": m.group(0)[:120], "context": line.strip()[:240]})
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    zh_chars = len(re.findall("[一-鿿]", text))
    en_hits = [(w, len(re.findall(r"\b" + re.escape(w) + r"\b", text, re.I))) for w in AI_WORDS]
    zh_hits = [(w, text.count(w)) for w in ZH_AI_WORDS]
    total_en = sum(c for _, c in en_hits)
    total_zh = sum(c for _, c in zh_hits)
    if words and total_en * 1000 / max(1, len(words)) > 5:
        hits.append({"line": 0, "rule": "lexicon.en_density", "severity": "WARN",
                     "match": f"{total_en} hits / {len(words)} words",
                     "context": str(sorted([x for x in en_hits if x[1]], key=lambda x: -x[1])[:10])})
    if zh_chars and total_zh * 1000 / max(1, zh_chars) > 5:
        hits.append({"line": 0, "rule": "lexicon.zh_density", "severity": "WARN",
                     "match": f"{total_zh} hits / {zh_chars} characters",
                     "context": str(sorted([x for x in zh_hits if x[1]], key=lambda x: -x[1])[:10])})
    return hits


def collect(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, names in os.walk(p):
                for n in names:
                    if n.endswith((".md", ".txt")):
                        files.append(os.path.join(root, n))
        else:
            files.append(p)
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=["."])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lang", choices=["auto", "en", "zh"], default="auto")
    ap.add_argument("--fail-on", choices=["error", "warn", "none"], default="error")
    args = ap.parse_args()
    files = collect(args.paths or ["."])
    report = []
    for f in files:
        try:
            text = open(f, encoding="utf-8").read()
        except Exception:
            continue
        hits = scan(text, args.lang)
        if hits:
            report.append({"file": f, "hits": hits})
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        total = sum(len(r["hits"]) for r in report)
        print(f"Prose style scan: {len(files)} file(s) scanned, {total} hit(s)")
        for r in report:
            print("\n" + r["file"])
            for h in r["hits"]:
                print(f"  {h['severity']:5s} L{h['line']:<4d} {h['rule']}: {h['match']}")
                if h["context"]:
                    print(f"        {h['context']}")
    if args.fail_on == "none":
        return 0
    bad = any(h["severity"] == "ERROR" or (args.fail_on == "warn" and h["severity"] == "WARN")
              for r in report for h in r["hits"])
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
