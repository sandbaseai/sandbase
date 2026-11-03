# Xiaohongshu Keyword Suggestions API: pricing, parameters and code examples

`xiaohongshu/search-recommend` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Xiaohongshu (RedNote) search keyword suggestions for a submitted seed term. Use it to expand query sets, refine content-research searches, and plan SEO or programmatic SEO keyword coverage.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/search-recommend", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/search-recommend', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/search-recommend", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/search-recommend", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/search-recommend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword.  |

## Details

This API returns search keyword suggestions from Xiaohongshu (RedNote) for a seed term. It needs one input, `keyword`, and returns a list of suggested search phrases.

### Use cases

- Expand a seed term like `美食` into a longer list of related search phrases.
- Find long-tail phrases to target when planning Xiaohongshu note titles and topics.
- Build keyword sets for content research or programmatic SEO pages.
- Check which phrasings the platform suggests for a product or topic name.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/search-recommend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "items": [
    {
      "highlight_flags": [
        true
      ],
      "icon": "http://picasso-static.xiaohongshu.com/fe-platform/ada4a11451816f9500d7a3bfd561ed…",
      "icon_night": "http://picasso-static.xiaohongshu.com/fe-platform/20107487de37f8896d23383e41f43d…",
      "is_intervened": false,
      "link": "",
      "search_type": "notes",
      "text": "美食推荐",
      "type": "top_note"
    }
  ],
  "result": {
    "message": "success",
    "success": true
  },
  "search_cpl_id": "a2bf3c0f624ba770ed010e326ae99187",
  "word_request_id": "07b78290ea0bc085425a9a628b86185c"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | List of suggested search phrases for the submitted `keyword`. |
| `items[].text` | The suggested search phrase, ready to use as a new search query. |
| `items[].highlight_flags` | List of true/false values, one per entry. The values show which parts of `text` the app highlights. |
| `items[].search_type` | The kind of search the suggestion leads to. The sample shows `notes`. |
| `items[].type` | The suggestion category. The sample shows `top_note`. |
| `items[].is_intervened` | Boolean flag. The sample shows `false` for every suggestion. |
| `items[].icon / items[].icon_night` | Icon image URLs for the suggestion, one for the default theme and one for night mode. |
| `items[].link` | Link attached to the suggestion. It is an empty string in the sample. |
| `result.success / result.message` | Whether the call worked, plus a status message such as `success`. |
| `search_cpl_id / word_request_id` | Request identifiers returned with the suggestions. |

### Notes

- Send the seed term in `keyword`. Chinese terms such as `美食` work as shown in the example.
- Use the `text` values from `items[]` as the `keyword` for a note search, for example with [Xiaohongshu (RED) Note Search](/apis/xiaohongshu/app-v2/search-notes).
- To see what is trending instead of what matches a seed term, call [Xiaohongshu Hot Search](/apis/xiaohongshu/hot-search).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/search-recommend.json`](../../../catalog/models/xiaohongshu/search-recommend.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/search-recommend
