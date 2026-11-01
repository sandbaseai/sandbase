# Zhihu Article Search

`zhihu/web/article-search-v3` · api · Zhihu

Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offset pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/article-search-v3", "keyword": "教育", "limit": "5", "offset": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/article-search-v3', {'keyword': '教育', 'limit': '5', 'offset': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/article-search-v3", {
  "keyword": "教育",
  "limit": "5",
  "offset": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/article-search-v3", sandbase.Params{
	"keyword": "教育",
	"limit": "5",
	"offset": "0",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/article-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Empty comprehensive sorting default `""` |
| `limit` | string |  | Number of articles per page default `"20"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `vertical` | string |  | Empty unlimited type default `""` |
| `search_source` | string |  | Search Source default `"Normal"` |
| `time_interval` | string |  | Time interval default `""` |
| `vertical_info` | string |  | Vertical information default `""` |
| `search_hash_id` | string |  | Search Hash ID, used to filter duplicate search results default `""` |
| `show_all_topics` | integer |  | Show all topics default `0` |

## Details

Search Zhihu for a keyword and get matching articles and answers with title, excerpt, author, URL and engagement counts.

### Use cases

- Research expert opinions and long-form discussion on Zhihu.
- Monitor how a brand or product is discussed.
- Collect articles on a topic for content analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/article-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `sort` | string | No | Empty comprehensive sorting |
| `limit` | string | No | Number of articles per page |
| `offset` | string | No | Offset |
| `vertical` | string | No | Empty unlimited type |
| `search_source` | string | No | Search Source |
| `time_interval` | string | No | Time interval |
| `vertical_info` | string | No | Vertical information |
| `search_hash_id` | string | No | Search Hash ID, used to filter duplicate search results |
| `show_all_topics` | integer | No | Show all topics |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "paging": {
    "is_end": false
  },
  "search_action_info": {
    "search_hash_id": "<hash>"
  },
  "data": [
    {
      "type": "search_result",
      "object": {
        "id": "2090812756115067700",
        "type": "article",
        "voteup_count": 3,
        "comment_count": 0,
        "created_time": 1791268958,
        "title": "OpenAI「疯狂28天」首日，这都发了些啥啊…",
        "excerpt": "模型打不过A社，一天到晚净整些有的没的，OpenAI你倒是争点气啊！ OpenAI订阅性价比被A社碾压了 这还没完",
        "url": "https://api.zhihu.com/articles/2090812756115067700",
        "author": {
          "name": "<user>"
        }
      }
    }
  ]
}
```

### Notes

- Paginate with `offset` and `limit` (default 20 per page).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu Hot List](/model/zhihu/web/hot-list): Get the Zhihu hot list: trending questions with title, excerpt, heat, answer and follower counts, and links.
- [Get Zhihu AI Search (v2)](/model/zhihu/web/ai-search-stream): Get Zhihu AI Search results (new endpoint).
- [Get Zhihu Answer Detail](/model/zhihu/web/answer-detail): Get a single Zhihu answer's detail (content / stats / author / question, etc.).

---
Machine-readable: [`catalog/models/zhihu/web/article-search-v3.json`](../../../../catalog/models/zhihu/web/article-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/article-search-v3
