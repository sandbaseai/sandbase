# Douyin Xingtu Author Cooperation Info API: pricing, parameters and code examples

`douyin/xingtu-v2/author-cp-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.004 per call (free daily quota) · **Modes:** sync

Returns Douyin Xingtu creator cooperation details for a specified author ID. Query profile and partnership data using creator IDs alongside optional platform channel filters.

## Pricing

- **$0.004 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-cp-info", "o_author_id": "6677767167234015243"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-cp-info', {'o_author_id': '6677767167234015243'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-cp-info", {
  "o_author_id": "6677767167234015243"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-cp-info", sandbase.Params{
	"o_author_id": "6677767167234015243",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-cp-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Returns expected performance numbers for one Douyin Xingtu creator: expected cost per engagement (CPE), expected cost per thousand views (CPM), expected video views, and a hot item value. It needs a creator ID in `o_author_id`.

### Use cases

- Compare the expected CPM of several creators before you pick who to book for a campaign.
- Estimate the reach of a planned video from the creator's expected views in `expect_vv.value`.
- Check the expected CPE of a creator to judge how much each engagement may cost.
- Screen a shortlist of Xingtu authors by their expected cost figures.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-cp-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7029342444797820939"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `platform_channel` | integer | No | Platform channel, default 1 |
| `platform_source` | integer | No | Platform source, default 1 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "expect_cpe": {
    "cpe_21_60": "100",
    "cpe_60": "377"
  },
  "expect_cpm": {
    "cpm_21_60": "1923",
    "cpm_60": "7211"
  },
  "expect_vv": {
    "value": 4160093
  },
  "hot_item": {
    "value": 1000
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `expect_cpe.cpe_21_60 / expect_cpe.cpe_60` | Expected cost per engagement (CPE) for two video length groups. The key names suggest `cpe_21_60` covers videos of 21 to 60 seconds and `cpe_60` covers videos over 60 seconds. Values are strings. |
| `expect_cpm.cpm_21_60 / expect_cpm.cpm_60` | Expected cost per thousand views (CPM) for the same two video length groups. Values are strings. |
| `expect_vv.value` | Expected video views (VV) for the creator, as a number. |
| `hot_item.value` | A numeric value for the creator's hot item metric. The response does not show what unit it uses. |
| `base_resp.status_code` | Status code of the call. `0` means the call succeeded. |
| `base_resp.status_message` | Status message. It is an empty string when the call succeeds. |

### Notes

- Pass the Xingtu creator ID as `o_author_id`. If you only have a Douyin ID, call [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id) first to get it.
- `platform_source` and `platform_channel` are optional integers. Both default to `1`.
- For profile data on the same creator, call [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info).

### Pricing

$0.004 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-cp-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-cp-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-cp-info
