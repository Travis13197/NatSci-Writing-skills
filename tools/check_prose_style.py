#!/usr/bin/env python3
"""Scan prose for AI-tone, defensive/self-limiting and template-contrast language.

Two modes beyond a plain scan:

  --metrics FILE...   report rhythm and density metrics (sentence-length CV,
                      hedge/recap/triad/nominalisation/em-dash density)
  --gate FILE...      fail when any ERROR fires, when a defensive or AI marker
                      fires, or when a metric leaves its band

Exit codes: 0 clean, 1 failed gate, 2 usage error.
"""
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
    ("contrast.comma_not", r"[A-Za-z0-9)],\s+not\s+(the|a|an|its|their|this|that|these|those)\b"),
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
    # 1.2.7.0 — sourced from the anti-defensive-writing review
    ("defensive.one_might_argue", r"\b(one might (argue|object|worry)|it (could|may) be argued|critics (might|may) (argue|say))\b"),
    ("defensive.still_lags", r"\b(still (lags?|falls? short)|remains? (a )?(challenging|difficult|elusive|open) (problem|question))\b"),
    ("defensive.plays_role", r"\bplays? (a|an) (crucial|vital|key|important|pivotal) role\b"),
    ("ai.roadmap", r"\b(the remainder of (this|the) (paper|article) is (organized|structured)|this paper (aims|seeks) to)\b"),
]

EN_ADVISORY = [
    ("defensive.false_modesty", r"\b(we (merely|only) (show|provide|report)|a first step|preliminary (results?|study|exploration)|proof of concept)\b"),
    ("defensive.we_acknowledge", r"\bwe (readily )?(acknowledge|recognize|concede)\b"),
    ("defensive.negative_framing", r"\b(suffers? from|limited (improvement|gain|benefit|success)|modest (improvement|gain))\b"),
    ("defensive.unfortunately", r"\b(unfortunately|regrettably)\b"),
    ("ai.notably", r"\b(notably|importantly),\s"),
    ("ai.taken_together", r"(?m)^\s*(Taken together|Collectively,)\b"),
    ("ai.valuable_insight", r"\b(provides? (a )?(valuable|useful|new) (insight|perspective|framework)|sheds? light on)\b"),
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
    # 1.2.7.0
    ("ai.zh_suizhe", r"(随着[^。]{0,20}(的)?(快速)?(发展|进步|推进)|在[^。]{0,20}(背景|浪潮)下)"),
    ("ai.zh_yiyi", r"(具有(重要|一定|深远)的?(理论|现实|实践|指导)?意义|提供了?(新|重要)的?(思路|方向|参考)|奠定(了)?(坚实)?基础)"),
    ("ai.zh_yaocai", r"(首先[^。]{0,40}其次|一方面[^。]{0,40}另一方面)"),
]

