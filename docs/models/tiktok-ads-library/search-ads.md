# TikTok Ads Library Search Ads API: pricing, parameters and code examples

`tiktok-ads-library/search-ads` · data API · TikTok Ads Library · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.06 per call · **Modes:** sync

Search the TikTok Ad Library for ads matching a query (advertiser name or keyword).

## Pricing

- **$0.06 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-ads-library/search-ads", "query": "nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-ads-library/search-ads', {'query': 'nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-ads-library/search-ads", {
  "query": "nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-ads-library/search-ads", sandbase.Params{
	"query": "nike",
})
```

Same call via the path form: `POST /v1/api/tiktok-ads-library/search-ads` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of results per page (max 50) default `12` |
| `query` | string | yes | Search query (advertiser name or keyword)  |
| `offset` | integer |  | Pagination offset (0-based). Requires search_id from a previous response for values > 0. default `0` |
| `region` | string |  | Region/country code filter (e.g. 'FR', 'DE', 'GB') or 'all' for all regions. Use get_supported_regions for the full list of accepted codes. one of: `all`, `FR`, `DE`, `GB`; default `"all"` |
| `sort_by` | string |  | Sort order: 'last_shown_date,desc' or 'last_shown_date,asc' one of: `last_shown_date,desc`, `last_shown_date,asc`; default `"last_shown_date,desc"` |
| `end_time` | integer |  | End of date range as Unix timestamp (seconds). Defaults to now.  |
| `search_id` | string |  | Search ID returned from a previous search_ads call. Required when offset > 0 to paginate through results.  |
| `start_time` | integer |  | Start of date range as Unix timestamp (seconds). Defaults to 1 year ago.  |

## Details

Search the TikTok Ad Library for ads matching a query (advertiser name or keyword).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "tiktok-ads-library/search-ads", "limit": 12, "query": "nike", "offset": 0, "region": "all", "sort_by": "last_shown_date,desc", "search_id": ""}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query (advertiser name or keyword) |
| `end_time` | integer | No | End of date range as Unix timestamp (seconds). Defaults to now. |
| `limit` | integer | No | Number of results per page (max 50) |
| `offset` | integer | No | Pagination offset (0-based). Requires search_id from a previous response for values > 0. |
| `region` | string | No | Region/country code filter (e.g. 'FR', 'DE', 'GB') or 'all' for all regions. Use get_supported_regions for the full list of accepted codes. One of: `all`, `FR`, `DE`, `GB`. |
| `search_id` | string | No | Search ID returned from a previous search_ads call. Required when offset > 0 to paginate through results. |
| `sort_by` | string | No | Sort order: 'last_shown_date,desc' or 'last_shown_date,asc' One of: `last_shown_date,desc`, `last_shown_date,asc`. |
| `start_time` | integer | No | Start of date range as Unix timestamp (seconds). Defaults to 1 year ago. |

### Pricing

Flat $0.06 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok-ads-library/search-ads.json`](../../../catalog/models/tiktok-ads-library/search-ads.json) · Store page: https://www.sandbase.ai/model/tiktok-ads-library/search-ads
