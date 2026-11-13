# Steam App API: pricing, parameters and code examples

`steam/app` · data API · Steam · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get a Steam game or app by app ID with title, price, discount, release date, developer, publisher, genres, review summary and platform support, by country and language.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "steam/app", "app_id": 730}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('steam/app', {'app_id': 730})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("steam/app", {
  "app_id": 730
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "steam/app", sandbase.Params{
	"app_id": 730,
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/steam/app` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `app_id` | integer | yes | Numeric Steam app ID. range 1–9007199254740991 |
| `country` | string |  | Two-letter country code for prices and availability.  |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |
| `language` | string |  | Steam language name, such as english, german, or french.  |

## Details

Get a Steam game or app by app ID with title, price, discount, release date, developer, publisher, genres, review summary and platform support, by country and language.

---
Machine-readable: [`catalog/models/steam/app.json`](../../../catalog/models/steam/app.json) · Store page: https://www.sandbase.ai/model/steam/app
