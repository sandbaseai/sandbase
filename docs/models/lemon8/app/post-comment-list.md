# Lemon8 Post Comments List API: pricing, parameters and code examples

`lemon8/app/post-comment-list` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves the list of comments for a specific Lemon8 post. Requires the post item ID, group ID, and media ID with support for paginated results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/post-comment-list", "group_id": "7361926875709129222", "item_id": "7361926875709129222", "media_id": "7428056850216862763"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/post-comment-list', {'group_id': '7361926875709129222', 'item_id': '7361926875709129222', 'media_id': '7428056850216862763'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/post-comment-list", {
  "group_id": "7361926875709129222",
  "item_id": "7361926875709129222",
  "media_id": "7428056850216862763"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/post-comment-list", sandbase.Params{
	"group_id": "7361926875709129222",
	"item_id": "7361926875709129222",
	"media_id": "7428056850216862763",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/post-comment-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | string |  | Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the offset returned by the last request is used for subsequent requests. default `"0"` |
| `item_id` | string | yes | Post's item_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` or `/lemon8/app/get_item_id`  |
| `group_id` | string | yes | Post's group_id, can be obtained from the interface `/lemon8/app/fetch_post_detail`  |
| `media_id` | string | yes | Post's media_id, can be obtained from the interface `/lemon8/app/fetch_post_detail`  |

## Details

Retrieves comments for a specific post on Lemon8 using `item_id`, `group_id`, and `media_id`. Supports pagination via `offset`.

### Use cases

- Retrieve audience feedback and discussions from specific Lemon8 posts.
- Track engagement trends across user comments over time.
- Collect comment data for community sentiment analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/post-comment-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"group_id": "7361926875709129222", "item_id": "7361926875709129222", "media_id": "7428056850216862763"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Post's item_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` or `/lemon8/app/get_item_id` |
| `group_id` | string | Yes | Post's group_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` |
| `media_id` | string | Yes | Post's media_id, can be obtained from the interface `/lemon8/app/fetch_post_detail` |
| `offset` | string | No | Pagination parameter, can be obtained from the return result of the last request. |

### Notes

- Obtain `item_id`, `group_id`, and `media_id` from the post details endpoint.
- Leave `offset` empty on the initial request, then pass the offset returned in the previous response for pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Banners](/model/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/model/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/model/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/post-comment-list.json`](../../../../catalog/models/lemon8/app/post-comment-list.json) · Store page: https://www.sandbase.ai/model/lemon8/app/post-comment-list
