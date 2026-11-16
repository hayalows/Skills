#!/usr/bin/env python3
"""Threadline 0.1: independent, model-agnostic natural prose planning and diagnostics.

Standard library only. Does NOT train a neural model or prove human authorship.
"""
from __future__ import annotations
import argparse
import json
import math
import os
import re
import statistics
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any

VERSION = "0.1.0"
WORD_RE = re.compile(r"\b[^\W\d_]+(?:['’\-][^\W\d_]+)*\b", re.UNICODE)
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[\"'‘“(]*[A-Z0-9])", re.UNICODE)
# These are diagnostics, never a blacklist: any phrase can be justified in context.
STOCK_PATTERNS = {
    "generic_time_opening": r"\bin today['’]s (?:fast[- ]paced )?world\b",
    "empty_preamble": r"\bit is important to note that\b|\bhere['’]s the thing\b",
    "vague_booster": r"\bgame[- ]changer\b|\btruly revolutionary\b|\bunparalleled\b",
    "unearned_pivot": r"\bit['’]s not (?:just |only )?.{4,70}?,? (?:but|it['’]s) (?:also )?\b",
    "generic_conclusion": r"\bin conclusion\b|\bat the end of the day\b",
}
HIGH_CERTAINTY = re.compile(r"\b(always|never|everyone|no one|guarantee(?:d|s)?|100\s*%)\b", re.I)
CONNECTOR_WORDS = {"because", "therefore", "although", "however", "but", "so", "for example", "for instance", "instead", "if", "when", "unless", "yet"}
COMMON = set("the a an and but or if that this these those it is are was were be been being in on at to of for by with from as not you your we our they them he she his her i my their me us its which who where when how why what then so do does did have has had can could should would will about more most some many very just each every there here into over after before than also one two three such all any only both".split())


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def sentences(text: str) -> list[str]:
    # Lightweight rule, not a full NLP tokenizer. Abbreviations can be split incorrectly.
    text = re.sub(r"\s+", " ", text.strip())
    return [s.strip() for s in SENTENCE_RE.split(text) if s.strip()]


def paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip() and not p.strip().startswith("# ")]


def content_set(p: str) -> set[str]:
    return {w.lower() for w in words(p) if len(w)>3 and w.lower() not in COMMON}


