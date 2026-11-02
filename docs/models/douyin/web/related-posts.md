# Douyin Related Posts Recommendations API: pricing, parameters and code examples

`douyin/web/related-posts` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended related posts for a specific Douyin video. Supports pagination using a refresh index and customizable post count limits.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/related-posts", "aweme_id": "7393365489105358132"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/related-posts', {'aweme_id': '7393365489105358132'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/related-posts", {
  "aweme_id": "7393365489105358132"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/related-posts", sandbase.Params{
	"aweme_id": "7393365489105358132",
})
```

Same call via the path form: `POST /v1/api/douyin/web/related-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, default is 20, it is recommended to keep it unchanged. default `20` |
| `aweme_id` | string | yes | Video id  |
| `refresh_index` | integer |  | Paging index, default is 1, then increase by 1 each time for paging. default `1` |

## Details

Returns recommended related Douyin posts based on a target video specified by `aweme_id`. Paginate through sequential recommendations using `refresh_index`.

### Use cases

- Discover recommended Douyin videos related to a specific post.
- Build content recommendation feeds based on video context.
- Retrieve sequential batches of related Douyin video suggestions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/related-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7393365489105358132"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `count` | integer | No | Number, default is 20, it is recommended to keep it unchanged. |
| `refresh_index` | integer | No | Paging index, default is 1, then increase by 1 each time for paging. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_list": [
    {
      "video": {
        "bit_rate": [
          {
            "bit_rate": 1048328,
            "gear_name": "normal_1080_0",
            "quality_type": 1
          }
        ]
      }
    }
  ]
}
```

### Notes

- Provide the target video ID in `aweme_id`.
- Paginate through results by incrementing `refresh_index` by 1, starting at 1.
- The default value for `count` is 20.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/related-posts.json`](../../../../catalog/models/douyin/web/related-posts.json) · Store page: https://www.sandbase.ai/model/douyin/web/related-posts
