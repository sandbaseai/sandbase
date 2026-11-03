# Douyin Search keyword suggestions V2 API: pricing, parameters and code examples

`douyin/search/search-suggest-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Fetch search keyword suggestions V2 on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/search-suggest-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/search-suggest-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/search-suggest-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/search-suggest-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/search-suggest-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | The keyword to be suggested default `"人工智能"` |
| `history_words` | string |  | Optional, the user's history search words (comma separated), affects the ranking of suggestions  |

## Details

Returns search keyword suggestions from Douyin for a given keyword. It needs one input, `keyword`, and accepts an optional `history_words` list to influence the ranking.

### Use cases

- Build a keyword list for Douyin content by expanding a seed term into related search phrases.
- Check which phrases Douyin offers when users start typing a topic such as `人工智能`.
- Compare suggestion lists for different seed words to find topic angles for video titles and hashtags.
- Test how a set of `history_words` changes the order of suggestions for the same keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/search-suggest-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `history_words` | string | No | Optional, the user's history search words (comma separated), affects the ranking of suggestions |
| `keyword` | string | No | The keyword to be suggested |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "items": [
    {
      "content": "人工智能比赛",
      "extra_info": {
        "poi_id": "",
        "poi_location_recall_log_id": "202611031532215E8A160EA19863E55352",
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
        "group_id": "6596440824983065859",
        "words_content": "人工智能比赛",
        "words_position": 0,
        "words_source": "sug"
      }
    }
  ],
  "raw_key": "sug_list",
  "words": [
    "人工智能比赛"
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].content` | The suggested search phrase as shown to the user. |
| `items[].pos[].begin / items[].pos[].end` | Start and end character positions in `content`. In the sample they cover the part of the phrase that matches the input keyword. |
| `items[].word_record.words_content` | The suggestion text inside the word record. It matches `content` in the sample. |
| `items[].word_record.words_position` | Zero-based rank of the suggestion in the list. |
| `items[].word_record.words_source` | Where the suggestion came from. The sample shows `sug`. |
| `items[].word_record.group_id` | Numeric ID string for the suggestion word group. |
| `items[].sug_type` | Type label of the suggestion. It is an empty string in the sample. |
| `items[].extra_info.search_params` | JSON string with extra search parameters, such as `sug_poi_id`. The sample value has an empty POI ID. |
| `words` | Plain list of the suggestion phrases, in the same order as `items`. |

### Notes

- The `words` array is the quickest way to get just the phrases. Use `items` when you need rank, match positions or IDs.
- `search_params` is a JSON-encoded string, so parse it before reading its keys.
- For another suggestion endpoint, see [Douyin Search Suggestions](/apis/douyin/search/search-suggest). For hashtag suggestions, use [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest).
- To search videos for a chosen suggestion, pass it to [Douyin Video Search](/apis/douyin/search/video-search-v2).

### Pricing

$0.01 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/search/search-suggest-v2.json`](../../../../catalog/models/douyin/search/search-suggest-v2.json) · Store page: https://www.sandbase.ai/model/douyin/search/search-suggest-v2
