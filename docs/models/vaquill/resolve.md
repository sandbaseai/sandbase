# Vaquill Resolve API: pricing, parameters and code examples

`vaquill/resolve` · data API · Vaquill · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02 per call · **Modes:** async

Resolve up to 50 Bluebook citation strings to the exact US law sections they name.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "vaquill/resolve", "citations": ["42 U.S.C. 1983"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('vaquill/resolve', {'citations': ['42 U.S.C. 1983']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("vaquill/resolve", {
  "citations": [
    "42 U.S.C. 1983"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "vaquill/resolve", sandbase.Params{
	"citations": []any{"42 U.S.C. 1983"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/vaquill/resolve` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `state` | string |  | Lowercase two-letter jurisdiction to resolve the whole batch within, for forms several states share ('8 CCR 1206-2' is Colorado, '22 CCR 76227' California). Omit for a batch that spans jurisdictions. one of: `al`, `ak`, `az`, `ar`, `ca`, `co`, `ct`, `de`, `dc`, `fl`, `ga`, `hi` … |
| `citations` | array | yes | Bluebook citations to resolve, e.g. ['42 U.S.C. 1983', '16 C.F.R. 444.1', 'Cal. Civ. Code 1950.5']. Duplicates are collapsed; at most 50 distinct citations per call. A pinpoint such as '42 U.S.C. 1983(b)(2)' resolves…  |
| `corpusType` | string |  | Corpus to resolve the whole batch within: STATE (statutory text), REGULATION (administrative codes), STATE_RULES (court rules), CONSTITUTION / STATE_CONSTITUTION. one of: `CONSTITUTION`, `REGULATION`, `STATE`, `STATE_CONSTITUTION`, `STATE_RULES` |

## Details

Resolve up to 50 Bluebook citation strings to the exact US law sections they name.

### Pricing

- Inspect reference unit price: $0.02 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/vaquill/resolve.json`](../../../catalog/models/vaquill/resolve.json) · Store page: https://www.sandbase.ai/model/vaquill/resolve
