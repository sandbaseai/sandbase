# X / Twitter Trends API: pricing, parameters and code examples

`twitter/trends` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0001 per call · **Modes:** sync

Get current X (Twitter) trends for worldwide, a country, or a city in X ranking order, including the resolved location.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0001**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/trends"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/trends', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/trends", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/trends", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/twitter/trends` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of ranked trends to return (1-50, default 50). default `50`; range 1–50 |
| `location` | string |  | Country name, city name, or ISO country code. Omit for worldwide trends.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `promoted`, and it is served only by a source that returns every one…  |

## Details

Returns the current ranked list of trending topics on X (Twitter) for worldwide, a country, or a city. It takes an optional `location` (country name, city name, or ISO country code) and an optional `limit`. The response also names the location it resolved.

### Use cases

- Show the top trending topics in the US on a news or social dashboard.
- Track when a topic enters or leaves the top 10 for a country by polling and comparing `rank`.
- Link each trend to its X search page with the `url` field.
- Compare what trends in one city against the whole country.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/trends" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 10, "location": "US"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of ranked trends to return (1-50, default 50). |
| `location` | string | No | Country name, city name, or ISO country code. Omit for worldwide trends. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `promoted`, and it is served only by a source that returns every one o |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "asOfUtc": 1793691889,
    "items": [
      {
        "name": "Bears",
        "query": "Bears",
        "rank": 1,
        "url": "http://twitter.com/search?q=Bears"
      }
    ],
    "location": "United States",
    "locationId": "23424977"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].name` | Display name of the trend, such as `Bears`. |
| `data.items[].query` | Search query for the trend. Use it as the search text in a search call. |
| `data.items[].rank` | Position of the trend in X ranking order. `1` is the top trend. |
| `data.items[].url` | Link to the X search page for the trend. |
| `data.location` | Name of the location the API resolved from your `location` input, such as `United States`. |
| `data.locationId` | ID of the resolved location, as a string. In this response it is `23424977`. |
| `data.asOfUtc` | Time of the trend snapshot. The value looks like a Unix timestamp in seconds. |
| `found` | `true` when the lookup returned a result. A lookup that finds nothing returns `false`. |

### Notes

- Omit `location` to get worldwide trends.
- Set `limit` between 1 and 50. The default is 50.
- Use `requireFields` with `isHashtag` or `promoted` only if you need those fields. This can change which source serves the call and its price.
- To read the posts behind a trend, pass its `query` value to [Twitter Search Timeline](/apis/twitter/search).

### Pricing

Billed at the actual cost of each call, about $0.0001 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/trends.json`](../../../catalog/models/twitter/trends.json) · Store page: https://www.sandbase.ai/model/twitter/trends
