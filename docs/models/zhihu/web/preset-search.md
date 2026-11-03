# Zhihu Preset Search API: pricing, parameters and code examples

`zhihu/web/preset-search` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves preset search recommendations and default placeholder queries from Zhihu Web. Returns trending search terms without requiring input parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/preset-search"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/preset-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/preset-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/preset-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/zhihu/web/preset-search` with the body above minus `model`.

## Details

Returns the preset search words Zhihu Web shows in its search box, with the query text, a display window, and tracking IDs for each word. It takes no input, so you send an empty JSON object.

### Use cases

- Read the current placeholder queries shown in the Zhihu search box.
- Log the `preset_words.words[].query` values on a schedule to see which suggested searches Zhihu rotates in and out.
- Feed the returned queries into a keyword search to see what content they lead to.
- Use `begin_ts` and `end_ts` to see how long each preset word stays active.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/preset-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attached_info": "OmsSIDQ3Zjc5OTUxMWU1OGY5YzZlNzZhMGRiODM0OTQ0YmZjggMgNDdmNzk5NTExZTU4ZjljNmU3NmEw…",
  "preset_words": {
    "NextRequestTs": 1793692733,
    "words": [
      {
        "ad_commercial_json": "",
        "attached_info": "OmsSIDQ3Zjc5OTUxMWU1OGY5YzZlNzZhMGRiODM0OTQ0YmZjggMgNDdmNzk5NTExZTU4ZjljNmU3NmEw…",
        "begin_ts": 1793692133,
        "end_ts": 1793695733,
        "id": "5759959305996362580",
        "is_force": false,
        "preset_word_ad_commercial_json": "",
        "query": "大学英语六级历年真题含答案",
        "real_query": "大学英语六级历年真题含答案",
        "recall_source": "q2q_co_click",
        "request_click_id": "e28295c4-4e69-486f-9164-08294ded32d2",
        "score": 0
      }
    ]
  },
  "request_hash_id": "47f799511e58f9c6e76a0db834944bfc"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `preset_words.words[].query` | The preset search text shown to the user. It matches `real_query` in the sample response. |
| `preset_words.words[].real_query` | The query text used when the word is searched. |
| `preset_words.words[].begin_ts / preset_words.words[].end_ts` | Start and end of the window in which the word is active. Both are Unix timestamps in seconds, and the sample window is 3600 seconds long. |
| `preset_words.NextRequestTs` | A Unix timestamp in seconds. It appears to mark when to request the preset words again. |
| `preset_words.words[].id` | Numeric ID of the preset word, returned as a string. It can be negative. |
| `preset_words.words[].recall_source` | Label for the method that picked the word, such as `q2q_co_click` or `preset_recall_dssm`. |
| `preset_words.words[].type` | Type of the preset word. The sample shows `general`. |
| `preset_words.words[].uuid / preset_words.words[].request_click_id` | Unique IDs for the word and the request click. Use them to tell entries apart. |
| `preset_words.words[].weight / preset_words.words[].score` | Numeric ranking values for the word. The sample shows `weight` as `1` and `score` as `0`. |
| `request_hash_id` | Hash ID for this request. |

### Notes

- Send `{}` as the body. The API has no request parameters.
- Each word has its own `attached_info` string, and there is also one at the top level. Treat these as opaque tracking values.
- To search a returned word, pass its `query` to [Zhihu Article Search](/apis/zhihu/web/article-search-v3).
- For more query ideas, see [Zhihu Search Suggestions](/apis/zhihu/web/search-suggest) or [Zhihu Hot List](/apis/zhihu/web/hot-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/preset-search.json`](../../../../catalog/models/zhihu/web/preset-search.json) · Store page: https://www.sandbase.ai/model/zhihu/web/preset-search
