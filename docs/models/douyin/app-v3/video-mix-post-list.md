# Douyin Video Mix Post List

`douyin/app-v3/video-mix-post-list` · api · Douyin

Returns a list of video posts belonging to a specific Douyin video compilation or mix. Query by mix_id with cursor-based pagination to retrieve post details and metadata.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/video-mix-post-list", "mix_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/video-mix-post-list', {'mix_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/video-mix-post-list", {
  "mix_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/video-mix-post-list", sandbase.Params{
	"mix_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/video-mix-post-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number Please keep the default, otherwise there will be BUG.  |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.  |
| `mix_id` | string | yes | Mix id  |

## Details

Retrieve video posts included in a Douyin mix playlist by supplying `mix_id`. Supports sequential paging using `cursor`.

### Use cases

- Retrieve all videos compiled under a specific Douyin mix.
- Track sequential episodes or series posted within a collection.
- Extract video identifiers and metadata for a curated playlist.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-mix-post-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mix_id": "7384792941870450726"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mix_id` | string | Yes | Mix id |
| `count` | integer | No | Number Please keep the default, otherwise there will be BUG. |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_list": [
    {
      "activity_video_type": -1,
      "author_user_id": 2557909361237356,
      "aweme_id": "7384478157656673562",
      "aweme_type": 0,
      "bodydance_score": 0,
      "boost_status": 0,
      "caption_template_id": 0,
      "cf_assets_type": 0,
      "create_time": 1719332130,
      "desc": "变量的大小为何很重要？ #编程 #编译原理",
      "admire_auth": {
        "author_can_admire": 0
      },
      "ancestor_info": {
        "product_id": 32
      },
      "author": {
        "apple_account": 0,
        "authority_status": 0,
        "aweme_count": 103,
        "close_friend_type": 0,
        "comment_filter_status": 0,
        "contacts_status": 2
      },
      "comment_permission_info": {
        "comment_permission_status": 0
      }
    }
  ]
}
```

### Notes

- Use `cursor` for pagination, starting with 0 on the first call and passing the cursor value returned in the prior response.
- Keep `count` at its default value to avoid unexpected issues.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-mix-post-list.json`](../../../../catalog/models/douyin/app-v3/video-mix-post-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-mix-post-list
