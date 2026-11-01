# Xiaohongshu (RED) Search Suggestions

`xiaohongshu/web-v3/search-suggest` · api · Xiaohongshu

Returns search query suggestions and autocomplete terms from Xiaohongshu (RED). Accepts an optional search query prefix to surface matching keyword recommendations.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/web-v3/search-suggest", "keyword": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/web-v3/search-suggest', {'keyword': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/web-v3/search-suggest", {
  "keyword": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/web-v3/search-suggest", sandbase.Params{
	"keyword": "",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/web-v3/search-suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Keyword (optional) default `""` |

## Details

Look up query suggestions on Xiaohongshu (RED) using an optional `keyword` prefix to retrieve matching search terms.

### Use cases

- Power autocomplete and search assistance in user-facing search inputs.
- Discover related keywords and query ideas on Xiaohongshu (RED).
- Analyze popular search terms associated with specific brands or topics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/web-v3/search-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Keyword (optional) |

### Notes

- The `keyword` parameter is optional and accepts search prefixes or query terms.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Homepage Feed](/model/xiaohongshu/web-v3/homefeed): Retrieves recommended notes from the Xiaohongshu homepage feed.
- [Xiaohongshu (RED) Homepage Categories](/model/xiaohongshu/web-v3/homefeed-categories): Returns a list of available homefeed category channels on Xiaohongshu (RED).
- [Xiaohongshu (RED) Web Note Details](/model/xiaohongshu/web-v3/note-detail): Returns detailed information for a specific Xiaohongshu note using its identifier and security token obtained from a web share link.

---
Machine-readable: [`catalog/models/xiaohongshu/web-v3/search-suggest.json`](../../../../catalog/models/xiaohongshu/web-v3/search-suggest.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/web-v3/search-suggest
