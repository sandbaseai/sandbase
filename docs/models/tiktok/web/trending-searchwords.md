# TikTok Daily Trending Search Words API: pricing, parameters and code examples

`tiktok/web/trending-searchwords` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns daily trending search terms and keywords from TikTok Web. Use this endpoint to monitor popular search queries and emerging platform topics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/trending-searchwords"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/trending-searchwords', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/trending-searchwords", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/trending-searchwords", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/trending-searchwords` with the body above minus `model`.

## Details

Returns the current list of trending search terms on TikTok Web. The request takes no input parameters, so you send an empty JSON object.

### Use cases

- Track which news events and topics people search for on TikTok today.
- Build a daily log of trending search terms to compare topics across days.
- Feed trending phrases into a content calendar or keyword research list.
- Use a trending phrase as the query for a follow-up search to find related videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/trending-searchwords" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611031544316D7CBC035751710D1C41",
    "now": 1793691871000
  },
  "log_pb": {
    "impr_id": "202611031544316D7CBC035751710D1C41"
  },
  "status_code": 0,
  "status_msg": "",
  "trending_search_words": [
    {
      "trendingSearchWord": "Learjet 60 Crashes Near Palm Beach, 9 Dead",
      "trendingSearchWordType": "2"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `trending_search_words[].trendingSearchWord` | The text of one trending search term, as shown on TikTok. |
| `trending_search_words[].trendingSearchWordType` | A type code for the term, returned as a string such as `"2"`. The response does not explain what each code means. |
| `status_code / status_msg` | Result status of the call. `0` with an empty message means the request succeeded. |
| `extra.now` | A timestamp for when the response was generated. The value looks like Unix time in milliseconds. |
| `extra.logid / log_pb.impr_id` | Request tracking identifiers. They have the same value in this response. |
| `extra.fatal_item_ids` | A list of item IDs that failed. It is empty when nothing failed. |

### Notes

- Send `{}` as the request body. The API has no parameters.
- Results come back as a single list in `trending_search_words`. The response shows no pagination fields.
- To search for a returned term, pass it to [TikTok Web General Search](/apis/tiktok/web/general-search).
- To get related query ideas for a keyword, call [TikTok Search Keyword Suggestions](/apis/tiktok/web/search-keyword-suggest).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/trending-searchwords.json`](../../../../catalog/models/tiktok/web/trending-searchwords.json) · Store page: https://www.sandbase.ai/model/tiktok/web/trending-searchwords
