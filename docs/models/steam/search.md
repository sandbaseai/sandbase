# Steam Search API: pricing, parameters and code examples

`steam/search` · data API · Steam · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Search the Steam store by keyword and get games and apps with app ID, title, price, discount, release date and review summary.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "steam/search", "q": "portal"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('steam/search', {'q': 'portal'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("steam/search", {
  "q": "portal"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "steam/search", sandbase.Params{
	"q": "portal",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/steam/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Game or software title to search for.  |
| `country` | string |  | Two-letter country code for prices and availability.  |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |
| `language` | string |  | Steam language name, such as english, german, or french.  |

## Details

Search the Steam store by keyword and get games and apps with app ID, title, price, discount, release date and review summary.

---
Machine-readable: [`catalog/models/steam/search.json`](../../../catalog/models/steam/search.json) · Store page: https://www.sandbase.ai/model/steam/search
