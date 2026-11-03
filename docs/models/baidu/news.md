# Baidu News Search API: pricing, parameters and code examples

`baidu/news` · data API · Baidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Baidu News results for a keyword: headline, source, date, snippet and link.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "baidu/news", "q": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('baidu/news', {'q': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("baidu/news", {
  "q": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "baidu/news", sandbase.Params{
	"q": "coffee",
})
```

Same call via the path form: `POST /v1/api/baidu/news` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | q  |

## Details

This API returns Baidu News search results for a keyword. Each result has a headline, source name, relative date, snippet, link and thumbnail. It needs one input, `q`, the search keyword.

### Use cases

- Track how Chinese media cover a brand or product by searching its name.
- Collect recent headlines and article links on a topic for a news digest.
- Find related queries to expand a keyword list for media monitoring.
- Check which outlets publish stories about a subject by reading the `source` field.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/baidu/news" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | q |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "organic_results": [
    {
      "date": "8天前",
      "link": "https://baijiahao.baidu.com/s?id=1880085169863886735&wfr=spider&for=pc",
      "position": 1,
      "snippet": "近日，《中国100咖啡指南（2026）》正式发布，贵阳4个咖啡品牌入选。其中，来自贵阳的咖啡品牌——Captain George 风味博物馆（上海太原路店）位列…",
      "source": "贵阳发布",
      "thumbnail": "https://t8.baidu.com/it/u=1035183366,940297393&fm=3035&app=3035&size=f242,162&n=…",
      "title": "全国百佳,贵阳占4席!"
    }
  ],
  "pagination": {
    "current": 1,
    "next": "https://www.baidu.com/s?rtt=1&ie=utf-8&bsst=1&cl=2&wd=coffee&tn=news&x_bfe_rqs=0…",
    "other_pages": {
      "2": "https://www.baidu.com/s?rtt=1&ie=utf-8&bsst=1&cl=2&wd=coffee&tn=news&x_bfe_rqs=0…",
      "3": "https://www.baidu.com/s?rtt=1&ie=utf-8&bsst=1&cl=2&wd=coffee&tn=news&x_bfe_rqs=0…"
    }
  },
  "related_searches": [
    {
      "link": "https://www.baidu.com/s?rtt=1&ie=utf-8&bsst=1&cl=2&wd=luckincoffee&tn=news&x_bfe…",
      "query": "luckincoffee"
    }
  ],
  "search_information": {
    "total_results": 23
  },
  "top_searches": [
    {
      "link": "https://www.baidu.com/s?cl=2&wd=%E8%AE%A9%E6%AF%8D%E4%BA%B2%E6%B2%B3%E6%B0%B8%E7…",
      "position": 1,
      "text": "让母亲河永续惠泽子孙后代"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organic_results[].title` | Headline of the news article. |
| `organic_results[].link` | URL of the article. |
| `organic_results[].snippet` | Short text excerpt from the article. Long text is cut with an ellipsis. |
| `organic_results[].source` | Name of the outlet that published the article. |
| `organic_results[].date` | Publication time as shown on the page, in relative form such as `8天前` (8 days ago). It is not an absolute timestamp. |
| `organic_results[].position` | Rank of the result in the list, starting at 1. |
| `organic_results[].thumbnail` | URL of the article's thumbnail image. |
| `pagination.current / pagination.next / pagination.other_pages` | The current page number, the link to the next page, and links to other pages keyed by page number. |
| `related_searches[].query / related_searches[].link` | A related search term and the Baidu link for it. |
| `search_information.total_results` | Total result count reported for the query. |

### Notes

- Set `q` to any keyword. The example uses `coffee`, and Chinese keywords also fit the response, since results are in Chinese.
- Page links in `pagination.next` and `pagination.other_pages` point to Baidu search pages. Page numbers appear as keys, such as `2` and `3`.
- `date` is relative text such as `6天前`, so store the time you made the call if you need to work out the absolute date.
- The response also has a `top_searches` list with `position`, `text` and `link` for each entry. It does not depend on your keyword in the sample.

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/baidu/news.json`](../../../catalog/models/baidu/news.json) · Store page: https://www.sandbase.ai/model/baidu/news
