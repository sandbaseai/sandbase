# Vaquill Divisions API: pricing, parameters and code examples

`vaquill/divisions` · data API · Vaquill · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** async

Walk a US legal code level by level: titles, chapters, parts, then sections.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "vaquill/divisions", "corpusType": "USC"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('vaquill/divisions', {'corpusType': 'USC'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("vaquill/divisions", {
  "corpusType": "USC"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "vaquill/divisions", sandbase.Params{
	"corpusType": "USC",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/vaquill/divisions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` | string |  | State code identifier to drill into, e.g. 'tx_pe' — the identifier returned by browsing corpusType=STATE with a state.  |
| `part` | string |  | Part identifier to drill into (CFR).  |
| `state` | string |  | Lowercase two-letter jurisdiction code, e.g. 'tx'; required for STATE and REGULATION. one of: `al`, `ak`, `az`, `ar`, `ca`, `co`, `ct`, `de`, `dc`, `fl`, `ga`, `hi` … |
| `cursor` | string |  | Resume token from a previous response's nextCursor, at the level that lists sections.  |
| `chapter` | string |  | Chapter identifier to drill into (USC and state codes).  |
| `actStatus` | string |  | List only sections carrying this status, e.g. 'repealed'. one of: `abolished`, `deleted`, `expired`, `in_force`, `inactive`, `non_precedential`, `not_funded`, `not_yet_effective`, `omitted`, `proposed`, `recodified`, `recompiled` … |
| `corpusType` | string | yes | Corpus to browse. Other corpora are flatter — search them instead. one of: `USC`, `CFR`, `STATE`, `REGULATION` |
| `titleNumber` | integer |  | USC or CFR title number to drill into. range -9007199254740991–9007199254740991 |
| `excludeRepealed` | boolean |  | Leave out sections whose status is affirmatively dead. A section with no recorded status is kept.  |

## Details

Walk a US legal code level by level: titles, chapters, parts, then sections.

---
Machine-readable: [`catalog/models/vaquill/divisions.json`](../../../catalog/models/vaquill/divisions.json) · Store page: https://www.sandbase.ai/model/vaquill/divisions
