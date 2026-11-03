# TikTok Stream Audience Ranking List API: pricing, parameters and code examples

`tiktok/app-v3/live-ranking-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the audience ranking list for a stream room based on the specified room identifier and anchor identifier. Helps inspect top viewer participation.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/live-ranking-list", "anchor_id": "7222941468722758702", "room_id": "7358603858249009962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/live-ranking-list', {'anchor_id': '7222941468722758702', 'room_id': '7358603858249009962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/live-ranking-list", {
  "anchor_id": "7222941468722758702",
  "room_id": "7358603858249009962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/live-ranking-list", sandbase.Params{
	"anchor_id": "7222941468722758702",
	"room_id": "7358603858249009962",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/live-ranking-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Live room id  |
| `anchor_id` | string | yes | Anchor id  |

## Details

Returns the audience ranking panel for a TikTok LIVE room. You pass the `room_id` and the `anchor_id` of the host. The response holds the ranked viewer list plus display settings and notice text for the panel.

### Use cases

- Read the `ranks` list to see which viewers sit at the top of a LIVE room's audience ranking.
- Check `total` to see how many viewers appear in the ranking for a room.
- Read `currency` and `show_score` to see how the ranking panel presents viewer scores.
- Poll a room during a stream to see whether the ranking list is filled or still empty.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/live-ranking-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"anchor_id": "7222941468722758702", "room_id": "7358603858249009962"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `anchor_id` | string | Yes | Anchor id |
| `room_id` | string | Yes | Live room id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "anchor_show_contribution": true,
    "anonymous": 0,
    "bottom_notice": "Showing the top viewers in this LIVE.",
    "currency": "Coins",
    "deprecated": false,
    "display_config": {
      "avatar_count": 2,
      "can_panel_click": true,
      "show_avatar_list": true,
      "show_online_panel": true,
      "show_score": true
    },
    "preview_count": 0,
    "ranks": [],
    "rule_url": "aweme://roma_redirect/?spark_page=top_view_ranking_new&roma_url_query=show_new_s…",
    "sub_tabs": [],
    "total": 0
  },
  "extra": {
    "now": 1793691833556
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.ranks[]` | List of ranked viewers in the room. It is empty when no viewers are ranked, as in the sample response. |
| `data.total` | Total number of entries in the ranking. The sample response returns `0`. |
| `data.currency` | Name of the currency used by the ranking, for example `Coins`. |
| `data.anchor_show_contribution` | Boolean flag. `true` means the ranking is set to show viewer contributions for the anchor. |
| `data.anonymous` | Numeric anonymity value for the ranking. The sample response returns `0`. |
| `data.bottom_notice` | Notice text shown at the bottom of the ranking panel. |
| `data.display_config.show_score / data.display_config.show_avatar_list / data.display_config.show_online_panel` | Boolean flags for what the panel shows: viewer scores, an avatar list, and the online viewer panel. |
| `data.display_config.avatar_count` | Number of avatars the panel is configured to show. |
| `data.rule_url` | In-app link to the ranking rules page. |
| `extra.now` | Timestamp of the response as a number, in the format shown in the sample (`1793691833556`). |

### Notes

- Both `room_id` and `anchor_id` are required. Take the room ID from a LIVE room lookup such as [TikTok Broadcast Room Information](/apis/tiktok/app-v3/live-room-info).
- Use [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online) to check that the room is online before you request its ranking.
- An empty `ranks` list with `total` of `0` is a valid response with `status_code` `0`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/live-ranking-list.json`](../../../../catalog/models/tiktok/app-v3/live-ranking-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/live-ranking-list
