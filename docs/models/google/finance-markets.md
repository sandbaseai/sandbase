# Google Finance Markets API: pricing, parameters and code examples

`google/finance-markets` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

List Google Finance market movers and overviews such as indexes, most active, gainers, losers, crypto and currencies, with price and change for each instrument.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/finance-markets", "trend": "indexes"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/finance-markets', {'trend': 'indexes'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/finance-markets", {
  "trend": "indexes"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/finance-markets", sandbase.Params{
	"trend": "indexes",
})
```

Same call via the path form: `POST /v1/api/google/finance-markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Parameter defines the country to use for the Google Finance Markets search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Google countries…  |
| `hl` | string |  | Parameter defines the language to use for the Google Finance Markets search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter…  |
| `trend` | string | yes | Parameter is used for retrieving different market trends. Due to a recent Google Finance update, this parameter now only accepts `indexes` as a valid value.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

List Google Finance market movers and overviews such as indexes, most active, gainers, losers, crypto and currencies, with price and change for each instrument.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/finance-markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"trend": "indexes"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `trend` | string | Yes | Parameter is used for retrieving different market trends. Due to a recent Google Finance update, this parameter now only accepts `indexes` as a valid value. |
| `hl` | string | No | Parameter defines the language to use for the Google Finance Markets search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region |
| `gl` | string | No | Parameter defines the country to use for the Google Finance Markets search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Google countries page for a full list o |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/finance-markets.json`](../../../catalog/models/google/finance-markets.json) · Store page: https://www.sandbase.ai/model/google/finance-markets
