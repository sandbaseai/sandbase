# Douyin Search Suggestions API: pricing, parameters and code examples

`douyin/search/search-suggest` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get Douyin search autocomplete suggestions for a keyword: the related queries users see while typing in the Douyin app.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/search-suggest", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/search-suggest', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/search-suggest", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/search-suggest", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/douyin/search/search-suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Input keyword, e.g., "Artificial Intelligence" default `"人工智能"` |

## Details

Returns the autocomplete suggestions Douyin shows while a user types a keyword in the search box. It needs one input, `keyword`, and returns a list of suggested queries in `sug_list`.

### Use cases

- Collect long-tail search phrases around a topic such as `人工智能` for Douyin content planning.
- Check which related queries Douyin offers for a brand or product name.
- Build keyword lists to feed into a Douyin video or user search.
- Compare the suggestions for several keywords to see how users phrase a topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/search-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Input keyword, e.g., "Artificial Intelligence" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cache_conf": {
    "enable": false
  },
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153220ABB7B6447CA5FAB75334",
    "now": 1793691141000,
    "search_request_id": ""
  },
  "log_pb": {
    "impr_id": "20261103153220ABB7B6447CA5FAB75334"
  },
  "rid": "20261103153220ABB7B6447CA5FAB75334",
  "status_code": 0,
  "status_msg": "",
  "sug_list": [
    {
      "content": "人工智能",
      "extra_info": {
        "poi_id": "",
        "poi_location_recall_log_id": "20261103153220ABB7B6447CA5FAB75334",
        "search_params": "{\"sug_poi_id\":\"\"}"
      },
      "pos": [
        {
          "begin": 0,
          "end": 3
        }
      ],
      "sug_type": "",
      "word_record": {
        "group_id": "6527568579963917582",
        "words_content": "人工智能",
        "words_position": 0,
        "words_source": "sug"
      }
    }
  ],
  "sug_virtual_list": null,
  "time_cost": {
    "server_engine_cost": "108",
    "stream_inner": "119"
  },
  "words_lists": [],
  "words_query_record": {
    "info": "{}",
    "query_id": "6527568579963917582",
    "words_source": "sug"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `sug_list[].content` | The suggested search phrase, as a user would see it in the Douyin search box. |
| `sug_list[].word_record.words_content` | The suggestion text again, stored inside the word record for that suggestion. |
| `sug_list[].word_record.words_position` | Zero-based position of the suggestion in the list. `0` is the first suggestion. |
| `sug_list[].word_record.group_id` | ID string for the suggestion word. |
| `sug_list[].word_record.words_source` | Where the word came from. The sample response shows `sug` for every item. |
| `sug_list[].pos[].begin / sug_list[].pos[].end` | Start and end character positions inside `content`. In the sample they cover the typed keyword at the start of the phrase. |
| `words_query_record.query_id` | ID of the query record for this request. In the sample it matches the first suggestion's `group_id`. |
| `status_code` | Request status inside the response body. `0` appears in the sample response, with an empty `status_msg`. |

### Notes

- The only input is `keyword`. Use the text a person would type into the Douyin search box.
- To search for content with a suggested phrase, pass its `content` value to [Douyin Video Search](/apis/douyin/search/video-search-v2) or [Douyin General Search](/apis/douyin/search/general-search-v1).
- For hashtag ideas instead of query suggestions, call [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest).
- `sug_virtual_list` is `null` and `words_lists` is empty in the sample response.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin General Search](/apis/douyin/search/general-search-v1): Search Douyin (Chinese TikTok) from the app's general search tab and get videos with descriptions, authors and play, like, comment and share counts.
- [Douyin Video Search (V1)](/apis/douyin/search/video-search-v1): Search Douyin videos by keyword: descriptions, authors and play, like, comment and share counts, with sort, publish-time, duration and content-type filters.
- [Douyin Video Search](/apis/douyin/search/video-search-v2): Search Douyin videos by keyword and get descriptions, authors and play, like, comment and share counts.

---
Machine-readable: [`catalog/models/douyin/search/search-suggest.json`](../../../../catalog/models/douyin/search/search-suggest.json) · Store page: https://www.sandbase.ai/model/douyin/search/search-suggest
