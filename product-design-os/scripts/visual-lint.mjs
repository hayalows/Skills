// Heuristic visual candidates only. No DOM, cascade or design judgment. Never treat absence of warnings as a pass.
export function visualLint(source,file="input.html"){
  const findings=[];
  const clean=String(source).replace(/<!--[\s\S]*?-->|\/\*[\s\S]*?\*\//g,m=>m.replace(/[^\n]/g," "));
  const add=(rule,index,message)=>findings.push({file,line:clean.slice(0,index).split("\n").length,severity:"warn",rule,message});
  const css=/\.css$/i.test(file)?clean:[...clean.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/gi)].map(m=>m[1]).join("\n");
  for(const m of clean.matchAll(/<(?:div|span|p|small)\b[^>]*\b(?:class|className)\s*=\s*["'][^"']*(?:\beyebrow\b|\bkicker\b|\boverline\b|\bpreheading\b)[^"']*["'][^>]*>[\s\S]{0,500}?<\/(?:div|span|p|small)>\s*<h[1-3]\b/gi))add("visual-eyebrow",m.index,"VI02: possible decorative pre-heading. Confirm whether it conveys required context.");
  for(const m of clean.matchAll(/<h[1-3]\b[^>]*>\s*(?:<span\b[^>]*>\s*)?(?:0[1-9]|[1-9]\d)\s*(?:[.:/]|<\/span>)/gi))add("visual-numbering",m.index,"VI07: numbered heading candidate; keep real sequence or rank.");
  for(const m of clean.matchAll(/<(?:span|small|div|p)\b[^>]*>\s*((?:[A-Z][A-Z0-9]{1,}\s+){2,}[A-Z][A-Z0-9]{1,})\s*<\/(?:span|small|div|p)>/g))add("visual-uppercase",m.index,"VI07: uppercase micro-label candidate; keep necessary acronyms and source text.");
  for(const m of clean.matchAll(/<(?:span|div)\b[^>]*\b(?:class|className)\s*=\s*["'][^"']*\b(?:live-dot|status-dot|pulse-dot|scroll-cue)\b[^"']*["'][^>]*>/gi))add("visual-telemetry",m.index,"VI03: status/scroll decoration candidate; verify status is real and useful.");
  for(const m of clean.matchAll(/\btransition-all\b|\btransition\s*:\s*all(?:\s|;|,|})/gi))add("visual-transition-all",m.index,"VI10: name the animated properties explicitly.");
  for(const m of clean.matchAll(/\bfont-size\s*:\s*(\d+(?:\.\d+)?)px\b/gi))if(Number(m[1])<13)add("visual-small-text",m.index,"VI05: sub-13px declaration; verify actual visible first-screen text, not hidden or unused styles.");
  if(css){
    const sizes=new Set([...css.matchAll(/\bfont-size\s*:\s*(\d+(?:\.\d+)?)px\b/gi)].map(m=>Number(m[1])));
    if(sizes.size>4)add("visual-type-sprawl",0,"VI05: "+sizes.size+" literal CSS size candidates; measure computed visible body roles and exemptions.");
  }
  return findings.sort((a,b)=>a.line-b.line);
}