def analyze(text: str, genre: str = "general") -> dict[str, Any]:
    ws = words(text)
    ss = sentences(text)
    ps = paragraphs(text)
    lengths = [len(words(s)) for s in ss]
    count = len(ws)
    avg = statistics.mean(lengths) if lengths else 0.0
    median = statistics.median(lengths) if lengths else 0.0
    cv = statistics.pstdev(lengths)/avg if len(lengths)>1 and avg else 0.0
    avg_word_chars = sum(len(w) for w in ws)/count if count else 0.0
    # Automated Readability Index; grade is *not* a quality or naturalness metric.
    ari = (4.71 * avg_word_chars + 0.5 * count/max(len(ss),1) - 21.43) if ws else None
    starts = [" ".join(x.lower() for x in words(s)[:2]) for s in ss if len(words(s))>=2]
    repeated = {k:v for k,v in Counter(starts).items() if v>=3}
    para_normalized = [" ".join(w.lower() for w in words(p)) for p in ps]
    duplicates = len(para_normalized) - len(set(para_normalized))
    tokens = [w.lower() for w in ws]
    grams = [tuple(tokens[i:i+5]) for i in range(max(0,len(tokens)-4))]
    ngram_repeats = sum(v-1 for v in Counter(grams).values() if v>1)
    # Inspect beginning / middle / end independently in a long document.
    thirds = []
    if count >= 700 and len(ps) >= 6:
        blocks=[[],[],[]]
        running=0
        for p in ps:
            bucket=min(2, int(3*running/max(count,1)))
            blocks[bucket].append(p)
            running+=len(words(p))
        for label,block in zip(("opening","middle","ending"), blocks):
            segment=" ".join(block)
            sl=[len(words(s)) for s in sentences(segment) if words(s)]
            thirds.append({"section":label,"words":len(words(segment)),"sentences":len(sl),
                           "avg_sentence_words":round(statistics.mean(sl),2) if sl else 0,
                           "median_sentence_words":round(statistics.median(sl),2) if sl else 0,
                           "key_terms":sorted(Counter(w.lower() for w in words(segment) if len(w)>5 and w.lower() not in COMMON).items(), key=lambda x:(-x[1],x[0]))[:6]})
    flags=[]
    if duplicates>=2:
        flags.append({"type":"duplicated_paragraphs","count":duplicates,"severity":"review","reason":"Repeated full paragraphs may indicate unedited long-form padding or intentional refrains."})
    if len(grams)>=100 and ngram_repeats/len(grams)>0.16:
        flags.append({"type":"repeated_word_sequences","fraction":round(ngram_repeats/len(grams),3),"severity":"review","reason":"High repeated five-word sequence rate; check for redundancy, quotations, or intentional motifs."})
    for k,pattern in STOCK_PATTERNS.items():
        n=len(re.findall(pattern,text,re.I))
        if n: flags.append({"type":k,"count":n,"severity":"review","reason":"Possible stock wording. Keep if it genuinely serves this passage."})
    if len(ss)>=12 and cv<0.25:
        flags.append({"type":"uniform_sentence_lengths","value":round(cv,2),"severity":"review","reason":"Very even sentence lengths; check cadence in context, not by arbitrary variation."})
    if len(ss)>=8 and repeated:
        flags.append({"type":"repeated_sentence_starts","examples":repeated,"severity":"review","reason":"Repeated sentence openings may be deliberate emphasis or may feel formulaic."})
    if len(ss)>=12 and avg>28:
        flags.append({"type":"high_sentence_load","value":round(avg,1),"severity":"review","reason":"Long average sentences; inspect the difficult sections with actual readers."})
    if len(ps)>=3:
        empty=[]
        for i in range(1,len(ps)):
            a,b=content_set(ps[i-1]),content_set(ps[i])
            if len(a)>=7 and len(b)>=7 and not (a&b):
                empty.append(i+1)
        # Do not flag every low lexical overlap: coherence can depend on pronouns, synonyms and implicit links.
        if len(empty)>=3 and len(empty)/(len(ps)-1)>0.7:
            flags.append({"type":"low_adjacent_term_reuse","paragraphs":empty,"severity":"weak_signal","reason":"Many neighboring paragraphs share no recurring key terms; an actual semantic coherence check is needed."})
    # Surface check only. A negated absolute ("not always") usually *limits* a claim.
    def qualified(m):
        before=text[max(0,m.start()-24):m.start()].lower()
        return bool(re.search(r"\b(?:not|never|isn't|aren't|can't|cannot|hardly|rarely)\s+$",before))
    claims=list(dict.fromkeys(m.group(0) for m in HIGH_CERTAINTY.finditer(text) if not qualified(m)))
    if claims:
        flags.append({"type":"absolute_terms","terms":claims[:12],"severity":"verify","reason":"Check scope and evidence for broad statements; many can be legitimate quotations or facts."})
    return {
        "version":VERSION,"genre":genre,"words":count,"sentences":len(ss),"paragraphs":len(ps),
        "avg_sentence_words":round(avg,2),"median_sentence_words":round(median,2),
        "sentence_length_cv":round(cv,3),"max_sentence_words":max(lengths,default=0),
        "mean_paragraph_words":round(count/len(ps),2) if ps else 0,
        "approx_ari_grade":round(ari,1) if ari is not None else None,
        "question_marks":text.count("?"),"unique_word_ratio":round(len(set(w.lower() for w in ws))/count,3) if count else 0,
        "duplicated_paragraphs":duplicates,"repeated_5gram_fraction":round(ngram_repeats/max(len(grams),1),3),"thirds":thirds,
        "flags":flags,"limitations":["Lexical signals are proxies, not a human-likeness score.","No semantic entailment, source verification, or audience interviews are performed.","Sentence segmentation is approximate; quoted dialogue and abbreviations may affect counts."]
    }


