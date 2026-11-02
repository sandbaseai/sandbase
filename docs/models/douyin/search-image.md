# Douyin Image Post Search API: pricing, parameters and code examples

`douyin/search-image` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Search Douyin (TikTok China) image posts by keyword with search-session pagination. Omit searchId for the first page, then use the search ID from the previous response to continue.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search-image", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search-image', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search-image", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search-image", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/douyin/search-image` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | The search keyword.  |
| `searchId` | string |  | Search ID returned by the previous response. Leave it empty for the first page.  |

## Details

Search Douyin (TikTok China) image posts by keyword with search-session pagination. Omit searchId for the first page, then use the search ID from the previous response to continue.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search-image" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The search keyword. |
| `searchId` | string | No | Search ID returned by the previous response. Leave it empty for the first page. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/search-image.json`](../../../catalog/models/douyin/search-image.json) · Store page: https://www.sandbase.ai/model/douyin/search-image
