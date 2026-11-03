# Douyin Hashtag Suggestions API: pricing, parameters and code examples

`douyin/search/challenge-suggest` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/challenge-suggest", "keyword": "游戏"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/challenge-suggest', {'keyword': '游戏'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/challenge-suggest", {
  "keyword": "游戏"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/challenge-suggest", sandbase.Params{
	"keyword": "游戏",
})
```

Same call via the path form: `POST /v1/api/douyin/search/challenge-suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search keyword, e.g., "game" default `"游戏"` |

## Details

Returns a list of Douyin hashtag and challenge suggestions that match a keyword. Each suggestion includes the challenge name, its challenge ID, and a total view count. The only input is `keyword`.

### Use cases

- Fill an autocomplete box for hashtag picking in a Douyin posting or planning tool.
- Compare the `view_count` of related hashtags to pick tags with a larger audience.
- Collect challenge IDs for a topic keyword, then look up each challenge in more detail.
- Check which hashtag spellings Douyin suggests for a brand or topic word.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/challenge-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search keyword, e.g., "game" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110315321538D3C329F551034F46C2",
    "now": 1793691135000,
    "scenes": null,
    "search_request_id": ""
  },
  "log_pb": {
    "impr_id": "2026110315321538D3C329F551034F46C2"
  },
  "rid": "2026110315321538D3C329F551034F46C2",
  "status_code": 0,
  "status_msg": "",
  "sug_list": [
    {
      "cha_name": "游戏",
      "cid": "1624332181128206",
      "group_id": "6534954143558145288",
      "tag": 0,
      "view_count": 747309565180
    }
  ],
  "words_query_record": {
    "info": "{}",
    "query_id": "",
    "words_source": "sug"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `sug_list[]` | List of suggested hashtags and challenges that match the keyword. |
| `sug_list[].cha_name` | Name of the suggested challenge or hashtag. |
| `sug_list[].cid` | Challenge ID of the suggestion, returned as a string. |
| `sug_list[].group_id` | Group ID returned with the suggestion, as a string. |
| `sug_list[].view_count` | Total view count of the challenge. |
| `sug_list[].tag` | Numeric tag value returned with each suggestion. It was `0` for all items in the sample. |
| `status_code / status_msg` | Status of the request. `status_code` is `0` and `status_msg` is empty in the sample. |
| `words_query_record.words_source` | Source label for the suggestions. The sample value is `sug`. |
| `rid / log_pb.impr_id` | Request ID. Both hold the same value in the sample. |

### Notes

- Pass the search text in `keyword`. The schema default is `游戏`.
- The response has no pagination fields. It returns one list of suggestions per request.
- Use `cid` to identify a challenge. For more on a hashtag, see [Douyin Hashtag Details](/apis/douyin/app-v3/hashtag-detail). To list its videos, see [Douyin Hashtag Video List](/apis/douyin/app-v3/hashtag-video-list).
- For full search results with more fields, use [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Discussion Search](/apis/douyin/search/discuss-search): Returns discussion and question-and-answer search results from Douyin.

---
Machine-readable: [`catalog/models/douyin/search/challenge-suggest.json`](../../../../catalog/models/douyin/search/challenge-suggest.json) · Store page: https://www.sandbase.ai/model/douyin/search/challenge-suggest
