# Pipixia User Post List API: pricing, parameters and code examples

`pipixia/app/user-post-list` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a list of posts, including videos and photos, for a specified user profile. Supports pagination via cursor and feed count parameters.

## Pricing

- **$0.0015 per call** (USD)
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

Retrieve post feeds from a specified user profile using `user_id`. Pagination is supported using `cursor` and `feed_count`.

### Use cases

- Display a user's uploaded videos and photos within an external dashboard.
- Track engagement metrics and recent posts for specific creators.
- Archive media items and post text from target Pipixia accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/user-post-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3602444694069495"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | AKA user id, can be obtained from the share link. |
| `cursor` | string | No | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. |
| `feed_count` | string | No | Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "data": [
      {
        "cell_id": 7692668426287847734,
        "cell_id_str": "7692668426287847734",
        "cell_type": 1,
        "city_name": "湖北",
        "display_time": 1791088941,
        "last_view_time": 0,
        "board_info": {
          "block_type": 12,
          "god_rank": -1
        },
        "hashtag": {
          "enter_num": 21002280,
          "followers_num": 227517,
          "works_num": 823422
        },
        "item": {
          "ancestor_id": "7692668426287847734",
          "content": "何亮已经到要给娟儿姐报备的程度了！",
          "create_time": 1791088941,
          "duration": 22.87,
          "item_cell_type": 1,
          "item_id": 7692668426287847734
        }
      }
    ]
  }
}
```

### Notes

- `user_id` can be obtained from the account share link.
- Set `cursor` using the `loadmore_cursor` value from the previous page, defaulting to 0.
- Increment `feed_count` by 1 for each subsequent page, starting at 0.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/model/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/model/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/model/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/user-post-list.json`](../../../../catalog/models/pipixia/app/user-post-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/user-post-list
