# Pipixia Post Comments API: pricing, parameters and code examples

`pipixia/app/post-comment-list` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns comments for a Pipixia post using its video identifier. Supports cursor-based pagination and cell type filtering to browse feedback.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/post-comment-list", "cell_id": "7411193113223371043", "cell_type": 1, "offset": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/post-comment-list', {'cell_id': '7411193113223371043', 'cell_type': 1, 'offset': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/post-comment-list", {
  "cell_id": "7411193113223371043",
  "cell_type": 1,
  "offset": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/post-comment-list", sandbase.Params{
	"cell_id": "7411193113223371043",
	"cell_type": 1,
	"offset": "0",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/post-comment-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | string |  | Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. default `"0"` |
| `cell_id` | string | yes | AKA video id, can be obtained from the share link.  |
| `cell_type` | integer |  | Video type, 1 for video, keep the default value for other types. default `1` |

## Details

Retrieve audience discussions on a post by providing its `cell_id`. Use `offset` to page through the comment list.

### Use cases

- Read audience feedback on Pipixia posts.
- Track comment volume and engagement on video content.
- Archive user reactions for social media analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/post-comment-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cell_id": "7411193113223371043"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cell_id` | string | Yes | AKA video id, can be obtained from the share link. |
| `offset` | string | No | Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. |
| `cell_type` | integer | No | Video type, 1 for video, keep the default value for other types. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "cell_comments": [
      {
        "cell_id": 7411241327297299263,
        "cell_id_str": "7411241327297299263",
        "cell_type": 8,
        "city_name": "河南",
        "display_time": 1725564088,
        "last_view_time": 0,
        "board_info": {
          "block_type": 12,
          "god_rank": -1
        },
        "comment_info": {
          "bds_origin_type": 1,
          "bury_count": -1,
          "comment_count": 1088,
          "comment_id": 7411241327297299263,
          "comment_id_str": "7411241327297299263",
          "create_time": 1725564088
        }
      }
    ]
  }
}
```

### Notes

- The `cell_id` corresponds to the video ID and can be obtained from the post share link.
- Set `offset` to the value returned in the previous response page to fetch the next set of comments.
- Set `cell_type` to 1 for video posts, or leave default for other types.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/model/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/model/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/model/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/post-comment-list.json`](../../../../catalog/models/pipixia/app/post-comment-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/post-comment-list
