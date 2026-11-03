# Douyin XingTu KOL Cost Metrics API: pricing, parameters and code examples

`douyin/xingtu/kol-cp-info-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get expected campaign metrics for a Douyin KOL from XingTu: expected views, CPM and CPE estimates, and hot-video counts.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-cp-info-v1", "kolId": "7038603512770461703"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-cp-info-v1', {'kolId': '7038603512770461703'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-cp-info-v1", {
  "kolId": "7038603512770461703"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-cp-info-v1", sandbase.Params{
	"kolId": "7038603512770461703",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-cp-info-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |

## Details

Returns the expected campaign metrics XingTu shows for one Douyin creator: expected views, CPM and CPE estimates, and a hot-video count. It needs one input, the creator's XingTu `kolId`.

### Use cases

- Estimate how many views a sponsored video from a given KOL is likely to get with `expect_vv.value`.
- Compare CPM and CPE estimates across a shortlist of KOLs before booking.
- Check CPM and CPE for different video lengths to pick the better format for a brief.
- Screen creators by `hot_item.value` to see how many hot videos XingTu counts for them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-cp-info-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7038603512770461703"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "expect_cpe": {
    "cpe_21_60": "47",
    "cpe_60": "63"
  },
  "expect_cpm": {
    "cpm_21_60": "2039",
    "cpm_60": "2733"
  },
  "expect_vv": {
    "value": 676711
  },
  "hot_item": {
    "value": 1800
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `expect_vv.value` | Expected video views for the KOL, as a number. |
| `expect_cpm.cpm_21_60` | Expected CPM for videos in the 21 to 60 range, returned as a string. The key name suggests a 21 to 60 second video length. |
| `expect_cpm.cpm_60` | Expected CPM for videos in the 60 range, returned as a string. The key name suggests videos longer than 60 seconds. |
| `expect_cpe.cpe_21_60` | Expected CPE for the 21 to 60 range, returned as a string. |
| `expect_cpe.cpe_60` | Expected CPE for the 60 range, returned as a string. |
| `hot_item.value` | Hot-video count for the KOL, as a number. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message means it succeeded. |

### Notes

- Get `kolId` from [Douyin XingTu kolId Lookup](/apis/douyin/xingtu/xingtu-kolid-by-sec-user-id), [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid) or [Douyin XingTu KOL ID by Unique ID](/apis/douyin/xingtu/xingtu-kolid-by-unique-id).
- `kolId` is a numeric ID sent as a string, for example `7038603512770461703`.
- CPM and CPE values come back as strings, so convert them to numbers before you compare them.
- For the rate card of the same creator, call [Douyin XingTu KOL Price](/apis/douyin/xingtu/kol-service-price-v1).

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.
- [Douyin XingTu KOL Audience](/apis/douyin/xingtu/kol-fans-portrait-v1): Get the audience portrait of a Douyin KOL from XingTu: fan age, gender, region, device and interest distributions.
- [Douyin XingTu KOL Price](/apis/douyin/xingtu/kol-service-price-v1): Get the XingTu rate card of a Douyin KOL: price per collaboration type (sponsored video, live and more), settlement type and industry tags.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-cp-info-v1.json`](../../../../catalog/models/douyin/xingtu/kol-cp-info-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-cp-info-v1