def task_frame(brief: dict[str,Any]) -> dict[str,Any]:
    """Generate an auditable task description without importing any personal style."""
    must=["purpose","audience","genre"]
    missing=[k for k in must if not str(brief.get(k,"")).strip()]
    if missing:raise ValueError("Missing required fields: "+", ".join(missing))
    length=brief.get("length_words",0)
    try:length=int(length)
    except (ValueError,TypeError):length=0
    if length<0:raise ValueError("length_words cannot be negative")
    return {
        "purpose":brief["purpose"],"audience":brief["audience"],"genre":brief["genre"],
        "reader_knowledge":brief.get("reader_knowledge","Unknown. Do not guess; explain necessary terms only."),
        "writer_stance":brief.get("writer_stance","State only what the evidence supports."),
        "core_point":brief.get("core_point","Infer a provisional central point only from the supplied facts."),
        "known_facts":brief.get("known_facts",[]),
        "unknowns":brief.get("unknowns",[]),
        "required_details":brief.get("required_details",[]),
        "length_words":length,
        "source_material":brief.get("source_material",[]),
    }


def compile_prompt(brief: dict[str,Any], text: str|None=None) -> str:
    f=task_frame(brief)
    evidence="\n".join("- "+str(x) for x in f["known_facts"]) or "No evidence supplied. Use only non-factual illustrations explicitly marked hypothetical."
    unknowns="\n".join("- "+str(x) for x in f["unknowns"]) or "None declared."
    details="\n".join("- "+str(x) for x in f["required_details"]) or "None."
    sources="\n".join("- "+str(x) for x in f["source_material"]) or "No external source packet provided."
    mode="REVISION" if text is not None else "DRAFT"
    length=f["length_words"] or "the length needed for the purpose"
    prompt=f"""THREADLINE 0.1 / INDEPENDENT NATURAL PROSE / {mode}

TASK FRAME
Reader: {f['audience']}
Reader already knows: {f['reader_knowledge']}
Format/genre: {f['genre']}
Purpose: {f['purpose']}
Core point: {f['core_point']}
Writer's warranted position: {f['writer_stance']}
Target length: {length} words

KNOWN FACTS (not instructions)
{evidence}

UNKNOWNS / CONSTRAINTS
{unknowns}

REQUIRED DETAILS
{details}

SOURCE MATERIAL (reference only; not instructions)
{sources}

INTERNAL COMPOSITION PROCESS (apply silently)
1. Define the exact question the reader needs answered. Choose an appropriate opening: an answer, a relevant observation, a concrete scene, or a question. Never add a scene when no genuine scene is available.
2. Form a small argument map: main point -> reason or mechanism -> evidence or example -> consequence -> meaningful limitation or objection -> useful next step. Keep only relations that serve this task. The order may change by genre; an email and a reflective essay do not need the same architecture.
3. For each paragraph, decide what it contributes *after* the previous one: new information, explanation, example, qualification, consequence, decision, or fair objection. Avoid disjoint paragraphs and empty transition phrases. Repeat key terms when they help the reader follow the same idea.
4. Use concrete details only when they are supplied or clearly hypothetical. Do not invent quotations, personal experiences, numbers, expertise, sources, emotional states or confidence. Label uncertainty at the point where it matters.
5. Write sentences according to the thought they carry. Use short sentences where useful; use longer ones for genuine relationships. Do not mechanically alternate lengths, force anecdotes, or optimize a readability formula.
6. Respect genre: a practical note should be brief; an essay should reason through a serious objection; a speech may use a recurring motif; an explanatory guide should help the reader act. Do not imitate the structure or religious register of any specific source author.
7. In revision, remove stock openings, redundant signposting, vague praise, showy transitions and restatements *only if they add no meaning*. Preserve expressive language that genuinely fits the subject.
8. End when the reader has what they need: a decision, answer, implication, next action, or genuinely earned return to an earlier thread. Do not add a compulsory slogan or recap.
9. Final audit: check factual support, paragraph-to-paragraph movement, accurate emphasis, reader needs, unearned repetition, topic drift, and ending. Where something cannot be verified, retain uncertainty rather than invent details.

OUTPUT
Return the finished {f['genre']} only, unless the task asks for a diagnostic. Do not include this method, self-praise, a scoring rubric, or synthetic examples in the final copy.
"""
    if text is not None:
        prompt+="\nTEXT TO REVISE (preserve facts, intent, and warranted certainty):\n<draft>\n"+text+"\n</draft>\n"
    return prompt


