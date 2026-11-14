# Vaquill Count API: pricing, parameters and code examples

`vaquill/count` · data API · Vaquill · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** async

Count the law sections in a jurisdiction, corpus, code, title, chapter, or part.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "vaquill/count"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('vaquill/count', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("vaquill/count", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "vaquill/count", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/vaquill/count` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` |  |  | State statutory code identifier, e.g. 'tx_pe' (Texas Penal Code) — the identifier /us/statutes/divisions returns for corpusType=STATE. The only way to scope below a whole jurisdiction.  |
| `part` |  |  | Part within a title or code, e.g. '240' (17 C.F.R. Part 240). Must be paired with titleNumber or code, or upstream answers 422.  |
| `state` |  |  | Lowercase two-letter jurisdiction code (50 states, 'dc', 'pr'), or 'federal' for USC / CFR / Constitution / federal rules. A list covers several at once.  |
| `chapter` |  |  | Chapter within a title or code, e.g. '21'. Must be paired with titleNumber or code, or upstream answers 422.  |
| `actStatus` |  |  | Keep only sections carrying these publisher statuses, e.g. 'repealed'. Contradicts excludeRepealed when it names a dead status (upstream 422).  |
| `corpusType` |  |  | Restrict to one corpus or a list, e.g. 'CFR' or ['USC','CFR']. Omit to cover every corpus. /us/statutes/coverage lists what each jurisdiction holds.  |
| `titleNumber` | integer |  | USC or CFR title number, e.g. 17 (SEC) or 42 (civil rights). State titles are not numeric — use code. range -9007199254740991–9007199254740991 |
| `excludeRepealed` | boolean |  | Drop sections whose status is affirmatively dead (repealed, renumbered, superseded, ...). A section with no recorded status is kept; read goodLawStatus on each result.  |

## Details

Count the law sections in a jurisdiction, corpus, code, title, chapter, or part.

---
Machine-readable: [`catalog/models/vaquill/count.json`](../../../catalog/models/vaquill/count.json) · Store page: https://www.sandbase.ai/model/vaquill/count
