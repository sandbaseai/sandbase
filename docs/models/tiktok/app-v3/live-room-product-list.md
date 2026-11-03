# TikTok Livestream Room Product List API: pricing, parameters and code examples

`tiktok/app-v3/live-room-product-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of showcase products featured in a broadcast session based on the specified room and author identifiers, with support for region filtering and pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/live-room-product-list", "author_id": "7408859677050274859", "room_id": "7420741353250507562"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/live-room-product-list', {'author_id': '7408859677050274859', 'room_id': '7420741353250507562'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/live-room-product-list", {
  "author_id": "7408859677050274859",
  "room_id": "7420741353250507562"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/live-room-product-list", sandbase.Params{
	"author_id": "7408859677050274859",
	"room_id": "7420741353250507562",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/live-room-product-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Page turning cursor, optional parameter, default is 0, increasing by 15 each time.  |
| `region` | string |  | Region, optional parameter, default is `US`. Other regions (for example `VN`) may return no data.  |
| `room_id` | string | yes | Live room id, required parameter.  |
| `author_id` | string | yes | Anchor id, required parameter.  |
| `page_size` | integer |  | Number per page, optional parameter, default is 15.  |

## Details

Returns the list of showcase products featured in a TikTok LIVE room, plus the display settings for the shopping bag. It needs a `room_id` and an `author_id`, and it accepts optional `region`, `offset` and `page_size` parameters.

### Use cases

- Check whether a specific LIVE room has any products in its shopping bag.
- Page through the products a host promotes in one broadcast.
- Read the total product count for a room with `total`.
- Compare the same room across regions by changing `region`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/live-room-product-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_id": "7408859677050274859", "room_id": "7420741353250507562"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `author_id` | string | Yes | Anchor id, required parameter. |
| `room_id` | string | Yes | Live room id, required parameter. |
| `offset` | integer | No | Page turning cursor, optional parameter, default is 0, increasing by 15 each time. |
| `page_size` | integer | No | Number per page, optional parameter, default is 15. |
| `region` | string | No | Region, optional parameter, default is `US`. Other regions (for example `VN`) may return no data. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "AIGC_term_banner": null,
    "all_product_ids": null,
    "atmosphere_tag_info": null,
    "bag_prom_logos": null,
    "bonus_entry": null,
    "buy_button_config": {
      "live_bag_buy_button_config": {
        "0": {
          "background_color": "#fe2c55ff",
          "background_color_dark_mode": "#ff3b5cff",
          "display_text": "购买",
          "display_text_color": "#ffffffff",
          "display_text_color_dark_mode": "#ffffffff",
          "toast": ""
        },
        "1": {
          "background_color": "#16182319",
          "background_color_dark_mode": "#ffffff19",
          "display_text": "购买",
          "display_text_color": "#00000052",
          "display_text_color_dark_mode": "#ffffff57",
          "toast": "商品已售罄"
        },
        "2": {
          "background_color": "#16182319",
          "background_color_dark_mode": "#ffffff19",
          "display_text": "购买",
          "display_text_color": "#00000052",
          "display_text_color_dark_mode": "#ffffff57",
          "toast": "商品已售罄"
        },
        "3": {
          "background_color": "#16182319",
          "background_color_dark_mode": "#ffffff19",
          "display_text": "即将开始",
          "display_text_color": "#00000052",
          "display_text_color_dark_mode": "#ffffff57",
          "toast": "你可以在直播秒杀开始时购买此商品。"
        }
      },
      "pin_card_buy_button_config": {
        "0": {
          "background_color": "#FFFE2C55",
          "background_color_dark_mode": "#FFFE2C55",
          "display_text": "购买",
          "display_text_color": "#FFFFFFFF",
          "display_text_color_dark_mode": "#FFFFFFFF",
          "toast": ""
        },
        "1": {
          "background_color": "#0F161823",
          "background_color_dark_mode": "#0F161823",
          "display_text": "购买",
          "display_text_color": "#52000000",
          "display_text_color_dark_mode": "#52000000",
          "toast": "商品已售罄"
        },
        "2": {
          "background_color": "#0F161823",
          "background_color_dark_mode": "#0F161823",
          "display_text": "售罄",
          "display_text_color": "#52000000",
          "display_text_color_dark_mode": "#52000000",
          "toast": "商品已售罄"
        },
        "3": {
          "background_color": "#0F161823",
          "background_color_dark_mode": "#0F161823",
          "display_text": "即将开始",
          "display_text_color": "#52000000",
          "display_text_color_dark_mode": "#52000000",
          "toast": "你可以在直播秒杀开始时购买此商品。"
        }
      }
    },
    "cart_entry": null,
    "cart_meta_bar": null,
    "coupon_entry": null,
    "coupons_activity_ui_type": 3,
    "flash_sale_atmosphere_info": [],
    "flash_sale_refresh_control": {
      "show_atmosphere_begin_millisecond": 1200000,
      "show_atmosphere_stock_change_limit": 0,
      "show_live_flash_sale_atmosphere": 1,
      "weaken_live_flash_sale_atmosphere": 0
    }
  },
  "msg": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code / msg` | Status of the call. `code` is `0` and `msg` is `success` when the request worked. |
| `data.products[]` | List of showcase products in the room. It is an empty list in this example, so the room had no products returned. |
| `data.total` | Total number of products reported for the room. It is `0` in this example. |
| `data.all_product_ids` | List of all product IDs in the room. It is `null` in this example. |
| `data.server_time` | Server timestamp of the response. The value `1793691834763` has 13 digits. |
| `data.buy_button_config.live_bag_buy_button_config` | Buy button styles for the shopping bag, keyed by state number (`0` to `3`). Each state has `display_text`, colors and a `toast` message. |
| `data.buy_button_config.pin_card_buy_button_config` | Buy button styles for the pinned product card, keyed by the same state numbers. Each state has `display_text`, colors and a `toast` message. |
| `data.live_bag_entry_layout.coupon_entry / data.live_bag_entry_layout.cart_entry` | Entry points shown in the shopping bag. Each one has a `link`, and the coupon entry also has a `text` label. |
| `data.flash_sale_refresh_control` | Display settings for the flash sale banner, such as `show_live_flash_sale_atmosphere` and `show_atmosphere_begin_millisecond`. |

### Notes

- Use `offset` to page. The default is `0`, and it grows by 15 for each page, matching the default `page_size` of 15.
- `region` defaults to `US`. Other regions, for example `VN`, may return no data.
- The example response has an empty `products` list and `total` of `0`. The rest of `data` holds display settings, and many of those keys are `null`.
- Check that a room is live first with [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online). Get room details with [TikTok Broadcast Room Information](/apis/tiktok/app-v3/live-room-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/live-room-product-list.json`](../../../../catalog/models/tiktok/app-v3/live-room-product-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/live-room-product-list
