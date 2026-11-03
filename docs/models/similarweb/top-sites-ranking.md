# Similarweb Top Sites Ranking API: pricing, parameters and code examples

`similarweb/top-sites-ranking` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.075 per call · **Modes:** sync

Get the top-ranked websites worldwide or in a category, ordered by traffic rank.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.075 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/top-sites-ranking", "category": "all", "limit": 3}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/top-sites-ranking', {'category': 'all', 'limit': 3})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/top-sites-ranking", {
  "category": "all",
  "limit": 3
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/top-sites-ranking", sandbase.Params{
	"category": "all",
	"limit": 3,
})
```

Same call via the path form: `POST /v1/api/similarweb/top-sites-ranking` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `offset` | integer |  | offset range 0–100000 |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `category` | string | yes | category  |

## Details

Returns a list of the top-ranked websites worldwide, ordered by traffic rank. It needs a `category` (for example `all`) and a `limit` of 1 to 20 rows.

### Use cases

- Build a leaderboard of the most visited websites worldwide.
- Check which domains hold the top ranks in a given category.
- Seed a competitor list with the highest-ranked domains before deeper analysis.
- Track how many sites you need to page through to reach a target rank with `offset`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/top-sites-ranking" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category": "all", "country": "ww", "limit": 3}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | category |
| `limit` | integer | Yes | limit |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `offset` | integer | No | offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "domain": "google.com",
      "rank": 1
    }
  ],
  "meta": {
    "last_updated": "2026-09-30",
    "query": {
      "asc": null,
      "limit": 3,
      "offset": 0,
      "sort": null
    },
    "request": {
      "category": "all",
      "channel": "total",
      "country": "ww",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "start_date": "2026-07-01",
      "web_source": "total"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One ranked website. The list is ordered by rank. |
| `data[].domain` | Domain name of the ranked website, such as `google.com`. |
| `data[].rank` | Traffic rank of the domain. `1` is the top site. |
| `meta.last_updated` | Date of the ranking data, in `YYYY-MM-DD` format. |
| `meta.query.limit / meta.query.offset` | The page size and starting position applied to this call. |
| `meta.request.category` | Category the ranking was built for. `all` means no category filter. |
| `meta.request.country` | Country scope of the ranking. `ww` means worldwide. |
| `meta.request.start_date / meta.request.end_date` | Date range the ranking covers, in `YYYY-MM-DD` format. |
| `meta.request.granularity` | Time grain of the data. The sample shows `monthly`. |
| `meta.status` | Result of the call. `success` means the request worked. |

### Notes

- Use `offset` with `limit` to page through the list. `limit` accepts 1 to 20 and `offset` accepts 0 to 100000.
- `country` accepts only `ww` (worldwide), and the value is case-insensitive.
- To see ranking details for a single domain, call [Similarweb Website Ranking](/apis/similarweb/ranking).
- To see traffic numbers for a domain from this list, call [Similarweb Website Traffic Snapshot](/apis/similarweb/website-traffic-snapshot).

### Pricing

Billed at the actual cost of each call, about $0.075 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/top-sites-ranking.json`](../../../catalog/models/similarweb/top-sites-ranking.json) · Store page: https://www.sandbase.ai/model/similarweb/top-sites-ranking
