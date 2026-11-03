# Pipixia Search API: pricing, parameters and code examples

`pipixia/app/search` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Pipixia (ByteDance humor community) by keyword across posts, videos, images, users and hashtags.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/search", "keyword": "OpenAI", "offset": "0", "search_type": "1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/search', {'keyword': 'OpenAI', 'offset': '0', 'search_type': '1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/search", {
  "keyword": "OpenAI",
  "offset": "0",
  "search_type": "1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/search", sandbase.Params{
	"keyword": "OpenAI",
	"offset": "0",
	"search_type": "1",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | string |  | Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. default `"0"` |
| `keyword` | string | yes | Search keyword.  |
| `search_type` | string |  | Search type, available values are as follows: 1: Comprehensive; 8: Hot; 9: Fresh; 2: Video; 3: Photo; 4: User; 5: Hashtag default `"1"` |

## Details

Searches Pipixia, the ByteDance humor community, for a keyword and returns a list of result cells. Each cell can hold a post, a hashtag or a group of users. The only required input is `keyword`.

### Use cases

- Collect posts that match a keyword such as a topic or brand name.
- Find user accounts that appear for a keyword and read their avatars and age text.
- Discover hashtags related to a keyword and check their `enter_num` and `followers_num` counts.
- Page through results with `offset` to build a larger set of posts on one topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `offset` | string | No | Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. |
| `search_type` | string | No | Search type, available values are as follows: 1: Comprehensive; 8: Hot; 9: Fresh; 2: Video; 3: Photo; 4: User; 5: Hashtag |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "correct_query": "",
    "data": [
      {
        "ad_info": null,
        "album_info": null,
        "banner_info": null,
        "block_info": null,
        "board_info": null,
        "button": null,
        "card_item": null,
        "cell_id": 3106651107666071,
        "cell_id_str": "3106651107666071",
        "cell_type": 7,
        "city_name": null,
        "club_info": null
      }
    ],
    "has_more": true,
    "middleground": true,
    "real_count": 20,
    "user_id": null,
    "user_id_str": null
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691715421
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.data[]` | One result cell. Check `cell_type` to see what the cell holds, then read the matching object such as `item`, `hashtag` or `users_hashtag`. |
| `data.data[].cell_id_str` | ID of the cell as a string. For post cells it matches `item.ancestor_id` in the sample. |
| `data.data[].cell_type` | Number that tells the cell kind. The sample shows `1` for cells with an `item` and `7` for a cell with `users_hashtag`. |
| `data.data[].display_time` | Time value for the cell. The sample values look like Unix seconds. |
| `data.data[].city_name` | Region name attached to the cell, for example `江苏`. It is `null` when absent. |
| `data.data[].item.aha_image[]` | Image objects for a post. Each one has `uri`, `width`, `height`, `is_gif`, and lists of image URLs in `url_list` and `download_list`. |
| `data.data[].hashtag.enter_num / data.data[].hashtag.followers_num` | Counts for a hashtag attached to a result. `enter_num` is a total count and `followers_num` is the follower count. |
| `data.data[].hashtag.base_hashtag.category_list[].name` | Category name of the hashtag, for example `搞笑区`. |
| `data.data[].users_hashtag.users[]` | Users matched by the keyword. Each row has `age`, `article_count`, `achievements` and an `avatar` image object. |
| `data.data[].search_attach_info` | JSON string with extra search tracking data for the user and hashtag blocks. |

### Notes

- Set `search_type` to `1` (mixed results), `8` (hot), `9` (fresh), `2` (video), `3` (photo), `4` (user) or `5` (hashtag). The default is `1`.
- For the next page, pass the `offset` value from the previous response. The first page uses `0`.
- Many fields in each cell are `null`. Only the object that matches `cell_type` is filled.
- To get full data for a result, call [Pipixia Post Detail](/apis/pipixia/app/post-detail), [Pipixia User Information](/apis/pipixia/app/user-info) or [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hot Search](/apis/pipixia/app/hot-search-board-list): Get the Pipixia hot search boards: trending posts with daily likes and top comments.
- [Get hashtag detail](/apis/pipixia/app/hashtag-detail): Get hashtag detail data.
- [Get hashtag post list](/apis/pipixia/app/hashtag-post-list): Get hashtag post list data.

---
Machine-readable: [`catalog/models/pipixia/app/search.json`](../../../../catalog/models/pipixia/app/search.json) · Store page: https://www.sandbase.ai/model/pipixia/app/search
