# TikTok Livestream Homepage Recommendations API: pricing, parameters and code examples

`tiktok/web/live-recommend` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended livestreams from the TikTok homepage for a specified category tag. Requires selecting a category tag to retrieve relevant active broadcast recommendations.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/live-recommend", "related_live_tag": "test"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/live-recommend', {'related_live_tag': 'test'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/live-recommend", {
  "related_live_tag": "test"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/live-recommend", sandbase.Params{
	"related_live_tag": "test",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/live-recommend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `related_live_tag` | string | yes | Related live tag (live category). The available values are not fixed; call `/fetch_live_recommend_tabs` first to get the currently available tag list, then pick one to pass in.  |

## Details

Returns a list of recommended livestream rooms from the TikTok homepage for one live category tag. It needs a `related_live_tag` value such as `VALORANT`.

### Use cases

- Pull the current livestream cards shown for a game category such as `VALORANT`.
- Collect cover images of recommended live rooms to show in an external dashboard.
- Check whether more recommendations exist for a tag before you request another batch.
- Store the `rid` of each result to match a recommendation batch with a later analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/live-recommend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"related_live_tag": "VALORANT"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `related_live_tag` | string | Yes | Related live tag (live category). The available values are not fixed; call `/fetch_live_recommend_tabs` first to get the currently available tag list, then pick one to pass in. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cookie": "tt_chain…",
  "data": [
    {
      "data": {
        "age_restricted": {},
        "anchor_tab_type": 7,
        "blurred_cover": {
          "avg_color": "#FAE6DC",
          "height": 100,
          "uri": "tos-maliva-avt-0068/e1c653d347180dc3f095dd5185877b22",
          "url_list": [
            "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/e1c653d347180dc3f095dd…"
          ],
          "width": 100
        },
        "client_version": 13800,
        "commerce_info": {},
        "cover": {
          "uri": "720x720/tos-maliva-avt-0068/e1c653d347180dc3f095dd5185877b22",
          "url_list": [
            "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/e1c653d347180dc3f095dd…"
          ]
        },
        "cover_type": 1,
        "enlarge_view_info": {
          "enabler_enlarge_view": true,
          "landscape_view": 1,
          "portrait_view": 1
        }
      },
      "flare_info": {},
      "rid": "202611031544263DDB5AFB9E6F854E228A",
      "room_event_tracking": "pc_web_game_sub_feed_refresh:1111006:normal:1:0",
      "type": 1
    }
  ],
  "extra": {
    "banner": {},
    "cost": 113,
    "has_more": true,
    "log_pb": {
      "impr_id": "202611031544263DDB5AFB9E6F854E228A",
      "session_id": 7703847894004796178
    },
    "max_time": 1793691866273,
    "now": 1793691866273,
    "total": 12,
    "unread_extra": "{\"channel_id\":1111006,\"req_from\":\"pc_web_game_sub_feed_refresh\",\"gen_time\":17936…"
  },
  "status_code": 0,
  "tt_chain_token": "0k5cdiqY…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].data.cover.url_list` | Image URLs for the 720x720 cover of the livestream. Each entry points to the same image in a different CDN host or format (`webp` or `jpeg`). |
| `data[].data.blurred_cover.url_list` | URLs of a small 100x100 blurred version of the cover. |
| `data[].data.blurred_cover.avg_color` | Average color of the blurred cover as a hex code. Use it as a placeholder color while the image loads. |
| `data[].data.feed_room_label.url_list` | Image URLs for a label shown on the room card. It appears only on some items. |
| `data[].data.anchor_tab_type` | Numeric tab type for the livestream entry. The response shows `7` for all items. |
| `data[].rid` | Request ID shared by all items in the same response. It matches `extra.log_pb.impr_id`. |
| `data[].room_event_tracking` | Tracking string for the feed that returned the item. It includes the feed name `pc_web_game_sub_feed_refresh`. |
| `extra.has_more` | Shows `true` when more recommendations are available. |
| `extra.total` | Total count reported for this response. |
| `extra.now / extra.max_time` | Timestamps in milliseconds, in the same format as `1793691866273`. |

### Notes

- Get valid `related_live_tag` values from [TikTok Stream Recommendation Tabs](/apis/tiktok/web/live-recommend-tabs) first. The list of tags changes, so do not hard-code it.
- The only request parameter is `related_live_tag`. The response gives `extra.has_more` but this API has no pagination parameter.
- Each item in `data[]` wraps its details in a second `data` object, so the full path is `data[].data`.
- The response also returns `tt_chain_token` and `cookie` at the top level.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/live-recommend.json`](../../../../catalog/models/tiktok/web/live-recommend.json) · Store page: https://www.sandbase.ai/model/tiktok/web/live-recommend
