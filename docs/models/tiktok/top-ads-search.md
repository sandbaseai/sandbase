# TikTok Top Ads Search API: pricing, parameters and code examples

`tiktok/top-ads-search` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search TikTok Creative Center top video ads by keyword, with campaign objective, performance percentile, and time-window filters.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/top-ads-search", "query": "glasses"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/top-ads-search', {'query': 'glasses'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/top-ads-search", {
  "query": "glasses"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/top-ads-search", sandbase.Params{
	"query": "glasses",
})
```

Same call via the path form: `POST /v1/api/tiktok/top-ads-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | One-based provider page number (default 1). default `1`; range 1– |
| `limit` | integer |  | Maximum number of ads requested for this page, from 1 through 20 (default 20). default `20`; range 1–20 |
| `query` | string | yes | Keyword to search in TikTok Creative Center top video ads.  |
| `period` | integer |  | Lookback period in days (default 180). one of: `7`, `30`, `180`; default `180` |
| `objective` | string |  | Campaign objective filter. Omit it to search every objective. one of: `traffic`, `app_installs`, `conversions`, `video_views`, `reach`, `lead_generation`, `product_sales` |
| `performanceRank` | string |  | Ad performance percentile bucket, where top_1_20 is the highest-performing 20 percent. Omit it to search every bucket. one of: `top_1_20`, `top_21_40`, `top_41_60`, `top_61_80` |

## Details

This API searches TikTok Creative Center top video ads for a keyword. It returns a page of ads with title, brand, likes, click-through rate, video length, and media links. It needs a `query` and accepts optional filters for objective, performance bucket, and lookback period.

### Use cases

- Collect high-performing glasses ads to study the hooks and offers that competitors run.
- Filter by `objective` to compare conversion ads with video view ads for the same keyword.
- Narrow results to the `top_1_20` performance bucket to build a swipe file of the strongest creatives.
- Track which brands advertise a product category by listing `brandName` across several pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/top-ads-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "glasses"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search in TikTok Creative Center top video ads. |
| `limit` | integer | No | Maximum number of ads requested for this page, from 1 through 20 (default 20). |
| `objective` | string | No | Campaign objective filter. Omit it to search every objective. |
| `page` | integer | No | One-based provider page number (default 1). |
| `performanceRank` | string | No | Ad performance percentile bucket, where top_1_20 is the highest-performing 20 percent. Omit it to search every bucket. |
| `period` | integer | No | Lookback period in days (default 180). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "ads": [
      {
        "adId": "7231584422875676673",
        "adTitle": "The best way to clean - 80% off, ends soon-634222",
        "brandName": "متجر الخليج",
        "cost": 2,
        "ctr": 0.16,
        "durationSeconds": 14.8,
        "height": 1024,
        "image": "https://p16-common-sign.tiktokcdn.com/tos-alisg-p-0037/oEBKAY2XAFC1PC2AIoEDhcfiQ…",
        "industry": "label_18106000000",
        "likes": 17219,
        "objective": "campaign_objective_conversion",
        "videoUrl": "https://v16m-default.tiktokcdn.com/3a0edf7542973ffeb3b20f2f5b890b2f/6ae9e540/vid…"
      }
    ],
    "hasMore": true,
    "page": 1,
    "pageSize": 20,
    "total": 300
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.ads[].adId` | ID of the ad as a string. Use it to identify the same ad across searches. |
| `data.ads[].adTitle / data.ads[].brandName` | Title text of the ad and the name of the advertiser brand. |
| `data.ads[].likes` | Number of likes on the ad. |
| `data.ads[].ctr` | Click-through rate of the ad as a decimal number, for example `0.16`. |
| `data.ads[].cost` | Cost level of the ad as a small whole number. The response does not show what the scale means. |
| `data.ads[].durationSeconds` | Length of the ad video in seconds. |
| `data.ads[].objective / data.ads[].industry` | Campaign objective of the ad, such as `campaign_objective_conversion`, and an industry label code such as `label_22101000000`. |
| `data.ads[].videoUrl / data.ads[].image` | Links to the ad video and its cover image. |
| `data.ads[].width / data.ads[].height` | Pixel size of the ad video, for example 576 by 1024. |
| `data.hasMore / data.page / data.pageSize / data.total` | Pagination info: whether more pages exist, the current page number, the page size, and the total number of matching ads. |

### Notes

- Set `page` to get the next page while `data.hasMore` is `true`. `limit` accepts 1 to 20 ads per page.
- The `objective` filter uses values like `conversions`, but each ad returns its objective as a value like `campaign_objective_conversion`.
- The media links in `videoUrl` and `image` include signed parameters, so save the files if you need them later.
- To look at one ad in depth, try [TikTok Ad Detail](/apis/tiktok/ads/ads-detail). For keyword ideas, try [TikTok Ad Query Suggestions](/apis/tiktok/ads/query-suggestions).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/top-ads-search.json`](../../../catalog/models/tiktok/top-ads-search.json) · Store page: https://www.sandbase.ai/model/tiktok/top-ads-search
