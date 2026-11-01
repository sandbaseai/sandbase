# Douyin XingTu KOL Audience

`douyin/xingtu/kol-fans-portrait-v1` · api · Douyin

Get the audience portrait of a Douyin KOL from XingTu: fan age, gender, region, device and interest distributions.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-fans-portrait-v1", "kolId": "7038603512770461703"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-fans-portrait-v1', {'kolId': '7038603512770461703'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-fans-portrait-v1", {
  "kolId": "7038603512770461703"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-fans-portrait-v1", sandbase.Params{
	"kolId": "7038603512770461703",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-fans-portrait-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |
| `fansType` | string |  | Fans Type, supports the following parameters: _1: Fans Portrait - Default; _2: Fans Group Portrait; _5: Iron Fans Portrait  |

## Details

Pass a XingTu `kolId` and get the demographics of the creator's fans.

### Use cases

- Check that a creator's audience matches your target customers.
- Compare audiences across KOLs.
- Plan region-specific campaigns.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-fans-portrait-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7038603512770461703"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-k… |
| `fansType` | string | No | Fans Type, supports the following parameters: _1: Fans Portrait - Default; _2: Fans Group Portrait; _5: Iron Fans Portr… |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "distributions": [
    {
      "type_display": "年龄分布",
      "description": "18到23岁居多,占比34%",
      "distribution_list": [
        {
          "distribution_key": "24-30",
          "distribution_value": "175378"
        },
        {
          "distribution_key": "50+",
          "distribution_value": "82955"
        },
        {
          "distribution_key": "31-40",
          "distribution_value": "155328"
        }
      ]
    },
    "…"
  ]
}
```

### Notes

- `fansType`: `_1` fans portrait (default), `_2` fan-group portrait, `_5` loyal fans.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin XingTu KOL Profile](/model/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.
- [Douyin XingTu KOL Cost Metrics](/model/douyin/xingtu/kol-cp-info-v1): Get expected campaign metrics for a Douyin KOL from XingTu: expected views, CPM and CPE estimates, and hot-video counts.
- [Douyin XingTu KOL Price](/model/douyin/xingtu/kol-service-price-v1): Get the XingTu rate card of a Douyin KOL: price per collaboration type (sponsored video, live and more), settlement type and industry tags.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-fans-portrait-v1.json`](../../../../catalog/models/douyin/xingtu/kol-fans-portrait-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-fans-portrait-v1
