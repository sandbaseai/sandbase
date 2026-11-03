# Pipixia Post Statistics API: pricing, parameters and code examples

`pipixia/app/post-statistics` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns engagement metrics and statistics for a single Pipixia post using its identifier. Includes figures such as likes, comments, and reposts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/post-statistics", "cell_id": "7411193113223371043"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/post-statistics', {'cell_id': '7411193113223371043'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/post-statistics", {
  "cell_id": "7411193113223371043"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/post-statistics", sandbase.Params{
	"cell_id": "7411193113223371043",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/post-statistics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cell_id` | string | yes | AKA video id, can be obtained from the share link.  |

## Details

Returns engagement counts for one Pipixia post, such as likes, comments, shares, plays and impressions. The only input is the post's `cell_id`, which is the video ID.

### Use cases

- Track how likes, comments and shares change on a single Pipixia video by calling it on a schedule.
- Compare `play_count` with `impression_count` and `go_detail_count` to see how many viewers open the post.
- Check a post's `reward_count` and `ward_info.ward_count` when you rank posts by audience support.
- Build a stats dashboard for a list of Pipixia video IDs you already hold.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/post-statistics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cell_id": "7411193113223371043"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cell_id` | string | Yes | AKA video id, can be obtained from the share link. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "data": [
      {
        "author": {
          "is_following": false
        },
        "bury_count": -1,
        "bury_counts": [
          {
            "bury_count": -1,
            "bury_type": 10
          }
        ],
        "bury_type": 10,
        "comment_count": 1257,
        "digg_counts": [
          {
            "digg_count": 16560,
            "digg_type": 10
          }
        ],
        "digg_type": 10,
        "dubbing_count": 0,
        "go_detail_count": 388260,
        "impression_count": 7066460,
        "is_bury": false,
        "is_like": false
      }
    ]
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691713155
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.data[].item_id_str` | The post ID as a string. It matches the `cell_id` you sent. Use this form to avoid rounding of the large number in `item_id`. |
| `data.data[].like_count` | Total likes on the post. |
| `data.data[].comment_count` | Number of comments on the post. |
| `data.data[].share_count` | Number of times the post was shared. |
| `data.data[].play_count / view_count / impression_count` | Counts of plays, views and impressions for the post. In the sample, `impression_count` is the largest and `play_count` is the smallest of the three. |
| `data.data[].go_detail_count` | Count of times viewers went to the post's detail page. |
| `data.data[].reward_count` | Number of rewards the post received. |
| `data.data[].digg_counts[]` | Like counts split by type. Each row has a `digg_count` and a `digg_type`. In the sample, type `10` holds 16560 and type `20` holds 1. |
| `data.data[].ward_info.ward_count` | Number of wards on the post. |
| `data.data[].ward_info.ward_users[].avatar.url_list[].url` | Avatar image URLs of users listed in `ward_users`. |

### Notes

- Get `cell_id` from the post share link. It is the same as the video ID.
- `bury_count` returns `-1` in the sample, which means no usable value was returned.
- The response holds one object inside `data.data`, so read the first item of the list.
- To get the post's text, media and author, call [Pipixia Post Detail](/apis/pipixia/app/post-detail). To read its comments, call [Pipixia Post Comments](/apis/pipixia/app/post-comment-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/post-statistics.json`](../../../../catalog/models/pipixia/app/post-statistics.json) · Store page: https://www.sandbase.ai/model/pipixia/app/post-statistics
