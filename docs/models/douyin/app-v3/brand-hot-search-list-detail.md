# Douyin Brand Hot Search List Detail API: pricing, parameters and code examples

`douyin/app-v3/brand-hot-search-list-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed brand hot search list data from Douyin for a specific category. Requires a category identifier to filter the ranking results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/brand-hot-search-list-detail", "category_id": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/brand-hot-search-list-detail', {'category_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/brand-hot-search-list-detail", {
  "category_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/brand-hot-search-list-detail", sandbase.Params{
	"category_id": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/brand-hot-search-list-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `category_id` | integer | yes | Category id  |

## Details

Returns the Douyin brand hot search ranking for one category. Each entry has the brand name, rank, heat score, and change since the last period. You pass a `category_id` to pick the category.

### Use cases

- Track which car brands rank highest on the Douyin brand hot search list for a category.
- Compare `heat` and `heat_diff` across brands to see who gained or lost attention.
- Spot brands that are live right now using `is_in_webcasting`.
- Pull brand logos and Blue V account IDs to match ranked brands to their Douyin accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/brand-hot-search-list-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_id": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_id` | integer | Yes | Category id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "banner_url": {
    "uri": "daa7000a0f0d6a308320",
    "url_list": [
      "https://p11-sign.douyinpic.com/obj/daa7000a0f0d6a308320?x-expires=1793775600&x-s…"
    ]
  },
  "banners": [
    {
      "click_track_url_list": null,
      "track_url_list": null
    }
  ],
  "brand_list": [
    {
      "bluev_sec_uid": "MS4wLjABAAAA7JaN8kq2bxUyOaeVzlgLXn950lMzirx3Hiu6F0w6Puo",
      "bluev_uid": "97358678838",
      "explain_tag_desc": "",
      "heat": 255279,
      "heat_diff": 10554,
      "id": 10246,
      "interactive_tag_type": 0,
      "is_in_webcasting": false,
      "logo_url": {
        "uri": "https://lf3-trendinsight.bytetos.com/obj/ad-count-platform/8a99e943bd28952c",
        "url_list": [
          "https://lf3-trendinsight.bytetos.com/obj/ad-count-platform/8a99e943bd28952c"
        ]
      },
      "mp_url": "sslocal://microapp?app_id=tt29865f3bb6bfdf9101&bdp_log=%7B%22enter_from%22%3A%22…",
      "name": "奇瑞",
      "rank": 1
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153133DD74A27D514ED842AB28",
    "now": 1793691093000
  },
  "log_pb": {
    "impr_id": "20261103153133DD74A27D514ED842AB28"
  },
  "status_code": 0,
  "status_msg": "",
  "weekly_info": {
    "end_date": "2026-10-24",
    "is_current": false,
    "last_updated_date": "2026-10-28",
    "serial": 3,
    "start_date": "2026-10-18"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `brand_list[].name` | Brand name as shown on the list. |
| `brand_list[].rank / brand_list[].rank_diff` | Current position on the list and the change in position. A positive `rank_diff` means the brand moved up, as seen with rank 1 and `rank_diff` 1. |
| `brand_list[].heat / brand_list[].heat_diff` | Heat score of the brand and its change from the previous period. A negative `heat_diff` means the heat fell. |
| `brand_list[].id` | Numeric ID of the brand. |
| `brand_list[].is_in_webcasting` | `true` when the brand is running a live stream at the time of the call. |
| `brand_list[].bluev_uid / brand_list[].bluev_sec_uid` | User ID and `sec_uid` of the brand's Blue V (verified) Douyin account. |
| `brand_list[].logo_url.url_list[]` | Image URLs for the brand logo. |
| `weekly_info.start_date / weekly_info.end_date` | First and last day of the week covered by the ranking, in `YYYY-MM-DD` format. |
| `weekly_info.serial / weekly_info.is_current` | Serial number of the weekly list, and whether it is the current week. |
| `banner_url.url_list[]` | Image URLs for the list banner. |

### Notes

- `category_id` is the only input and it is required. Get valid category values from [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list).
- `status_code` is `0` when the call succeeds.
- `extra.now` is a Unix timestamp in milliseconds.
- The response has no pagination parameters.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.
- [Douyin Video Share QR Code](/apis/douyin/app-v3/generate-video-share-qrcode): Returns a Douyin share QR code for a designated target.

---
Machine-readable: [`catalog/models/douyin/app-v3/brand-hot-search-list-detail.json`](../../../../catalog/models/douyin/app-v3/brand-hot-search-list-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/brand-hot-search-list-detail
