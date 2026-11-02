# Zhihu Salt Content Search API: pricing, parameters and code examples

`zhihu/web/salt-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns Zhihu Salt column and chapter search results matching a specified keyword. Supports pagination with offset and limit parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/salt-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/salt-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/salt-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/salt-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/salt-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of contents per page default `"20"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `search_hash_id` | string |  | Search Hash ID default `""` |

## Details

Retrieve Zhihu Salt market search results by providing a query term in `keyword`.

### Use cases

- Search Zhihu Salt stories and column chapters by keyword.
- Browse market content catalogs and chapter links programmatically.
- Paginate through Salt search results using custom limit and offset values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/salt-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of contents per page |
| `offset` | string | No | Offset |
| `search_hash_id` | string | No | Search Hash ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "id": 1911116557708399705,
      "type": "knowledge_ad",
      "object": {
        "commodity_id": "1911116557708399705",
        "commodity_type": "paid_column_chapter",
        "sku_id": "1911116568743638150",
        "slave_url": "https://www.zhihu.com/market/paid_column/1910478282010363787/section/19111165577…",
        "tab_type": "album_all",
        "url": "https://www.zhihu.com/market/paid_column/1910478282010363787/section/19111165577…"
      }
    }
  ]
}
```

### Notes

- Use `limit` and `offset` to paginate through search results.
- Pass `search_hash_id` when tracking a specific search session.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/salt-search-v3.json`](../../../../catalog/models/zhihu/web/salt-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/salt-search-v3
