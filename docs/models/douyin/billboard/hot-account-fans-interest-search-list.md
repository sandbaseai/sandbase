# Douyin Account Fan Interest Search Terms API: pricing, parameters and code examples

`douyin/billboard/hot-account-fans-interest-search-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the top ten search terms reflecting fan interest over the last three days for a specified Douyin creator account using their user sec_id.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-account-fans-interest-search-list", "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-account-fans-interest-search-list', {'sec_uid': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-account-fans-interest-search-list", {
  "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-account-fans-interest-search-list", sandbase.Params{
	"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-account-fans-interest-search-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_uid` | string | yes | User sec_id  |

## Details

Returns the top ten search terms that fans of a Douyin creator account searched for over the last three days. Each term comes with a hot score. You send the creator's `sec_uid` as input.

### Use cases

- Find out what an account's audience is searching for right now to plan new videos.
- Compare the search interests of fans across several creators before choosing a partner.
- Spot a recurring search term in a niche and build a topic or hashtag around it.
- Check whether a creator's fan interests match your product category, such as beauty items.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-fans-interest-search-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "hot_score": 32,
      "word": "反相之地"
    }
  ],
  "extra": {
    "now": 1793691104000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | List of fan interest search terms for the account. The sample response shows three items, and the API describes the list as the top ten. |
| `data[].word` | The search term fans looked up. The sample values are Chinese text. |
| `data[].hot_score` | Numeric hot score for the term. Higher values mean the term ranks higher in fan interest, and the sample scores run from 31 to 32. |
| `code` | Status code of the response. `0` appears in the sample response for a successful call. |
| `message` | Status message. It is an empty string in the sample response. |
| `extra.now` | Timestamp for the response in the `extra` object. The sample value `1793691104000` has 13 digits, which fits a millisecond Unix timestamp. |

### Notes

- Pass the creator's `sec_uid`, which is the Douyin user sec_id. It is a long string that starts with `MS4wLjAB`.
- The endpoint takes only `sec_uid`. It has no pagination parameters.
- To see which accounts the same fans follow, call [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list). For the topics they care about, call [Douyin Account Fan Interest Topics](/apis/douyin/billboard/hot-account-fans-interest-topic-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-fans-interest-search-list.json`](../../../../catalog/models/douyin/billboard/hot-account-fans-interest-search-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-fans-interest-search-list
