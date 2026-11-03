# Lemon8 Hot Search Keywords API: pricing, parameters and code examples

`lemon8/app/hot-search-keywords` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending search keywords and topics currently popular on Lemon8. Call this endpoint to track real-time user discovery trends across the app.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/hot-search-keywords"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/hot-search-keywords', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/hot-search-keywords", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/hot-search-keywords", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/lemon8/app/hot-search-keywords` with the body above minus `model`.

## Details

Returns the list of trending search keywords currently shown in Lemon8 search. It needs no input: send an empty JSON object `{}`.

### Use cases

- Collect the current hot search queries on Lemon8 to see which topics users look for.
- Pick keywords for Lemon8 post titles and tags from the terms in `data.hot_words[].query`.
- Store the list on a schedule to compare which queries appear or drop out over time.
- Feed a returned `query` into Lemon8 search to see the posts that match a trending term.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/hot-search-keywords" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "guess_hit_id": "",
    "hot_random_words": null,
    "hot_word_search_type": 2,
    "hot_words": [
      {
        "extra": "{\"recall_score\":{\"bert_viking_two_hop_recall\":\"0.000000\"},\"recall_position\":{\"be…",
        "group_id": "7590746814001978624",
        "query": "football catching tips",
        "recall_source": "bert_viking_two_hop_recall",
        "source": "recom_search",
        "type": "plain"
      }
    ],
    "impr_id": "202611030736318E8A0C01D997AA17A64C"
  },
  "message": "success",
  "result_status": 0,
  "server_time": "1793691391.95"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.hot_words[].query` | The trending search keyword text, for example `christmas`. |
| `data.hot_words[].group_id` | ID string attached to the keyword entry. |
| `data.hot_words[].type` | Kind of keyword entry. The sample shows `plain`. |
| `data.hot_words[].source` | Where the keyword comes from. The sample shows `recom_search`. |
| `data.hot_words[].recall_source` | Name of the recall method that selected this keyword, for example `bert_viking_two_hop_recall`. |
| `data.hot_words[].extra` | A JSON string with ranking details such as `recall_score`, `recall_position` and `roughsort_score`. Parse it as JSON before use. |
| `data.hot_random_words` | Extra random keywords. It is `null` in the sample response. |
| `data.hot_word_search_type` | Numeric search type code for the list. The sample shows `2`. |
| `data.impr_id` | ID string for this response. |
| `code / message / result_status` | Call status. `code` `0` and `message` `success` mean the call worked. |

### Notes

- The endpoint takes no parameters and returns the keyword list in a single response, with no pagination.
- `server_time` is a Unix timestamp in seconds, returned as a string with decimals.
- To see posts for a keyword, pass its `query` to [Lemon8 Search](/apis/lemon8/app/search).
- To browse more of the app's discovery content, call [Lemon8 Discover Page Content](/apis/lemon8/app/discover-tab).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Lemon8 Discover Page Banners](/apis/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/apis/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/apis/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/hot-search-keywords.json`](../../../../catalog/models/lemon8/app/hot-search-keywords.json) · Store page: https://www.sandbase.ai/model/lemon8/app/hot-search-keywords
