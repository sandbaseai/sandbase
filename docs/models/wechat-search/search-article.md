# WeChat Article Search API: pricing, parameters and code examples

`wechat-search/search-article` · data API · WeChat Search · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.111111 per call · **Modes:** sync

Search WeChat Official Account articles by keyword with publish-time and sort filters plus page, offset, and continuation-state pagination.

## Pricing

- **$0.111111 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-search/search-article", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-search/search-article', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-search/search-article", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-search/search-article", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-search/search-article` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Search result offset returned by the previous response. Use 0 for the first page. default `0` |
| `keyword` | string | yes | Search keyword for WeChat Official Account articles.  |
| `sortType` | string |  | Sort order for WeChat Official Account article web search results. one of: `COMPREHENSIVE`, `LATEST`, `HOT`; default `"COMPREHENSIVE"` |
| `currentPage` | integer |  | Current page number starting from 1 for WeChat web search pagination. default `1` |
| `publishTimeType` | string |  | Publish time filter for WeChat Official Account article web search. one of: `ALL`, `ONE_DAY`, `SEVEN_DAYS`, `HALF_YEAR`; default `"ALL"` |

## Details

Search WeChat Official Account articles by keyword with publish-time and sort filters plus page, offset, and continuation-state pagination.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-search/search-article" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword for WeChat Official Account articles. |
| `publishTimeType` | string | No | Publish time filter for WeChat Official Account article web search. |
| `sortType` | string | No | Sort order for WeChat Official Account article web search results. |
| `currentPage` | integer | No | Current page number starting from 1 for WeChat web search pagination. |
| `offset` | integer | No | Search result offset returned by the previous response. Use 0 for the first page. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-search/search-article.json`](../../../catalog/models/wechat-search/search-article.json) · Store page: https://www.sandbase.ai/model/wechat-search/search-article
