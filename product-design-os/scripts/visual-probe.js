/* Read-only browser probe. Run as a DevTools snippet or evaluate via Playwright.
   Returns candidates for the current viewport/state, not accessibility or design compliance.
   Scroll to relevant states and rerun. No network, edits, or dependencies. */
(() => {
  const vw = document.documentElement.clientWidth, vh = window.innerHeight;
  const sizeCounts = {}, bodySizes = {}, fonts = {}, tiny = [], overflow = [], headings = [];
  const describe = e => ({tag:e.tagName.toLowerCase(), id:e.id || null,
    text:(e.innerText || e.getAttribute("aria-label") || "").trim().slice(0,100)});
  const visible = e => {
    const s = getComputedStyle(e);
    if (!e.getClientRects().length || s.display === "none" || s.visibility !== "visible" || Number(s.opacity) === 0 || e.closest("[hidden],[aria-hidden=true]")) return false;
    const r=e.getBoundingClientRect();
    if (r.width <= 1 || r.height <= 1) return false;
    for(let p=e.parentElement;p;p=p.parentElement){const c=getComputedStyle(p);if(c.display==="none"||c.visibility!=="visible"||Number(c.opacity)===0)return false;}
    return true;
  };
  const rendered = [...document.querySelectorAll("body *")].filter(visible);
  for(const e of rendered){
    const r=e.getBoundingClientRect(), s=getComputedStyle(e), inView=r.bottom>0&&r.top<vh&&r.right>0&&r.left<vw;
    if((r.right>vw+1||r.left< -1)&&overflow.length<100)overflow.push({...describe(e),left:Math.round(r.left),right:Math.round(r.right),inView});
    if(/^H[1-6]$/.test(e.tagName)&&inView)headings.push(describe(e));
    const ownText=[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()) || /^(INPUT|TEXTAREA|SELECT)$/.test(e.tagName);
    if(!ownText||!inView)continue;
    const px=Math.round(parseFloat(s.fontSize)*100)/100;
    sizeCounts[px]=(sizeCounts[px]||0)+1;
    const family=s.fontFamily;fonts[family]=(fonts[family]||0)+1;
    if(!e.closest("h1") && !e.closest("[data-visual-role=wordmark],[data-visual-role=display-value]"))bodySizes[px]=(bodySizes[px]||0)+1;
    if(px<13&&tiny.length<100)tiny.push({...describe(e),px});
  }
  const nav=[...document.querySelectorAll("nav")].filter(visible).map(e=>({...describe(e),clientWidth:e.clientWidth,scrollWidth:e.scrollWidth,overflow:e.scrollWidth>e.clientWidth+1}));
  const result={viewport:{width:vw,height:vh,scrollY:window.scrollY},pageOverflow:document.documentElement.scrollWidth>vw+1,bodySizes,sizeCounts,fontFamilyStacks:fonts,tinyVisibleCandidates:tiny,elementOverflowCandidates:overflow,nav,headings,notes:"Counts are candidate computed sizes in this viewport, including labels and controls. Review actual visibility/clipping, font fallback stacks, hidden text, focal values and wordmarks manually. Mark only intentional display roles; do not use attributes to evade the gate. No contrast, overlap, role, interaction or subjective quality verdict."};
  console.log(JSON.stringify(result,null,2));return result;
})()
