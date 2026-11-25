// Pure function regression fixtures. Run with Node.
import assert from "node:assert/strict";
import { visualLint } from "../scripts/visual-lint.mjs";
const fixtures=[
  [
    "eyebrow",
    "<p class=\"eyebrow\">Our mission</p><h1>Money</h1>",
    "a.html",
    "visual-eyebrow",
    true
  ],
  [
    "kicker",
    "<span className=\"feature-kicker\">Introducing</span>\n<h2>Tools</h2>",
    "a.tsx",
    "visual-eyebrow",
    true
  ],
  [
    "ordinary date",
    "<time>25 Nov</time><h2>Market</h2>",
    "a.html",
    "visual-eyebrow",
    false
  ],
  [
    "heading number",
    "<h2>01. Features</h2>",
    "a.html",
    "visual-numbering",
    true
  ],
  [
    "actual heading",
    "<h2>2027 budget</h2>",
    "a.html",
    "visual-numbering",
    false
  ],
  [
    "caps",
    "<span>THE BIG NUMBER</span>",
    "a.html",
    "visual-uppercase",
    true
  ],
  [
    "acronym",
    "<span>PAYE</span>",
    "a.html",
    "visual-uppercase",
    false
  ],
  [
    "live dot",
    "<span class=\"live-dot\"></span>",
    "a.html",
    "visual-telemetry",
    true
  ],
  [
    "semantic status candidate",
    "<span class=\"status-dot\"></span><span>Pending</span>",
    "a.html",
    "visual-telemetry",
    true
  ],
  [
    "status plain",
    "<span role=\"status\">Source unavailable</span>",
    "a.html",
    "visual-telemetry",
    false
  ],
  [
    "css all",
    ".a{transition: all 200ms;}",
    "a.css",
    "visual-transition-all",
    true
  ],
  [
    "tailwind all",
    "<div className=\"transition-all\">x</div>",
    "a.tsx",
    "visual-transition-all",
    true
  ],
  [
    "explicit",
    ".a{transition: opacity 200ms, transform 180ms;}",
    "a.css",
    "visual-transition-all",
    false
  ],
  [
    "small",
    ".a{font-size:12px}",
    "a.css",
    "visual-small-text",
    true
  ],
  [
    "13 boundary",
    ".a{font-size:13px}",
    "a.css",
    "visual-small-text",
    false
  ],
  [
    "many sizes",
    ".a{font-size:13px}.b{font-size:14px}.c{font-size:15px}.d{font-size:16px}.e{font-size:18px}",
    "a.css",
    "visual-type-sprawl",
    true
  ],
  [
    "four sizes",
    ".a{font-size:13px}.b{font-size:14px}.c{font-size:16px}.d{font-size:24px}",
    "a.css",
    "visual-type-sprawl",
    false
  ],
  [
    "ignored comment",
    "/* transition: all 1s; font-size:10px */ .a{font-size:14px}",
    "a.css",
    "visual-small-text",
    false
  ],
  [
    "comment eyebrow",
    "<!-- <p class=\"eyebrow\">X</p><h1>Y</h1> -->",
    "a.html",
    "visual-eyebrow",
    false
  ],
  [
    "line number",
    "\n\n.a{font-size:12px}",
    "a.css",
    "visual-small-text",
    true
  ],
  [
    "real tabs",
    "<button role=\"tab\" aria-selected=\"true\">Currency</button>",
    "a.html",
    "visual-eyebrow",
    false
  ],
  [
    "required text",
    "<label>Amount</label><p>Fees may apply.</p>",
    "a.html",
    "visual-uppercase",
    false
  ]
];
for(const [name,source,file,rule,expected] of fixtures){assert.equal(visualLint(source,file).some(x=>x.rule===rule),expected,name);}
assert.equal(visualLint("\n\n.a{font-size:12px}","a.css")[0].line,3);
console.log("PASS: "+fixtures.length+" visual lint candidate fixtures and line location");
