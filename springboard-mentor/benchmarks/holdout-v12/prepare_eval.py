"""Prepare independent, gold-hidden fictional test environments. Does not run a model."""
from pathlib import Path
import json, shutil
repo=Path(__file__).resolve().parents[3]
skill=repo/"springboard-mentor"
cases=json.loads((skill/"benchmarks/holdout-v12/cases.json").read_text(encoding="utf-8"))["cases"]
root=repo.parent/"independent-eval"
root.mkdir(exist_ok=True)
keys=["id","route","student_text","mentor_note","source_status"]
item={"type":"object","properties":{k:{"type":"string"} for k in keys},"required":keys,"additionalProperties":False}
schema={"type":"object","properties":{"responses":{"type":"array","items":item}},"required":["responses"],"additionalProperties":False}
(root/"schema.json").write_text(json.dumps(schema,indent=2),encoding="utf-8")
for variant in ("v11","v12"):
    base=skill/"versions/v1.1.0" if variant=="v11" else skill
    for batch in range(3):
        dst=root/variant/str(batch+1)
        (dst/"mentor-skill/references").mkdir(parents=True,exist_ok=True)
        (dst/"papa-kojo-writing-style/references").mkdir(parents=True,exist_ok=True)
        shutil.copy2(base/"SKILL.md",dst/"mentor-skill/SKILL.md")
        for src in (base/"references").glob("*.md"):
            shutil.copy2(src,dst/"mentor-skill/references"/src.name)
        voice=repo/"papa-kojo-writing-style"
        shutil.copy2(voice/"SKILL.md",dst/"papa-kojo-writing-style/SKILL.md")
        for f in ("register-dial.md","voice-bank.md","voice-profile.md"):
            shutil.copy2(voice/"references"/f,dst/"papa-kojo-writing-style/references"/f)
        group=cases[batch*20:(batch+1)*20]
        safe=[{"id":x["id"],"scenario":x["scenario"],"group":x["group"]} for x in group]
        (dst/"cases_to_answer.json").write_text(json.dumps(safe,indent=2),encoding="utf-8")
        prompt=("You are tested on 20 fictional mentoring situations. Read mentor-skill/SKILL.md, its relevant references and the included Papa Kojo writing skill. "
          "Apply ONLY this variant, not any later guidance. Do not read outside this folder, seek a gold answer key, contact anyone or modify records. "
          "For EACH entry in cases_to_answer.json, choose the best route and proposed reply. Return JSON object with responses array. "
          "Each response: id, route, student_text, mentor_note, source_status. Preserve case order and case ID. "
          "student_text is one or two short WhatsApp/email sentences, or empty when no reply or forbidden disclosure. "
          "mentor_note should briefly justify the choice and state any live verification gap. "
          "source_status must be verified, not_checked, not_needed, or unavailable. Say verified ONLY if an official primary source was actually opened in THIS run. "
          "Keep replies natural and avoid repeated questions or fictitious promises. This is a simulation; no protected student records. "
          "Don't invent current policies or claim a message was sent. Output JSON only, not Markdown.\n")
        (dst/"prompt.txt").write_text(prompt,encoding="utf-8")
print(f"Prepared {len(cases)} cases in six independent batches at {root}")
