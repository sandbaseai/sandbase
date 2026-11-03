# Pipixia Post Comments API: pricing, parameters and code examples

`pipixia/app/post-comment-list` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comments for a Pipixia post using its video identifier. Supports cursor-based pagination and cell type filtering to browse feedback.

## Pricing

- **$0.001 per call** (USD)
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

Returns a page of comment entries for a Pipixia post. The only required input is the post's video identifier, passed as `cell_id`.

### Use cases

- Page through the comments on a Pipixia video to review audience feedback.
- Read the total comment count of a post from `data.count`.
- Sort comments by `comment_info.create_time` to build a timeline of when viewers reacted.
- Group comments by `city_name` to see which regions the commenters come from.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/post-comment-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cell_id": "7411193113223371043"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cell_id` | string | Yes | AKA video id, can be obtained from the share link. |
| `cell_type` | integer | No | Video type, 1 for video, keep the default value for other types. |
| `offset` | string | No | Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "cell_comments": [
      {
        "board_info": {
          "block_type": 12,
          "god_rank": -1
        },
        "cell_id": 7411241327297299263,
        "cell_id_str": "7411241327297299263",
        "cell_type": 8,
        "city_name": "河南",
        "comment_info": {
          "bds_origin_type": 1,
          "bury_count": -1,
          "can_delete": false,
          "can_download": true,
          "comment_count": 1088,
          "comment_id": 7411241327297299263,
          "comment_id_str": "7411241327297299263",
          "create_time": 1725564088
        },
        "display_time": 1725564088,
        "last_view_time": 0,
        "pass_through": "{\"cell_id_str\":\"7411241327297299263\",\"cell_type\":\"8\"}",
        "stickup": false
      }
    ],
    "count": 1088,
    "has_more": true,
    "offset": 10,
    "user_send_god_type": 0
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691711920
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.cell_comments[]` | One comment entry in the current page. |
| `data.cell_comments[].comment_info.comment_id / comment_id_str` | Identifier of the comment, as a number and as a string. Use the string form to avoid number precision loss. |
| `data.cell_comments[].comment_info.create_time / display_time` | Unix timestamps in seconds for when the comment was created and shown. |
| `data.cell_comments[].city_name` | Location name attached to the comment, such as a province. |
| `data.cell_comments[].comment_info.comment_count` | Count value attached to the comment. In this response it equals `data.count` on every item. |
| `data.cell_comments[].comment_info.bury_count` | Bury count of the comment. The value `-1` appears in this response. |
| `data.cell_comments[].stickup` | Boolean that shows whether the comment is pinned. |
| `data.cell_comments[].comment_info.can_delete / can_download` | Boolean flags for whether the comment can be deleted or downloaded. |
| `data.count` | Total number of comments reported for the post. |
| `data.has_more / offset` | `has_more` shows whether more pages exist. `offset` is the cursor for the next page. |

### Notes

- Get `cell_id` from the post share link. [Pipixia Short URL Conversion](/apis/pipixia/app/short-url) can help turn a short link into a usable identifier.
- For the next page, send the `data.offset` value from the previous response as `offset`. Stop when `data.has_more` is `false`.
- Keep `cell_type` at its default of `1` for videos.
- Call [Pipixia Post Detail](/apis/pipixia/app/post-detail) to see details of the post itself.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/post-comment-list.json`](../../../../catalog/models/pipixia/app/post-comment-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/post-comment-list
