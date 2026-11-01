# Zhihu Video List

`zhihu/web/video-list` · api · Zhihu

Retrieves a paginated list of videos from the Zhihu web platform. Supports pagination controls through page size and offset index parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/video-list", "limit": "12", "offset": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/video-list', {'limit': '12', 'offset': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/video-list", {
  "limit": "12",
  "offset": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/video-list", sandbase.Params{
	"limit": "12",
	"offset": "0",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of videos per page default `"12"` |
| `offset` | string |  | Offset default `"0"` |

## Details

Retrieve a collection of video entries from Zhihu by specifying pagination parameters including `limit` and `offset`.

### Use cases

- Browse video feeds from Zhihu for media tracking.
- Paginate through video listings for content analysis.
- Integrate Zhihu video entries into external dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | string | No | Number of videos per page |
| `offset` | string | No | Offset |

### Notes

- Use `limit` to control the number of videos returned per page.
- Use `offset` to manage list pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/video-list.json`](../../../../catalog/models/zhihu/web/video-list.json) · Store page: https://www.sandbase.ai/model/zhihu/web/video-list
