# Douyin Web Series Videos API: pricing, parameters and code examples

`douyin/web/series-aweme` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a paginated list of series videos from the Douyin web platform. Results can be filtered by content subtype, page number, and page size.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/series-aweme", "content_type": 1, "count": 1, "offset": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/series-aweme', {'content_type': 1, 'count': 1, 'offset': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/series-aweme", {
  "content_type": 1,
  "count": 1,
  "offset": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/series-aweme", sandbase.Params{
	"content_type": 1,
	"count": 1,
	"offset": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/web/series-aweme` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer | yes | Number per page, default is 16  |
| `offset` | integer | yes | Page number, default is 0  |
| `content_type` | integer | yes | Subtype, default is 0  |

## Details

Returns a paginated list of series videos (short episodic dramas) from the Douyin web platform. It needs `content_type`, `count` and `offset`. Each card holds a video ID plus series details such as the author, cover image and pricing.

### Use cases

- Build a catalog of paid short drama series currently listed on Douyin.
- Compare episode counts and per-episode prices across series.
- Collect cover images and author avatars for a series discovery page.
- Track newly created series by sorting on `create_time`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/series-aweme" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"content_type": 0, "count": 16, "offset": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `content_type` | integer | Yes | Subtype, default is 0 |
| `count` | integer | Yes | Number per page, default is 16 |
| `offset` | integer | Yes | Page number, default is 0 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "card_list": [
    {
      "aweme_id": "7691366885727800611",
      "card_scene": 1,
      "series": {
        "actors": [],
        "author": {
          "accept_private_policy": false,
          "account_region": "",
          "ad_cover_url": null,
          "allow_story_normal_like": false,
          "apple_account": 0,
          "authority_status": 0,
          "avatar_168x168": {
            "height": 720,
            "uri": "168x168/aweme-avatar/tos-cn-avt-0015_6c86ff301426f5e2268337378b1193ed",
            "url_list": [
              "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_6c86ff301426f5e2268…"
            ],
            "width": 720
          },
          "avatar_300x300": {
            "height": 720,
            "uri": "300x300/aweme-avatar/tos-cn-avt-0015_6c86ff301426f5e2268337378b1193ed",
            "url_list": [
              "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_6c86ff301426f5e2268…"
            ],
            "width": 720
          }
        },
        "charge_info": {
          "buy_schema": "sslocal://webcast_redirect?entry=ent_playlet_bill&product_id=7691316314564940841…",
          "charge_count": 55,
          "charge_episodes": null,
          "charge_type": 1,
          "has_paid": false,
          "paid_episodes": null,
          "promise_update_time": 1791993600,
          "sell_type": 2
        },
        "charge_strategy": {
          "discount_threshold": 5,
          "has_paid_episodes": 0,
          "is_charge": 0,
          "support_segment_unlock": true,
          "total_price": 825,
          "unit_price": 15
        },
        "content_sub_type": 0,
        "cover_url": {
          "height": 720,
          "uri": "tos-cn-i-dy/2f433ea9e0cd3fd35d2f44021ebfd669",
          "url_list": [
            "https://p3-sign.douyinpic.com/tos-cn-i-dy/2f433ea9e0cd3fd35d2f44021ebfd669~tplv-…"
          ],
          "width": 720
        },
        "create_time": 1790774315,
        "dark_icon_url": {
          "height": 720,
          "uri": "tos-cn-i-30241dr4mi/f6bfed05d3354fbd86127c49c563a197",
          "url_list": [
            "https://p3-sign.douyinpic.com/obj/tos-cn-i-30241dr4mi/f6bfed05d3354fbd86127c49c5…"
          ],
          "width": 720
        }
      }
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611031532326F1A13E262C0BC4D1EFF",
    "now": 1793691152000
  },
  "has_more": true,
  "log_pb": {
    "impr_id": "202611031532326F1A13E262C0BC4D1EFF"
  },
  "offset": 16,
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `card_list[].aweme_id` | ID of the video that represents the series card. |
| `card_list[].series.create_time` | Unix timestamp in seconds for when the series was created. |
| `card_list[].series.cover_url.url_list[]` | Cover image URLs for the series, in webp and jpeg formats. The URLs carry `x-expires` and `x-sign` query parameters. |
| `card_list[].series.author.avatar_168x168.url_list[] / card_list[].series.author.avatar_300x300.url_list[]` | Author avatar image URLs at 168x168 and 300x300 sizes. |
| `card_list[].series.charge_info.charge_count` | Number of episodes covered by the charge settings for the series. |
| `card_list[].series.charge_info.promise_update_time` | Unix timestamp in seconds tied to the series update promise. |
| `card_list[].series.charge_strategy.unit_price / card_list[].series.charge_strategy.total_price` | Price per episode and price for the whole series. The response does not state the currency or unit. |
| `card_list[].series.charge_strategy.support_segment_unlock` | Whether the series supports unlocking episodes in segments. |
| `has_more` | `true` when more results are available after this page. |
| `offset` | Offset value to send in the next request to get the following page. |

### Notes

- Send `content_type` as `0` to match the default subtype. The response does not list other values.
- Pagination: the request used `offset` `0` and `count` `16`, and the response returned `offset` `16` with `has_more` set to `true`. Pass the returned `offset` in the next call.
- Check `status_code`: `0` with an empty `status_msg` means the call succeeded.
- To get full details for a video in a card, pass its `aweme_id` to [Douyin Single Video Details (V1)](/apis/douyin/web/one-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/series-aweme.json`](../../../../catalog/models/douyin/web/series-aweme.json) · Store page: https://www.sandbase.ai/model/douyin/web/series-aweme
