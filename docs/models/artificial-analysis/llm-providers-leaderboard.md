# Artificial Analysis Llm Providers Leaderboard API: pricing, parameters and code examples

`artificial-analysis/llm-providers-leaderboard` · data API · Artificial Analysis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Get the main LLM API Providers Leaderboard data, including all model endpoints and their performance metrics (speed, latency, price, etc.). Returns a large dataset of provider-model combinations with pricing,.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "artificial-analysis/llm-providers-leaderboard"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('artificial-analysis/llm-providers-leaderboard', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("artificial-analysis/llm-providers-leaderboard", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "artificial-analysis/llm-providers-leaderboard", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/artificial-analysis/llm-providers-leaderboard` with the body above minus `model`.

## Details

This API returns a list of LLM endpoints. Each endpoint is one model served by one host, with speed, latency, feature and benchmark score data. It takes no input.

### Use cases

- Find the host with the highest median output speed or the lowest time to first token for a given model.
- Filter for endpoints that support function calling, JSON mode or a minimum context window.
- Build a dashboard that tracks open weights models next to their benchmark scores.
- Compare benchmark scores of models from different creators, such as `gpqa-diamond` and `tau2-bench`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/artificial-analysis/llm-providers-leaderboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "endpoints": [
      {
        "features": {
          "contextWindowTokens": 256000,
          "functionCalling": true,
          "jsonMode": true,
          "openaiCompatible": true
        },
        "footnotes": null,
        "host": {
          "color": "#ff7018",
          "functionCallingUrl": "https://www.alibabacloud.com/help/en/model-studio/qwen-function-calling?spm=a2c6…",
          "jsonModeUrl": "https://www.alibabacloud.com/help/en/model-studio/json-mode?spm=a2c63.p38356.hel…",
          "logo": "alibaba.svg",
          "name": "Alibaba Cloud",
          "slug": "alibaba_cloud"
        },
        "hostApiId": "qwen3.5-omni-plus",
        "id": "5b20b073-b487-44c5-84bd-0444d3f5979e",
        "label": "Qwen3.5 Omni Plus",
        "model": {
          "creator": {
            "logo": "alibaba.svg",
            "name": "Alibaba"
          },
          "deprecated": false,
          "intelligenceIndex": null,
          "isOpenWeights": false,
          "omniscience": null,
          "reasoningModel": false,
          "scores": {
            "artificial-analysis-long-context-reasoning": 0.636666666666667,
            "critpt": 0.00563265306122449,
            "gpqa-diamond": 0.826262626262626,
            "humanitys-last-exam": 0.148748841519926,
            "ifbench": 0.51156462585034,
            "mmmu-pro": 0.705202312138728,
            "tau2-bench": 0.883040935672515,
            "terminalbench-hard": 0.212121212121212
          },
          "sizeClass": "large"
        },
        "performance": {
          "medianEndToEndResponseTimeSeconds": 5.895152423598014,
          "medianOutputTokensPerSecond": 131.164075532196,
          "medianReasoningTimeSeconds": null,
          "medianTimeToFirstAnswerTokenSeconds": 2.08313302749997,
          "medianTimeToFirstTokenSeconds": 2.08313302749997,
          "percentile05OutputTokensPerSecond": 61.938558708569,
          "percentile05TimeToFirstTokenSeconds": 1.88292898965,
          "percentile95OutputTokensPerSecond": 157.94364645409
        },
        "pricing": {
          "cacheHitPrice": null,
          "cacheWritePrice": null,
          "price1mInputTokens": 0.4,
          "price1mOutputTokens": 4.8,
          "priceClass": "medium"
        }
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.endpoints[].label` | Display name of the model endpoint. It can include variant notes such as `(non-reasoning)` or `(FP4)`. |
| `data.endpoints[].host.name / data.endpoints[].host.slug` | Name and slug of the company that hosts this endpoint. |
| `data.endpoints[].hostApiId` | Model identifier used by the host in its own API. |
| `data.endpoints[].model.creator.name` | Organization that created the model. |
| `data.endpoints[].model.isOpenWeights / data.endpoints[].model.reasoningModel / data.endpoints[].model.deprecated` | Boolean flags for open weights release, reasoning model type and deprecated status. |
| `data.endpoints[].model.scores` | Benchmark scores keyed by benchmark name, such as `gpqa-diamond`, `ifbench` and `tau2-bench`. Some benchmarks are missing for some models. |
| `data.endpoints[].performance.medianOutputTokensPerSecond` | Median output speed in tokens per second. `percentile05OutputTokensPerSecond` and `percentile95OutputTokensPerSecond` show the low and high ends of the range. |
| `data.endpoints[].performance.medianTimeToFirstTokenSeconds / data.endpoints[].performance.medianEndToEndResponseTimeSeconds` | Median seconds until the first token arrives, and median seconds for the full response. |
| `data.endpoints[].features.contextWindowTokens` | Context window size in tokens. Sibling flags `functionCalling`, `jsonMode` and `openaiCompatible` show supported features. |

### Notes

- The request has no parameters. Send an empty JSON object `{}`.
- Each endpoint has a UUID in `data.endpoints[].id`. The same model can appear once per host.
- `intelligenceIndex` and `omniscience` are `null` for some models, so check for `null` before you sort on them.
- To look up models without host data, use [Artificial Analysis Models List](/apis/artificial-analysis/models-list) or [Artificial Analysis Search Models](/apis/artificial-analysis/search-models).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/artificial-analysis/llm-providers-leaderboard.json`](../../../catalog/models/artificial-analysis/llm-providers-leaderboard.json) · Store page: https://www.sandbase.ai/model/artificial-analysis/llm-providers-leaderboard
