# Pipixia User Post List API: pricing, parameters and code examples

`pipixia/app/user-post-list` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of posts, including videos and photos, for a specified user profile. Supports pagination via cursor and feed count parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/user-post-list", "user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/user-post-list', {'user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/user-post-list", {
  "user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/user-post-list", sandbase.Params{
	"user_id": "example",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/user-post-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page.  |
| `user_id` | string | yes | AKA user id, can be obtained from the share link.  |
| `feed_count` | string |  | Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on.  |

## Details

Returns a page of posts, such as videos and photos, from one Pipixia user profile. It needs a `user_id`, which you can take from the profile share link.

### Use cases

- Show a creator's recent Pipixia posts in an external dashboard.
- Check which hashtags a creator's recent posts are tagged with.
- Collect post IDs and publish times for a creator to build an archive.
- Page through a creator's full post history with the returned cursor.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/user-post-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3602444694069495"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | AKA user id, can be obtained from the share link. |
| `cursor` | string | No | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. |
| `feed_count` | string | No | Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "compilation_list": [],
    "cursor": {
      "feed_len": 0,
      "has_more": true,
      "loadmore_cursor": 1793507806316341,
      "previous_cursor": null,
      "refresh_cursor": 0
    },
    "data": [
      {
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
        "cell_id": 7703195169469765938,
        "cell_id_str": "7703195169469765938",
        "cell_type": 1,
        "city_name": "湖北",
        "club_info": null
      }
    ],
    "index": null,
    "play_sound": true
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691717937
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.data[]` | One post card in the user's feed. Each entry holds the post, its hashtag and display details. |
| `data.data[].cell_id_str` | Post ID as a string. It matches `pass_through` and `item.ancestor_id` for the same post. Use the string form to avoid number rounding. |
| `data.data[].cell_type` | Numeric type of the card. Every card in this sample has the value `1`. |
| `data.data[].display_time` | Unix timestamp in seconds for when the post is shown in the feed. |
| `data.data[].city_name` | City or region name attached to the post, for example `湖北`. |
| `data.data[].hashtag.base_hashtag.activity_icon.name` | Name shown on the hashtag's activity icon, for example `追剧不能停`. |
| `data.data[].hashtag.base_hashtag.category_list[].name` | Category name of the hashtag, for example `影视娱乐`. |
| `data.data[].hashtag.enter_num / data.data[].hashtag.followers_num` | Counts for the hashtag attached to the post: `enter_num` and `followers_num`. |
| `data.cursor.has_more` | Shows whether another page is available. |
| `data.cursor.loadmore_cursor` | Cursor value to send as `cursor` to get the next page. |

### Notes

- Get `user_id` from the user's share link. If you only have a short link, use [Pipixia Short URL Conversion](/apis/pipixia/app/short-url) first.
- For the next page, pass `data.cursor.loadmore_cursor` as `cursor` and raise `feed_count` by 1. The first page uses `0` for both.
- Many fields in each card, such as `ad_info` and `live_info`, are `null` for ordinary posts.
- Call [Pipixia Post Detail](/apis/pipixia/app/post-detail) to look up a single post, or [Pipixia User Information](/apis/pipixia/app/user-info) for the profile itself.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/user-post-list.json`](../../../../catalog/models/pipixia/app/user-post-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/user-post-list
