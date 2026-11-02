# Pipixia Hashtag Post List API: pricing, parameters and code examples

`pipixia/app/hashtag-post-list` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of posts associated with a specific hashtag on Pipixia. Filter by hashtag identifier, sort options, and paginate through results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/hashtag-post-list", "hashtag_id": "129559"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/hashtag-post-list', {'hashtag_id': '129559'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/hashtag-post-list", {
  "hashtag_id": "129559"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/hashtag-post-list", sandbase.Params{
	"hashtag_id": "129559",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/hashtag-post-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. default `"0"` |
| `feed_count` | string |  | Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. default `"0"` |
| `hashtag_id` | string | yes | AKA hashtag id, can be obtained from the share link.  |
| `hashtag_sort_type` | string |  | Hashtag sort type default `"3"` |
| `hashtag_request_type` | string |  | Hashtag request type default `"0"` |

## Details

Retrieve posts under a specific topic using `hashtag_id`. Supports pagination via `cursor` and `feed_count`.

### Use cases

- Monitor user-generated posts filed under specific Pipixia hashtags.
- Track trending discussions and post volume for selected topic tags.
- Extract video post details and hashtag engagement metrics over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/hashtag-post-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag_id": "129559"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag_id` | string | Yes | AKA hashtag id, can be obtained from the share link. |
| `cursor` | string | No | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. |
| `feed_count` | string | No | Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the second page, 2 for the third page, and so on. |
| `hashtag_sort_type` | string | No | Hashtag sort type |
| `hashtag_request_type` | string | No | Hashtag request type |

### Notes

- Provide `hashtag_id` extracted from the Pipixia share link.
- Use `cursor` taken from the previous response `loadmore_cursor` for pagination.
- Increment `feed_count` by 1 for each subsequent page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/model/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia App Home Feed](/model/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.
- [Pipixia Home Short Drama Feed](/model/pipixia/app/home-short-drama-feed): Returns short drama and novel recommendations from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/hashtag-post-list.json`](../../../../catalog/models/pipixia/app/hashtag-post-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/hashtag-post-list