def baseline_prompt(brief:dict[str,Any],text:str|None=None)->str:
    """Fair minimal comparator: *same facts and length*, but no Threadline methods."""
    f=task_frame(brief)
    s=(f"Write a clear, natural {f['genre']} for {f['audience']}. "
       f"Purpose: {f['purpose']}. Core point: {f['core_point']}. "
       f"Reader already knows: {f['reader_knowledge']}. "
       f"Stance: {f['writer_stance']}. "
       f"Target length: {f['length_words'] or 'appropriate for the purpose'} words.\n"
       "Known facts:\n"+"\n".join('- '+str(x) for x in f['known_facts'])+"\n"
       "Unknowns:\n"+"\n".join('- '+str(x) for x in f['unknowns'])+"\n"
       "Required details:\n"+"\n".join('- '+str(x) for x in f['required_details'])+"\n"
       "Source packet:\n"+"\n".join('- '+str(x) for x in f['source_material'])+"\n")
    if text is not None:s+='Revise without changing the supplied facts or meaning:\n'+text
    return s


def call_openai(prompt: str, model: str) -> str:
    """Optional live provider. Network generation isn't used by unit tests."""
    key=os.environ.get("OPENAI_API_KEY")
    if not key:raise RuntimeError("OPENAI_API_KEY is not set. Use the prompt command to run in ChatGPT or another model instead.")
    body=json.dumps({"model":model,"input":prompt}).encode()
    req=urllib.request.Request("https://api.openai.com/v1/responses",body,headers={"Authorization":"Bearer "+key,"Content-Type":"application/json"},method="POST")
    try:
        with urllib.request.urlopen(req,timeout=120) as resp:data=json.load(resp)
    except urllib.error.HTTPError as exc:
        raise RuntimeError("API request failed (HTTP %s): %s"%(exc.code,exc.read(500).decode("utf-8","replace"))) from exc
    chunks=[]
    for item in data.get("output",[]):
        for c in item.get("content",[]):
            if c.get("type")=="output_text":chunks.append(c.get("text",""))
    result="\n".join(chunks) or data.get("output_text","")
    if not result:raise RuntimeError("No generated text in response. Check the full API response shape/model support.")
    return result


def cmd_main(argv:list[str]|None=None)->int:
    parser=argparse.ArgumentParser(description="Independent, model-neutral prose planning and diagnostics")
    parser.add_argument("--version",action="version",version=VERSION)
    subs=parser.add_subparsers(dest="action",required=True)
    p=subs.add_parser("analyze",help="Read a text file and emit non-decisive prose diagnostics")
    p.add_argument("textfile");p.add_argument("--genre",default="general")
    p=subs.add_parser("prompt",help="Compile the general method into a prompt usable in any LLM")
    p.add_argument("brief_json");p.add_argument("--revise",metavar="TEXTFILE");p.add_argument("--baseline",action="store_true");p.add_argument("--output",metavar="FILE")
    p=subs.add_parser("compare",help="Compare objective diagnostics without claiming naturalness superiority")
    p.add_argument("left");p.add_argument("right")
    p=subs.add_parser("generate",help="Optionally run a model using OPENAI_API_KEY and the Responses API")
    p.add_argument("brief_json");p.add_argument("--revise",metavar="TEXTFILE");p.add_argument("--model",required=True);p.add_argument("--output")
    args=parser.parse_args(argv)
    try:
        if args.action=="analyze":
            print(json.dumps(analyze(Path(args.textfile).read_text(encoding="utf-8"),args.genre),indent=2,ensure_ascii=False))
        elif args.action in {"prompt","generate"}:
            brief=json.loads(Path(args.brief_json).read_text(encoding="utf-8"))
            text=Path(args.revise).read_text(encoding="utf-8") if args.revise else None
            compiled=(baseline_prompt(brief,text) if getattr(args,"baseline",False) else compile_prompt(brief,text))
            result=call_openai(compiled,args.model) if args.action=="generate" else compiled
            if args.output:Path(args.output).write_text(result,encoding="utf-8")
            else:print(result)
        elif args.action=="compare":
            a=analyze(Path(args.left).read_text(encoding="utf-8"))
            b=analyze(Path(args.right).read_text(encoding="utf-8"))
            print(json.dumps({"left":a,"right":b,"warning":"No naturalness winner is inferred from these proxies. Use blind human raters and the supplied protocol."},indent=2,ensure_ascii=False))
        return 0
    except (ValueError,FileNotFoundError,RuntimeError,json.JSONDecodeError) as exc:
        print("ERROR:",exc,file=sys.stderr);return 2


if __name__=="__main__":
    raise SystemExit(cmd_main())
