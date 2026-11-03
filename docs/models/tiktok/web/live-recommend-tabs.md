# TikTok Stream Recommendation Tabs API: pricing, parameters and code examples

`tiktok/web/live-recommend-tabs` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns available recommendation tabs and category tags for TikTok broadcast homepages. Supports pagination via a log identifier cursor.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/live-recommend-tabs"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/live-recommend-tabs', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/live-recommend-tabs", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/live-recommend-tabs", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/live-recommend-tabs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `logid` | string |  | Pagination cursor. Leave empty for the first page; to load the next page, pass the `logid` value returned by the previous response default `""` |

## Details

Retrieve available stream recommendation tabs and sub-tabs from TikTok. Pass `logid` to paginate through subsequent pages of recommendations.

### Use cases

- Explore trending broadcast tags and gaming categories.
- Monitor viewer counts across featured stream categories.
- Populate category navigation filters in external streaming dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/live-recommend-tabs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `logid` | string | No | Pagination cursor. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "sub_tabs": [
        {
          "cover_url": "https://p16-common-sign.tiktokcdn.com/tos-alisg-i-agnx3xz2cs-sg/Garena_Free_Fire…",
          "rank_type": "hot_game",
          "tab_name": "Garena Free Fire",
          "tab_type": "Garena Free Fire",
          "viewer_count": 156952
        }
      ]
    }
  ]
}
```

### Notes

- Pass the `logid` returned from a prior response to load the next page of results, or leave it empty for the initial page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/live-recommend-tabs.json`](../../../../catalog/models/tiktok/web/live-recommend-tabs.json) · Store page: https://www.sandbase.ai/model/tiktok/web/live-recommend-tabs
