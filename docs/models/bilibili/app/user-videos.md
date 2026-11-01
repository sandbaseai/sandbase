# Bilibili User Videos

`bilibili/app/user-videos` · api · Bilibili

Returns uploaded video listings for a specified Bilibili creator account. Supports pagination controls and filtering by post types such as archives or seasons.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/user-videos", "page": 1, "post_filter": "archive", "ps": 20, "user_id": "203680252"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/user-videos', {'page': 1, 'post_filter': 'archive', 'ps': 20, 'user_id': '203680252'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/user-videos", {
  "page": 1,
  "post_filter": "archive",
  "ps": 20,
  "user_id": "203680252"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/user-videos", sandbase.Params{
	"page": 1,
	"post_filter": "archive",
	"ps": 20,
	"user_id": "203680252",
})
```

Same call via the path form: `POST /v1/api/bilibili/app/user-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ps` | integer |  | Page size default `20` |
| `page` | integer |  | Page number default `1` |
| `user_id` | string | yes | User ID (required)  |
| `post_filter` | string |  | Filter type (archive/season/contribute) default `"archive"` |

## Details

Retrieve a list of video uploads from a creator using their `user_id`. You can also filter the results by content type and paginate through records.

### Use cases

- Track recent video uploads from specific Bilibili creators.
- Catalog channel content by archive, season, or contribution type.
- Collect video metadata including duration, view counts, and category tags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/user-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "203680252"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID (required) |
| `ps` | integer | No | Page size |
| `page` | integer | No | Page number |
| `post_filter` | string | No | Filter type (archive/season/contribute) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "item": [
      {
        "author": "AYCS2",
        "ctime": 1790748319,
        "duration": 1171,
        "publish_time_text": "9月30日",
        "title": "老Y蜜月之旅 | 马尔代夫菲诺芙",
        "tname": "出行",
        "view_content": "17万",
        "view_self_type": 0
      }
    ]
  }
}
```

### Notes

- Filter content types using `post_filter` with values such as archive, season, or contribute.
- Control pagination with the `page` and `ps` parameters.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili App Bangumi Tab](/model/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/model/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/model/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/user-videos.json`](../../../../catalog/models/bilibili/app/user-videos.json) · Store page: https://www.sandbase.ai/model/bilibili/app/user-videos
