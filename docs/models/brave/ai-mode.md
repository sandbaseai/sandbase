# Brave AI Mode API: pricing, parameters and code examples

`brave/ai-mode` · data API · Brave · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get the AI-generated answer Brave Search shows for a query, with answer text, cited sources and location and language options.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/ai-mode", "q": "How does a heat pump work?"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/ai-mode', {'q': 'How does a heat pump work?'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/ai-mode", {
  "q": "How does a heat pump work?"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/ai-mode", sandbase.Params{
	"q": "How does a heat pump work?",
})
```

Same call via the path form: `POST /v1/api/brave/ai-mode` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search.  |
| `lat` | string |  | Parameter defines a GPS latitude for the search origin. Parameter is required when using `lon` parameter. Parameter can't be used with `location` parameter.  |
| `lon` | string |  | Parameter defines a GPS longitude for the search origin. Parameter is required when using `lat` parameter. Parameter can't be used with `location` parameter.  |
| `country` | string |  | Parameter defines the country to use for the Brave AI search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Brave countries page for a full…  |
| `language` | string |  | Parameter defines the language to use for the Brave AI search. It's a two-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French). Head to the Brave languages page for a full list of…  |
| `location` | string |  | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. It is…  |
| `safeSearch` | string |  | Parameter defines the level of filtering for adult content. It can be set to: `off` - Off `moderate` - Moderate `strict` - Strict  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `units_of_measurement` | string |  | Parameter defines the units of measurement to use. It can be set to: `metric` - Metric `us` - Imperial (US)  |
| `subsequent_request_token` | string |  | Parameter defines the token used to continue a Brave AI Mode conversation. Pass this token to send a follow-up question that includes the prior exchange as context (multi-turn). The token is returned by the API from…  |

## Details

Get the AI-generated answer Brave Search shows for a query, with answer text, cited sources and location and language options.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/ai-mode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "How does a heat pump work?"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. |
| `location` | string | No | Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. It is recommended to specif |
| `lat` | string | No | Parameter defines a GPS latitude for the search origin. Parameter is required when using `lon` parameter. Parameter can't be used with `location` parameter. |
| `lon` | string | No | Parameter defines a GPS longitude for the search origin. Parameter is required when using `lat` parameter. Parameter can't be used with `location` parameter. |
| `country` | string | No | Parameter defines the country to use for the Brave AI search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). Head to the Brave countries page for a full list of supported Bra |
| `language` | string | No | Parameter defines the language to use for the Brave AI search. It's a two-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French). Head to the Brave languages page for a full list of supported Brave AI Mode lang |
| `safeSearch` | string | No | Parameter defines the level of filtering for adult content. It can be set to: `off` - Off `moderate` - Moderate `strict` - Strict |
| `units_of_measurement` | string | No | Parameter defines the units of measurement to use. It can be set to: `metric` - Metric `us` - Imperial (US) |
| `subsequent_request_token` | string | No | Parameter defines the token used to continue a Brave AI Mode conversation. Pass this token to send a follow-up question that includes the prior exchange as context (multi-turn). The token is returned by the API from your previous request us |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/brave/ai-mode.json`](../../../catalog/models/brave/ai-mode.json) · Store page: https://www.sandbase.ai/model/brave/ai-mode
