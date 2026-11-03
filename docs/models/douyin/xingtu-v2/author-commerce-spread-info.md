# Douyin Author Commerce Spread Info API: pricing, parameters and code examples

`douyin/xingtu-v2/author-commerce-spread-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call · **Modes:** sync

Get Author Commerce Spread Info on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.003 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-commerce-spread-info", "o_author_id": "7112600044674482187"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-commerce-spread-info', {'o_author_id': '7112600044674482187'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-commerce-spread-info", {
  "o_author_id": "7112600044674482187"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-commerce-spread-info", sandbase.Params{
	"o_author_id": "7112600044674482187",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-commerce-spread-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `o_author_id` | string | yes | Creator ID  |

## Details

Returns commerce spread metrics for one Douyin creator on Xingtu, such as cost per thousand views (CPM), cost per engagement (CPE) and view counts. It needs the creator ID in `o_author_id`.

### Use cases

- Compare a creator's `cpm_60` and `cpe_60` against other creators before you shortlist them for a campaign.
- Check how a creator's CPM ranks with `cpm_20_60_rank_percent` when you build a pricing benchmark.
- Compare the creator's own values with the `sn_` values to see how they differ for the same metric.
- Pull `vv` for a set of creators to estimate their view volume in commerce content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-commerce-spread-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7112600044674482187"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "cpe_20_60": "0.3849",
  "cpe_60": "0.4812",
  "cpm_20_60": "10.2661",
  "cpm_20_60_rank_percent": "0.04531789206117616",
  "cpm_60": "12.8326",
  "modify_time": "1793675684",
  "platform_hot_rate": "1",
  "sn_cpe_20_60": "1.5187",
  "sn_cpe_60": "1.8984",
  "sn_cpm_20_60": "27.0499",
  "sn_cpm_60": "33.8124"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cpm_20_60 / cpm_60` | CPM values for the creator. The `20_60` name suggests a 20 to 60 range and `60` suggests a 60 threshold, but the response does not define it. Values are strings. |
| `cpe_20_60 / cpe_60` | CPE values for the creator, with the same `20_60` and `60` naming as the CPM fields. |
| `cpm_20_60_rank_percent` | Rank value for `cpm_20_60`, returned as a decimal string between 0 and 1. |
| `sn_cpm_20_60 / sn_cpm_60` | CPM values with an `sn_` prefix. They are higher than the matching `cpm_` values in this response. |
| `sn_cpe_20_60 / sn_cpe_60` | CPE values with an `sn_` prefix. They are higher than the matching `cpe_` values in this response. |
| `vv / sn_vv` | View counts as numeric strings. `sn_vv` is lower than `vv` in this response. |
| `platform_hot_rate` | Hot rate value for the platform, returned as a string. It is `1` in this response. |
| `modify_time` | Unix timestamp in seconds, returned as a string. It most likely marks the last update of this record. |
| `base_resp.status_code` | Status code of the call. `0` means success. |

### Notes

- Get `o_author_id` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator) or from [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info).
- All metric values arrive as strings. Convert them to numbers before you sort or compare.
- For general spread metrics of the same creator, call [Douyin Xingtu Author Spread Info](/apis/douyin/xingtu-v2/author-spread-info).

### Pricing

$0.003 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-commerce-spread-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-commerce-spread-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-commerce-spread-info
