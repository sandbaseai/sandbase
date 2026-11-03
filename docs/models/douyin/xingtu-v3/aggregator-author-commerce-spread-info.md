# Douyin Xingtu Creator Commerce Spread Info API: pricing, parameters and code examples

`douyin/xingtu-v3/aggregator-author-commerce-spread-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) commerce spread information for a specified creator. Use it to compare creators during commerce campaign planning.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-commerce-spread-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-commerce-spread-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-commerce-spread-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-commerce-spread-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-commerce-spread-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns a small set of commerce spread numbers for one creator on Douyin Creator Marketplace (Xingtu). It needs the creator's `oAuthorId`.

### Use cases

- Compare view counts of several creators before you pick who to book for a commerce campaign.
- Check how much of a creator's views come from the `sn_vv` figure against the total `vv` figure.
- Track the `platform_hot_rate` value for a shortlist of creators.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-commerce-spread-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "modify_time": "1793681224",
  "platform_hot_rate": "1",
  "sn_vv": "12061062",
  "vv": "13169552"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `vv` | View count for the creator, returned as a string. Compare it with `sn_vv`. |
| `sn_vv` | A second view count returned as a string. It is lower than `vv` in the sample, so it likely covers a narrower set of videos. The key name does not say which. |
| `platform_hot_rate` | Hot rate value for the creator on the platform, returned as a string. The sample value is `1`. |
| `modify_time` | Time of the last update, as a Unix timestamp in seconds, returned as a string. |
| `base_resp.status_code / base_resp.status_message` | Call status. `status_code` is `0` and `status_message` is empty in the successful sample. |

### Notes

- Pass the creator's Xingtu author ID as `oAuthorId`. It is a numeric string such as `6870161898013196295`.
- All numbers come back as strings. Convert them to integers before you compare or sort.
- For more creator detail, call [Douyin Xingtu Spread Metrics](/apis/douyin/xingtu-v3/data-sp-author-spread-info) or [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-commerce-spread-info.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-commerce-spread-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-commerce-spread-info
