# Youku Video Search

`youku/search-video` · api · Youku

Search Youku videos by keyword with page-based pagination. Use it to discover videos related to a topic, title, creator, or other search term.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youku/search-video", "keyword": "电影"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youku/search-video', {'keyword': '电影'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youku/search-video", {
  "keyword": "电影"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youku/search-video", sandbase.Params{
	"keyword": "电影",
})
```

Same call via the path form: `POST /v1/api/youku/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination, starting from 1. default `1` |
| `keyword` | string | yes | Keyword to search for.  |

## Details

Search Youku videos by keyword with page-based pagination. Use it to discover videos related to a topic, title, creator, or other search term.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youku/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "电影"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword to search for. |
| `page` | integer | No | Page number for pagination, starting from 1. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/youku/search-video.json`](../../../catalog/models/youku/search-video.json) · Store page: https://www.sandbase.ai/model/youku/search-video
