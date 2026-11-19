#!/usr/bin/env node
/**
 * Public KB research lead generator, not a complete KB mirror or source verifier.
 * No network calls, credentials, student data, scraping or claims of live access.
 */
const args = process.argv.slice(2);
const help = () => {
  console.log("Usage: node springboard-mentor/scripts/kb-gateway.mjs --query \"registration hold\" [--program PC|CD] [--json]");
  console.log("       node springboard-mentor/scripts/kb-gateway.mjs --article KA-03332 [--json]");
};
function flag(name) {
  const n=args.indexOf(name);
  return n === -1 ? null : (args[n+1] && !args[n+1].startsWith("--") ? args[n+1] : "");
}
function safeQuery(input) {
  if (typeof input !== "string" || !input.trim()) throw Error("Give a generic topic without student information.");
  const s = input.trim().replace(/\s+/g, " ");
  if (s.length>140) throw Error("Search query is too long. Use 2-6 generic keywords.");
  if (/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i.test(s)) throw Error("Do not search with student emails or contact details.");
  if (/(?:\+?\d[\s-]?){9,}/.test(s)) throw Error("Do not search with student IDs or phone numbers.");
  if (/https?:\/\/|\b(student\s*id|date\s*of\s*birth|account\s*number)\b/i.test(s)) throw Error("Use a generic topic, not protected details or links.");
  return s;
}
function officialArticle(id) {
  if (!/^KA-\d{5}$/i.test(id)) throw Error("Article ID must look like KA-03332.");
  return "https://help.byupathway.edu/en-US/knowledgebase/article/?kb="+encodeURIComponent(id.toUpperCase())+"&lang=en";
}
function buildSearch(query, program=null) {
  const q=safeQuery(query);
  if (program && !["PC","CD","EC"].includes(program)) throw Error("--program must be PC, CD or EC.");
  const extras=program==="PC"?" PathwayConnect":program==="CD"?" Certificate Degree":program==="EC"?" EnglishConnect":"";
  const site='site:help.byupathway.edu/en-US/knowledgebase/article/ "'+q+'"'+extras;
  const tutorials='site:help.byupathway.edu/en-US/tutorials/ "'+q+'"'+extras;
  return {
    status:"SEARCH_LEADS_ONLY_NOT_VERIFIED",
    officialHelpCenter:"https://help.byupathway.edu/en-US/",
    officialKnowledgeBase:"https://help.byupathway.edu/en-US/knowledgebase/",
    helpCenterSearchInstruction:"Enter short topic words in the How can we help you? field; also browse Knowledge Base and Tutorials.",
    webSearchQueries:[site,tutorials,'site:help.byupathway.edu "'+q+'"'],
    webSearchUrls:[
      "https://www.google.com/search?q="+encodeURIComponent(site),
      "https://www.google.com/search?q="+encodeURIComponent(tutorials)
    ],
    nextStep:"Open an official article, read the full matching section, verify programme/catalogue/block and date, then cite its exact KA ID and URL. Search results alone are not policy."
  };
}
try {
  if (args.includes("--help") || args.length===0) {help(); process.exit(0);}
  const q=flag("--query"), a=flag("--article"), program=flag("--program");
  if ((q===null)===(a===null)) throw Error("Supply exactly one of --query or --article.");
  const result = a!==null
    ? {status:"ARTICLE_LEAD_NOT_VERIFIED",url:officialArticle(a),nextStep:"Open and read the live official page before making any policy claim."}
    : buildSearch(q,program);
  if (args.includes("--json")) console.log(JSON.stringify(result,null,2));
  else {
    console.log(result.status);
    for (const [key,value] of Object.entries(result)) if (key!=="status") {
      console.log(key+":");
      if (Array.isArray(value)) value.forEach(v=>console.log("  "+v));
      else console.log("  "+value);
    }
  }
} catch (e) {
  console.error("KB gateway: "+e.message);
  process.exit(2);
}
