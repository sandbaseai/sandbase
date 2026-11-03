# IMDb Streaming Picks API: pricing, parameters and code examples

`imdb/streaming-picks-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get IMDb streaming picks for Prime Video using selected language and country preferences. Use it to explore streaming titles for discovery, catalog review, or watchlist research.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/streaming-picks-query"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/streaming-picks-query', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/streaming-picks-query", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/streaming-picks-query", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/imdb/streaming-picks-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

This API returns a list of IMDb title IDs that IMDb picks for streaming on Prime Video. It takes one optional input, `languageCountry`, which sets the language and country preference and defaults to `en_US`.

### Use cases

- Build a Prime Video discovery list from the returned title IDs.
- Collect current streaming picks for a catalog review.
- Seed a watchlist research tool with IDs, then look up details for each title.
- Compare picks across locales by calling the API with different `languageCountry` values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/streaming-picks-query" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `languageCountry` | string | No | Language and country preferences. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "streamingTitles": [
    {
      "titles": {
        "edges": [
          {
            "node": {
              "title": {
                "id": "tt11540908"
              }
            }
          }
        ]
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `streamingTitles[]` | One group of streaming picks. The response holds a list of these groups. |
| `streamingTitles[].titles.edges[]` | One entry per picked title. Each entry wraps a single title in `node`. |
| `streamingTitles[].titles.edges[].node.title.id` | IMDb title ID of the pick, for example `tt11540908`. This is the only field returned for each title. |

### Notes

- The response gives IDs only. It has no title names, ratings or images.
- Title IDs start with `tt` followed by digits. Pass them to other IMDb APIs such as [IMDb Base Info](/apis/imdb/title-base-query) or [IMDb Details](/apis/imdb/title-details-query) to get title data.
- Use [IMDb Plot Summary](/apis/imdb/title-plot-query) to read a short plot for any returned ID.
- Allowed `languageCountry` values are `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US` and `es_MX`.

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/streaming-picks-query.json`](../../../catalog/models/imdb/streaming-picks-query.json) · Store page: https://www.sandbase.ai/model/imdb/streaming-picks-query
