# Douyin Hashtag Video List API: pricing, parameters and code examples

`douyin/app-v3/hashtag-video-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of videos associated with a specific Douyin hashtag. Supports sorting by comprehensive rank, most likes, or latest release along with cursor pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/hashtag-video-list", "ch_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/hashtag-video-list', {'ch_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/hashtag-video-list", {
  "ch_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/hashtag-video-list", sandbase.Params{
	"ch_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/hashtag-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ch_id` | string | yes | Hashtag id  |
| `count` | integer |  | Number Please keep the default, otherwise there will be BUG.  |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.  |
| `sort_type` | integer |  | 0: Comprehensive sorting 1: Most likes 2: Latest release  |

## Details

Query videos linked to a specific Douyin topic using `ch_id`. You can sort results by popularity or date using `sort_type` and paginate through feeds with `cursor`.

### Use cases

- Track video submissions and trends under a specific Douyin hashtag.
- Monitor top-liked video content for competitive topic research.
- Retrieve the latest public posts associated with a campaign hashtag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/hashtag-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ch_id": "1575791821492238"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ch_id` | string | Yes | Hashtag id |
| `count` | integer | No | Number Please keep the default, otherwise there will be BUG. |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |
| `sort_type` | integer | No | 0: Comprehensive sorting 1: Most likes 2: Latest release |

### Notes

- Set `cursor` to 0 for the first page, then use the cursor value returned in the response for subsequent pages.
- Set `sort_type` to 0 for comprehensive sorting, 1 for most likes, or 2 for latest release.
- It is recommended to keep `count` at its default value to prevent errors.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/hashtag-video-list.json`](../../../../catalog/models/douyin/app-v3/hashtag-video-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/hashtag-video-list
