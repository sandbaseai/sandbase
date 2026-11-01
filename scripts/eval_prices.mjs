// Evaluate SandBase price formulas for a list of parameter combinations.
// stdin:  [{ "name": str, "formula": str, "cases": [{ "params": {}, "usage": {} }] }]
// stdout: [{ "name": str, "results": [number|null] }]
// Formulas run in an isolated vm context that only exposes Math and the
// helper functions the SandBase metering engine provides to formulas.
import vm from "node:vm";

const input = JSON.parse(await new Promise((resolve) => {
  let buf = "";
  process.stdin.on("data", (c) => (buf += c));
  process.stdin.on("end", () => resolve(buf));
}));

const helpers = {
  Math,
  len: (v) => (v == null ? 0 : Array.isArray(v) || typeof v === "string" ? v.length : Object.keys(v).length),
  int: (v) => Math.trunc(Number(v)),
  float: (v) => Number(v),
  sum: (v) => (Array.isArray(v) ? v.reduce((a, b) => a + Number(b || 0), 0) : Number(v || 0)),
  // media_duration needs the real media file; unknown at catalog build time.
  media_duration: () => { throw new Error("media_duration unavailable"); },
};

const out = [];
for (const item of input) {
  const results = [];
  let script;
  try {
    script = new vm.Script(`(${item.formula})`);
  } catch {
    out.push({ name: item.name, results: item.cases.map(() => null), error: "syntax" });
    continue;
  }
  for (const c of item.cases) {
    try {
      const ctx = vm.createContext({ ...helpers, params: c.params ?? {}, usage: c.usage ?? {}, output: {}, outputs: [] });
      const v = script.runInContext(ctx, { timeout: 50 });
      results.push(typeof v === "number" && Number.isFinite(v) ? Math.round(v * 1e6) / 1e6 : null);
    } catch {
      results.push(null);
    }
  }
  out.push({ name: item.name, results });
}
process.stdout.write(JSON.stringify(out));
