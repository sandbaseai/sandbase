# Douyin Hot Account Fan Portrait API: pricing, parameters and code examples

`douyin/billboard/hot-account-fans-portrait-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns fan portrait metrics and demographic distribution data for a Douyin account using its secure user ID and portrait option filter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-account-fans-portrait-list", "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-account-fans-portrait-list', {'sec_uid': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-account-fans-portrait-list", {
  "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-account-fans-portrait-list", sandbase.Params{
	"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-account-fans-portrait-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `option` | integer |  | Option  |
| `sec_uid` | string | yes | User sec_id  |

## Details

Returns the fan portrait of a Douyin account as a share distribution and a TGI distribution across buckets. It needs the account's `sec_uid` and accepts an optional integer `option` to pick the portrait type.

### Use cases

- Compare the top buckets in `portrait` across creators to see which audience segment dominates each account.
- Use `portrait_tgi` to find which segment is over-represented in a creator's fans compared with the baseline.
- Screen influencers for a campaign by checking whether their fan distribution matches a target segment.
- Store portrait snapshots for an account to review its audience mix over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-fans-portrait-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_id |
| `option` | integer | No | Option |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "option": "1",
    "portrait": {
      "key": "2000~2999",
      "portrait_data": [
        {
          "name": "2000~2999",
          "value": 0.24579581073685258
        }
      ]
    },
    "portrait_tgi": {
      "key": "7000~7999",
      "portrait_data": [
        {
          "name": "7000~7999",
          "value": 166.5975572593203
        }
      ]
    },
    "user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
  },
  "extra": {
    "now": 1793691104000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.option` | The portrait option the response is for, returned as a string. The request sent no `option`, and the response shows `1`. |
| `data.user_id` | The `sec_uid` of the account the portrait belongs to. |
| `data.portrait.key` | The name of the bucket with the highest share in `portrait_data`. |
| `data.portrait.portrait_data[].name` | Bucket label, such as `2000~2999`. The labels are ranges of numbers, and the response does not say what the numbers measure. |
| `data.portrait.portrait_data[].value` | Share of fans in that bucket, as a decimal. For example `0.2458` is about 24.6 percent. |
| `data.portrait_tgi.key` | The name of the bucket with the highest TGI value in `portrait_tgi.portrait_data`. |
| `data.portrait_tgi.portrait_data[].name` | Bucket label for the TGI list. It uses the same range format as `portrait`. |
| `data.portrait_tgi.portrait_data[].value` | TGI score for the bucket. A value above 100 would mean the bucket is over-represented, but the scale is not documented, so check it against your own data. |

### Notes

- Get `sec_uid` from an account list call such as [Douyin Hot Account List](/apis/douyin/billboard/hot-account-list) or [Douyin Hot Account Search](/apis/douyin/billboard/hot-account-search-list).
- `sec_uid` is the only required parameter. The `option` value is an integer and the API does not list the allowed values.
- The `portrait_data` lists in the response are sorted from highest to lowest `value`.
- For what else fans like, call [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-fans-portrait-list.json`](../../../../catalog/models/douyin/billboard/hot-account-fans-portrait-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-fans-portrait-list
