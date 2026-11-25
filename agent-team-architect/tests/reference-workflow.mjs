import { runTests } from "../scripts/reference-workflow.mjs";
const r=await runTests();
for(const t of r.results) console.log((t.pass?"PASS ":"FAIL ")+t.name);
if(r.results.some(t=>!t.pass)) process.exitCode=1;
console.log(JSON.stringify(r,null,2));
