# Toutiao Web Keyword Search API: pricing, parameters and code examples

`toutiao/search` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.071429 per call · **Modes:** sync

Search Toutiao web articles by keyword. Use it to discover relevant articles for topic research, media monitoring, or source collection.

## Pricing

- **$0.071429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/search", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/search', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/search", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/search", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/toutiao/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword or query.  |

## Details

Returns a list of Toutiao web search results for a keyword. Each result has a title, summary, author name, article type and link. The only input is `keyword`.

### Use cases

- Collect article links and titles about a topic such as `人工智能` for research.
- Track which sources and authors appear in Toutiao results for a brand or term.
- Build a source list for a topic, then fetch full article details for each link.
- Scan result summaries to see how a keyword is described across different sites.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword or query. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "list": [
    {
      "作者名称": "vivo智能手机官方网站",
      "发表时间": null,
      "搜索关键词": "人工智能",
      "收藏量": null,
      "文章摘要": "手机领域的国际化品牌,vivo官网提供手机资讯、售前咨询、在线购买、售后服务等功能;vivo当季明星机型有X300系列、S50系列、X Fold5、iQOO 1…",
      "文章标题": "vivo智能手机官方网站 - S50系列 长焦Live神器",
      "文章类型": "头条文章",
      "文章链接": "https://www.vivo.com.cn/upgrade/detail?modelId=285",
      "点赞量": null,
      "评论量": null,
      "阅读量": null
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `list[]` | One search result. The response is a list of these objects. |
| `list[].文章标题` | Title of the result. |
| `list[].文章摘要` | Short summary text of the result. Long summaries are cut off with `...`. |
| `list[].文章链接` | URL of the result. In the sample it points to an external web page, such as a company site. |
| `list[].作者名称` | Author or publisher name shown for the result. |
| `list[].文章类型` | Type label of the result. The sample values are `头条文章`. |
| `list[].搜索关键词` | The keyword that produced this result. It echoes the `keyword` input. |
| `list[].阅读量 / 点赞量 / 评论量 / 收藏量` | Read, like, comment and favorite counts. All are `null` in the sample, so do not rely on them being filled. |
| `list[].发表时间` | Publish time. It is `null` in the sample. |

### Notes

- The `keyword` parameter is required and accepts Chinese text, for example `人工智能`.
- The request has no pagination parameter, so each call takes only `keyword`.
- Field names in the response are in Chinese and appear exactly as shown in the table above.
- To get more detail on a result, use [Toutiao Article Details (Web)](/apis/toutiao/web/article-info) with the article link.

### Pricing

$0.071429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/toutiao/search.json`](../../../catalog/models/toutiao/search.json) · Store page: https://www.sandbase.ai/model/toutiao/search
