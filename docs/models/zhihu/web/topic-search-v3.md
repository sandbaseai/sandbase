# Zhihu Topic Search (V3) API: pricing, parameters and code examples

`zhihu/web/topic-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches Zhihu topics by keyword and returns matching topic profiles, follower metrics, and highlighted text matches with pagination support.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/topic-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/topic-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/topic-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/topic-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/topic-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of topics per page default `"25"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |

## Details

This API searches Zhihu topics by keyword. It returns a list of matching topics with their IDs, names, follower counts, and highlighted text. It needs one input, `keyword`.

### Use cases

- Find the Zhihu topic ID for a brand or subject such as OpenAI.
- Compare `follower_count` across topics that match the same keyword to see which has the largest audience.
- Show matched terms in a search UI by using the `<em>` tags in the highlight text.
- Collect topic avatars and descriptions to build a directory of topics on one theme.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/topic-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of topics per page |
| `offset` | string | No | Offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ab_params": "dm_ai_search_safe=1;dm_recency_ab=1;sb_cr=1;sb_vip_tag=1;sb_sku_time=1;dm_correc…",
  "data": [
    {
      "highlight": {
        "description": "由 Elon Musk, Peter Thiel, Sam Altman",
        "title": "<em>OpenAI</em>"
      },
      "hit_labels": null,
      "id": "20083046",
      "index": 0,
      "object": {
        "agreed_count": 0,
        "ai_ranking_list_url": "",
        "aliases": [],
        "attached_info_bytes": "OvEBCgtwbGFjZWhvbGRlchIgZjYyOWJjOGQwZDRmMDljZmNkMDgzMWYyYTFkNzI3OTQYAiIGMTgwNDc2…",
        "avatar_url": "https://pic1.zhimg.com/80/v2-4a85355a9ea1acc515ddabc2b3d1d4b1_qhd.jpg",
        "description": "由 Elon Musk, Peter Thiel, Sam Altman",
        "excerpt": "由 Elon Musk, Peter Thiel, Sam Altman",
        "follower_count": 6574
      },
      "type": "search_result"
    }
  ],
  "domain_info": {
    "first_category": ""
  },
  "filter_items": null,
  "hit_labels": null,
  "is_brand_word": false,
  "is_koc_words": false,
  "item_in_view": [
    {
      "index": 5,
      "token": "b62a7302…",
      "type": "user_survey"
    }
  ],
  "paging": {
    "is_end": false,
    "next": "https://api.zhihu.com/search_v3?advert_count=0&correction=1&filter_fields=&gk_ve…"
  },
  "pendant": null,
  "related_search_result": [],
  "search_action_info": {
    "attached_info_bytes": "OqQBEiBmNjI5YmM4ZDBkNGYwOWNmY2QwODMxZjJhMWQ3Mjc5NEoGb3BlbmFpUABYA2ABagZPcGVuQUlw…",
    "isfeed": false,
    "lc_idx": 20,
    "search_hash_id": "f629bc8d0d4f09cfcd0831f2a1d72794"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].id` | ID of the matching topic, as a string. |
| `data[].type` | Result type. Here it is `search_result`. |
| `data[].index` | Position of the result in the list, starting at 0. |
| `data[].highlight.title` | Topic title with the matched keyword wrapped in `<em>` tags. |
| `data[].highlight.description` | Topic description with matches highlighted. It can be an empty string. |
| `data[].object.description / data[].object.excerpt` | Short text describing the topic. Both can be empty. |
| `data[].object.follower_count` | Number of followers of the topic. Many topics show `0`. |
| `data[].object.avatar_url` | Image URL for the topic. |
| `data[].object.aliases` | List of alternative names for the topic. It is empty in this response. |
| `paging.is_end / paging.next` | `is_end` tells you whether more results exist. `next` is a URL for the next page of results. |

### Notes

- Use `limit` and `offset` to page through results. Both are sent as strings, and `limit` defaults to `25` and `offset` to `0`.
- Check `paging.is_end` to know when to stop paging.
- Strip the `<em>` tags from `highlight.title` if you need the plain topic name.
- To search content instead of topics, try [Zhihu Article Search](/apis/zhihu/web/article-search-v3) or [Zhihu Search Suggestions](/apis/zhihu/web/search-suggest).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/topic-search-v3.json`](../../../../catalog/models/zhihu/web/topic-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/topic-search-v3
