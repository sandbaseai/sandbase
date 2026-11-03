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

Pass a XingTu `kolId` and get the cost-performance estimates XingTu shows for the creator.

### Use cases

- Estimate campaign reach and cost per view.
- Compare cost efficiency across KOLs.
- Support media-buying decisions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-cp-info-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7038603512770461703"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-k… |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "expect_cpe": {
    "cpe_21_60": "106",
    "cpe_60": "143"
  },
  "expect_cpm": {
    "cpm_21_60": "4415",
    "cpm_60": "5919"
  },
  "expect_vv": {
    "value": 312535
  },
  "hot_item": {
    "value": 1800
  }
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.
- [Douyin XingTu KOL Audience](/apis/douyin/xingtu/kol-fans-portrait-v1): Get the audience portrait of a Douyin KOL from XingTu: fan age, gender, region, device and interest distributions.
- [Douyin XingTu KOL Price](/apis/douyin/xingtu/kol-service-price-v1): Get the XingTu rate card of a Douyin KOL: price per collaboration type (sponsored video, live and more), settlement type and industry tags.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-cp-info-v1.json`](../../../../catalog/models/douyin/xingtu/kol-cp-info-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-cp-info-v1
