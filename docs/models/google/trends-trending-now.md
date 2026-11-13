# Google Trends Trending Now API: pricing, parameters and code examples

`google/trends-trending-now` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

List searches trending right now on Google in a country, with search volume, growth, start time and related queries, filtered by category and time window.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/trends-trending-now", "geo": "US"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/trends-trending-now', {'geo': 'US'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/trends-trending-now", {
  "geo": "US"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/trends-trending-now", sandbase.Params{
	"geo": "US",
})
```

Same call via the path form: `POST /v1/api/google/trends-trending-now` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hl` | string |  | Parameter defines the language to use for the Google Trends Trending Now search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a…  |
| `geo` | string | yes | Parameter defines the location from where you want the search to originate. It defaults to `US` (activated when the value of `geo` parameter is not set or empty). Head to the Google Trends Trending Now Locations for a…  |
| `hours` | string |  | Parameter defines the number of past hours to retrieve the results for. It defaults to `24` (Past 24 hours). It can be set to: -`4` (Past 4 hours) -`24` (Past 24 hours) -`48` (Past 48 hours) -`168` (Past 7 days).  |
| `category_id` | string |  | Parameter allows results to be filtered by a specific category. E.g.&nbsp;`category_id`:`18` will return only results from the "Technology" category. Head to the Google Trends Trending Now Categories for the full list…  |
| `only_active` | string |  | Parameter filters results to only include those that are currently active.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

List searches trending right now on Google in a country, with search volume, growth, start time and related queries, filtered by category and time window.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/trends-trending-now" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"geo": "US"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `geo` | string | Yes | Parameter defines the location from where you want the search to originate. It defaults to `US` (activated when the value of `geo` parameter is not set or empty). Head to the Google Trends Trending Now Locations for a full list of supported |
| `hours` | string | No | Parameter defines the number of past hours to retrieve the results for. It defaults to `24` (Past 24 hours). It can be set to: -`4` (Past 4 hours) -`24` (Past 24 hours) -`48` (Past 48 hours) -`168` (Past 7 days). |
| `category_id` | string | No | Parameter allows results to be filtered by a specific category. E.g.&nbsp;`category_id`:`18` will return only results from the "Technology" category. Head to the Google Trends Trending Now Categories for the full list of supported categorie |
| `only_active` | string | No | Parameter filters results to only include those that are currently active. |
| `hl` | string | No | Parameter defines the language to use for the Google Trends Trending Now search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit re |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/trends-trending-now.json`](../../../catalog/models/google/trends-trending-now.json) · Store page: https://www.sandbase.ai/model/google/trends-trending-now
