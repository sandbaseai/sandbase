# Douyin Live Room Gift User Ranking API: pricing, parameters and code examples

`douyin/web/live-gift-ranking` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves the contributor gift ranking for a specific Douyin live stream room. Query by room ID and leaderboard type to inspect top gift givers.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/live-gift-ranking", "rank_type": 30, "room_id": "7356585666190461731"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/live-gift-ranking', {'rank_type': 30, 'room_id': '7356585666190461731'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/live-gift-ranking", {
  "rank_type": 30,
  "room_id": "7356585666190461731"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/live-gift-ranking", sandbase.Params{
	"rank_type": 30,
	"room_id": "7356585666190461731",
})
```

Same call via the path form: `POST /v1/api/douyin/web/live-gift-ranking` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Room room_id  |
| `rank_type` | integer |  | Leaderboard type, default is 30, no need to modify. default `30` |

## Details

Returns the gift contributor ranking for one Douyin live room. You send a `room_id` and, optionally, a `rank_type`. The response holds the ranked list, totals, and the ranking info for the requesting viewer.

### Use cases

- Check who gives the most gifts in a Douyin live room.
- Compare the contributor count of a live room across repeated calls.
- Read the ranking rules link that Douyin attaches to a live room leaderboard.
- Check whether a room has had earlier live sessions using a single flag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/live-gift-ranking" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7356585666190461731"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Room room_id |
| `rank_type` | integer | No | Leaderboard type, default is 30, no need to modify. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "currency": "",
    "has_more": false,
    "has_once_live": true,
    "invisible_total": 0,
    "label": "",
    "music_wave": "",
    "ranks": [],
    "rules_url": "sslocal://webcast_webview?url=https%3A%2F%2Faweme.snssdk.com%2Fmagic%2Fpage%2Fej…",
    "seats": [],
    "self_info": {
      "app_name": "",
      "delta": 1,
      "exactly_score": "0",
      "first_gift": false,
      "gap_description": "",
      "is_hidden": false,
      "rank": 0,
      "score": 0,
      "score_description": "0",
      "team_id": "",
      "team_jump_schema": "",
      "user": {
        "adversary_authorization_info": 0,
        "adversary_user_status": 0,
        "age_range": 0,
        "allow_be_located": false,
        "allow_find_by_contacts": false,
        "allow_others_download_video": false,
        "allow_others_download_when_sharing_video": false,
        "allow_share_show_profile": false
      }
    },
    "service_days": 0,
    "total": 0
  },
  "extra": {
    "now": 1793691146979
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.ranks[]` | List of ranked gift contributors for the room. It is empty in this sample response, so a room with no gifts returns no rows. |
| `data.total` | Total count for the leaderboard. It is `0` in this sample. |
| `data.user_count_desc` | Text version of the user count shown on the leaderboard. It is `"0"` in this sample. |
| `data.has_more` | Shows whether more ranking entries exist beyond the returned list. |
| `data.has_once_live` | Boolean flag for the room. It is `true` in this sample. |
| `data.rules_url` | Link to the leaderboard rules page, in a Douyin app `sslocal://` format. |
| `data.self_info.rank / data.self_info.score` | Rank and gift score of the requesting viewer. Both are `0` in this sample. |
| `data.self_info.score_description / data.self_info.exactly_score` | Score as text. `exactly_score` is a string and `score_description` is a display string. |
| `data.self_info.user` | User profile object for the requesting viewer, with many account setting flags. |
| `status_code` | Request status. `0` means success. |

### Notes

- Get `room_id` from a Douyin live room link. [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id) extracts webcast IDs, and [Douyin Webcast ID to Room ID](/apis/douyin/web/webcast-id-2-room-id) converts a webcast ID to a `room_id`.
- Leave `rank_type` at its default of `30` unless you need another leaderboard type.
- `extra.now` is a 13-digit timestamp, which looks like Unix time in milliseconds.
- `data.ranks` and `data.seats` can be empty arrays, so handle empty lists in your code.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/live-gift-ranking.json`](../../../../catalog/models/douyin/web/live-gift-ranking.json) · Store page: https://www.sandbase.ai/model/douyin/web/live-gift-ranking
