# Pipixia Post Detail API: pricing, parameters and code examples

`pipixia/app/post-detail` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed data for a Pipixia post, including video and photo content, using a specific post identifier and optional post type.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/post-detail", "cell_id": "7411193113223371043"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/post-detail', {'cell_id': '7411193113223371043'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/post-detail", {
  "cell_id": "7411193113223371043"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/post-detail", sandbase.Params{
	"cell_id": "7411193113223371043",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cell_id` | string | yes | AKA video id, can be obtained from the share link.  |
| `cell_type` | integer |  | Video type, 1 for video, keep the default value for other types. default `1` |

## Details

Returns the detail record for one Pipixia post, including its hashtag, location label, display time and item media. It needs a `cell_id`, which is the post (video) ID, and accepts an optional `cell_type`.

### Use cases

- Look up the hashtag a Pipixia video belongs to, with its follower and visit counts.
- Convert a shared Pipixia link into a post record with its ID and publish time.
- Collect the thumbnail images attached to a post.
- Check which city or region label a post carries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/post-detail" \
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

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "data": {
      "ad_info": null,
      "album_info": null,
      "banner_info": null,
      "block_info": null,
      "board_info": {
        "block_type": 12,
        "god_rank": -1
      },
      "button": null,
      "card_item": null,
      "cell_id": 7411193113223371043,
      "cell_id_str": "7411193113223371043",
      "cell_type": 1,
      "city_name": "广东",
      "club_info": null
    }
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691712048
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.data.cell_id / data.data.cell_id_str` | The post ID as a number and as a string. Use the string version to avoid precision loss. |
| `data.data.cell_type` | The type of the returned cell. The value `1` matches the video type in the request parameter. |
| `data.data.display_time` | Time the post is shown, as a Unix timestamp in seconds. |
| `data.data.city_name` | Location label of the post, such as `广东`. |
| `data.data.hashtag.base_hashtag.atmosphere` | Short label text of the hashtag the post is attached to. |
| `data.data.hashtag.base_hashtag.category_list[].name` | Name of the category the hashtag belongs to, for example `同城生活`. |
| `data.data.hashtag.enter_num / data.data.hashtag.followers_num` | Counts for the hashtag. `enter_num` is the entry count and `followers_num` is the number of followers. |
| `data.data.hashtag.base_hashtag.avatars[].url_list[].url` | Image URLs for the hashtag avatars, each 200 by 200 pixels. |
| `data.data.item.aha_image[].url_list[].url` | Image URLs attached to the post item. Each entry also has `width`, `height` and `uri`. |
| `data.data.item.ancestor_id` | ID of the original post this item traces back to. It equals the requested `cell_id` here. |

### Notes

- Take `cell_id` from a Pipixia share link. Use [Pipixia Short URL Conversion](/apis/pipixia/app/short-url) if you only have a short link.
- Keep `cell_type` at its default of `1` for videos. Keep the default for other types too.
- Many fields, such as `comment`, `user_info` and `ad_info`, return `null` in this response.
- For engagement numbers and comments, call [Pipixia Post Statistics](/apis/pipixia/app/post-statistics) or [Pipixia Post Comments](/apis/pipixia/app/post-comment-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/post-detail.json`](../../../../catalog/models/pipixia/app/post-detail.json) · Store page: https://www.sandbase.ai/model/pipixia/app/post-detail
