# DuckDuckGo News Search API: pricing, parameters and code examples

`duckduckgo/news` · data API · DuckDuckGo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

DuckDuckGo News results for a keyword: headline, source, date, snippet and link.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "duckduckgo/news", "q": "apple"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('duckduckgo/news', {'q': 'apple'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("duckduckgo/news", {
  "q": "apple"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "duckduckgo/news", sandbase.Params{
	"q": "apple",
})
```

Same call via the path form: `POST /v1/api/duckduckgo/news` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | q  |

## Details

This API returns DuckDuckGo News results for a keyword. Each result has a headline, source name, relative date, snippet, link and thumbnail. It needs one input: the search term in `q`.

### Use cases

- Track news mentions of a brand or product name such as `apple`.
- Build a headline feed for a topic page or dashboard.
- Collect article links and snippets for a media monitoring report.
- Check which outlets cover a subject by counting the `source` values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/duckduckgo/news" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "apple"}'
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
  "news_results": [
    {
      "date": "8 hours ago",
      "link": "https://techcrunch.com/2026/11/02/apple-says-its-hard-to-predict-when-iphone-duo…",
      "position": 1,
      "snippet": "Apple says iPhone Duo production is ramping up, but it still can't say when supp…",
      "source": "TechCrunch",
      "thumbnail": "https://techcrunch.com/wp-content/uploads/2026/09/iPhone-duo.jpeg?resize=1200,67…",
      "title": "Apple says it's 'hard to predict' when iPhone Duo constraints will improve"
    }
  ],
  "search_information": {
    "news_results_state": "Results for exact spelling"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `news_results[].title` | Headline of the news article. |
| `news_results[].link` | Full URL of the article on the publisher's site. |
| `news_results[].source` | Name of the publication, for example `TechCrunch` or `MarketWatch`. |
| `news_results[].date` | When the article was published, as relative text such as `8 hours ago`. |
| `news_results[].snippet` | Short text excerpt from the article. Long snippets may end with an ellipsis. |
| `news_results[].position` | Rank of the result in the list, starting at `1`. |
| `news_results[].thumbnail` | URL of the preview image for the article. |
| `search_information.news_results_state` | Short status text about the search, for example `Results for exact spelling`. |

### Notes

- Pass the search term in `q`. This is the only parameter and it is required.
- The `date` field is relative text, not a timestamp, so store the fetch time if you need to date articles later.
- For general web results instead of news, use [DuckDuckGo Search](/apis/duckduckgo/search).

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/duckduckgo/news.json`](../../../catalog/models/duckduckgo/news.json) · Store page: https://www.sandbase.ai/model/duckduckgo/news