ZH_ADVISORY = [
    ("defensive.zh_qianxu", r"(不揣浅陋|一得之见|挂一漏万|难免有?疏漏|限于条件)"),
    ("defensive.zh_tiaojian", r"(由于(条件|时间|数据)限制|受限于|本研究的?不足)"),
    ("ai.zh_chubu", r"(初步(探索|研究|验证|实现)|尝试性地|尚属首次)"),
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

HEDGES_EN = r"\b(may|might|could|possibly|potentially|arguably|seemingly|apparently|somewhat|relatively|to some extent)\b"
HEDGES_ZH = r"(或许|也许|可能|有望|尚需|有待|一定程度上|某种意义上|大约|左右|似乎|看来)"
LIMIT_EN = r"\b(limitation|limitations|caveat|caveats|shortcoming|shortcomings)\b"
LIMIT_ZH = r"(局限|不足|限制条件|局限性地)"

def safe_json(obj):
    """Print JSON without dying on a non-UTF-8 console (Windows defaults to GBK)."""
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    text = json.dumps(obj, indent=2, ensure_ascii=False)
    try:
        print(text)
    except UnicodeEncodeError:
        print(json.dumps(obj, indent=2, ensure_ascii=True))


GATE = {
    "en": {"cv": (0.30, 0.65), "recap": 1.0, "hedge": 4.0, "triad": 2.0,
           "nominal": 0.12, "emdash": 2.0, "limitation": 2.0},
    "zh": {"cv": (0.30, 0.75), "recap": 1.0, "hedge": 4.0, "triad": 2.0,
           "nominal": 1.0, "emdash": 2.0, "limitation": 2.0},
}


def strip_fences(text):
    fence = chr(96) * 3
    return re.sub(r"(?ms)^(~~~|" + fence + r").*?^\1\s*$", "", text)


def norm(rules):
    out = []
    for item in rules:
        if len(item) == 3:
            out.append(item)
        else:
            out.append((item[0], item[1], "ERROR"))
    return out


def detect_lang(text):
    zh = len(re.findall("[\u4e00-\u9fff]", text))
    en = len(re.findall(r"[A-Za-z]", text))
    return "zh" if zh > en / 2 else "en"


def prose_only(text):
    """Drop code, tables, headings, bullets and quotes so metrics describe running prose.

    A diagnostics document that tabulates banned patterns, or a README built from
    bullet lists, is not a manuscript; counting its dashes and triads measures the
    table, not the writing.
    """
    fence = chr(96) * 3
    keep = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", "|", ">", "-", "*", "+")):
            continue
        if s.startswith(fence) or s.startswith("~~~"):
            continue
        if s.startswith("<") or s.count("|") >= 2:
            continue
        keep.append(line)
    return "\n".join(keep)


def metrics(text, lang):
    body = prose_only(strip_fences(text))
    if lang == "zh":
        sents = [s for s in re.split(r"(?<=[。！？])", body) if s.strip()]
        lens = [len(re.findall("[\u4e00-\u9fff]", s)) for s in sents]
        lens = [x for x in lens if x > 0]
        unit = max(1, sum(lens))
        hedge = len(re.findall(HEDGES_ZH, body))
        limit = len(re.findall(LIMIT_ZH, body))
        triads = len(re.findall(r"[\u4e00-\u9fff]{1,6}、[\u4e00-\u9fff]{1,6}、[\u4e00-\u9fff]{1,6}", body))
        recap = len(re.findall(r"(综上所述|总而言之|由此可见|总的来说|总之)", body))
    else:
        sents = [s for s in re.split(r"(?<=[.!?])\s+", body) if s.strip()]
        lens = [len(re.findall(r"[A-Za-z][A-Za-z'-]*", s)) for s in sents]
        lens = [x for x in lens if x > 0]
        words = re.findall(r"[A-Za-z][A-Za-z'-]*", body)
        unit = max(1, len(words))
        hedge = len(re.findall(HEDGES_EN, body, re.I))
        limit = len(re.findall(LIMIT_EN, body, re.I))
        triads = len(re.findall(r"\b[A-Za-z][A-Za-z-]{2,12}, [A-Za-z][A-Za-z-]{2,12}, (?:and |or )[A-Za-z][A-Za-z-]{2,12}\b", body))
        recap = len(re.findall(r"\b(In summary|In conclusion|Overall|Taken together|Collectively)\b", body))
    n = len(lens)
    mean = sum(lens) / n if n else 0
    var = sum((x - mean) ** 2 for x in lens) / n if n else 0
    cv = (var ** 0.5) / mean if mean else 0
    content = re.findall(r"[A-Za-z][A-Za-z'-]{3,}", body) if lang == "en" else []
    nominal = [w for w in content if re.search(r"(tion|sion|ment|ance|ence|ity|ness)$", w.lower())]
    return {
        "units": unit,
        "sentences": n,
        "mean_sentence_len": round(mean, 2),
        "sentence_cv": round(cv, 3),
        "recap_per_1k": round(recap * 1000 / unit, 2),
        "hedge_per_1k": round(hedge * 1000 / unit, 2),
        "limitation_per_1k": round(limit * 1000 / unit, 2),
        "triad_per_500": round(triads * 500 / unit, 2),
        "nominalisation_ratio": round(len(nominal) / max(1, len(content)), 3) if lang == "en" else 0.0,
        "emdash_per_1k": round(body.count("\u2014") * 1000 / max(1, unit), 2),
    }


GENRE_FACTOR = {"paper": 1.0, "perspective": 1.75, "report": 1.0}


def gate_failures(m, lang, genre="paper"):
    if genre == "report":
        return []
    g = GATE[lang]
    k = GENRE_FACTOR.get(genre, 1.0)
    out = []
    lo, hi = g["cv"]
    if m["sentences"] >= 8 and not (lo <= m["sentence_cv"] <= hi):
        out.append(f"sentence_cv={m['sentence_cv']} outside [{lo}, {hi}]")
    caps = (("recap_per_1k", g["recap"], 1.0), ("hedge_per_1k", g["hedge"], k),
            ("triad_per_500", g["triad"], 1.0), ("emdash_per_1k", g["emdash"], 1.0),
            ("limitation_per_1k", g["limitation"], k))
    for key, cap, factor in caps:
        cap = cap * factor
        if m[key] > cap:
            out.append(f"{key}={m[key]} > {cap}")
    if lang == "en" and m["nominalisation_ratio"] > g["nominal"]:
        out.append(f"nominalisation_ratio={m['nominalisation_ratio']} > {g['nominal']}")
    return out


def scan(text, lang="auto"):
    text = strip_fences(text)
    hits = []
    lang = detect_lang(text) if lang == "auto" else lang
    checks = (norm(EN_ERROR + EN_ADVISORY) if lang == "en" else norm(ZH_ERROR + ZH_ADVISORY))
    for i, line in enumerate(text.splitlines(), 1):
        for rule, pattern, sev in checks:
            for m in re.finditer(pattern, line, re.I if lang == "en" else 0):
                hits.append({"line": i, "rule": rule, "severity": sev,
                             "match": m.group(0)[:120], "context": line.strip()[:240]})
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    zh_chars = len(re.findall("[\u4e00-\u9fff]", text))
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
    return hits, lang


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


def read(path):
    try:
        return open(path, encoding="utf-8").read()
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=["."])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lang", choices=["auto", "en", "zh"], default="auto")
    ap.add_argument("--fail-on", choices=["error", "warn", "none"], default="error")
    ap.add_argument("--metrics", action="store_true", help="report rhythm and density metrics")
    ap.add_argument("--gate", action="store_true", help="fail on any defensive/AI marker or out-of-band metric")
    ap.add_argument("--genre", choices=["paper", "perspective", "report"], default="paper",
                    help="paper tightens hedging; perspective allows proposal modality; report is metrics-only")
    args = ap.parse_args()
    files = collect(args.paths or ["."])
    report = []
    for f in files:
        text = read(f)
        if not text:
            continue
        hits, lang = scan(text, args.lang)
        if hits:
            report.append({"file": f, "hits": hits, "lang": lang})

    if args.metrics or args.gate:
        rows = []
        for f in files:
            text = read(f)
            if not text:
                continue
            lang = detect_lang(text) if args.lang == "auto" else args.lang
            m = metrics(text, lang)
            fails = gate_failures(m, lang, args.genre)
            rows.append({"file": f, "lang": lang, "metrics": m, "failures": fails})
        if args.json:
            safe_json({"metrics": rows, "hits": report})
        else:
            print(f"Prose metrics: {len(rows)} file(s)")
            for r in rows:
                m = r["metrics"]
                print(f"\n{r['file']}  [{r['lang']}]  units={m['units']} sentences={m['sentences']}")
                print(f"  sentence_cv={m['sentence_cv']:<7} mean_len={m['mean_sentence_len']:<7}"
                      f" hedge/1k={m['hedge_per_1k']:<6} recap/1k={m['recap_per_1k']:<6}"
                      f" limit/1k={m['limitation_per_1k']:<6} triad/500={m['triad_per_500']:<6}"
                      f" nominal={m['nominalisation_ratio']:<6} emdash/1k={m['emdash_per_1k']}")
                if r["failures"]:
                    print("  GATE FAIL: " + "; ".join(r["failures"]))
        if not args.gate:
            return 0
        gate_bad = any(r["failures"] for r in rows) or any(
            h["severity"] == "ERROR" or h["rule"].startswith(("defensive.", "ai."))
            for r in report for h in r["hits"])
        return 1 if gate_bad else 0

    if args.json:
        safe_json(report)
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
