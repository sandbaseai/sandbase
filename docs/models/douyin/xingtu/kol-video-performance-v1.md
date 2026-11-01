# Douyin XingTu KOL Video Performance

`douyin/xingtu/kol-video-performance-v1` · api · Douyin

Get a Douyin KOL's video performance from XingTu: interaction and play benchmarks versus peers, plus recent videos with likes, plays, comments and shares.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-video-performance-v1", "kolId": "7038603512770461703", "onlyAssign": false}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-video-performance-v1', {'kolId': '7038603512770461703', 'onlyAssign': False})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-video-performance-v1", {
  "kolId": "7038603512770461703",
  "onlyAssign": false
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-video-performance-v1", sandbase.Params{
	"kolId": "7038603512770461703",
	"onlyAssign": false,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-video-performance-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |
| `onlyAssign` | boolean | yes | Whether to display only assigned works, the specific parameters are as follows: false: Show all, including personal works and assigned works, default value; true: Only display assigned works from XingTu  |

## Details

Pass a XingTu `kolId` and get how the creator's recent videos perform, including benchmarks against similar creators.

### Use cases

- Evaluate a creator's content quality before hiring.
- Compare sponsored vs organic performance (`onlyAssign`).
- Track creator performance trends.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-video-performance-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7038603512770461703", "onlyAssign": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-k… |
| `onlyAssign` | boolean | Yes | Whether to display only assigned works, the specific parameters are as follows: false: Show all, including personal wor… |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data_description": {
    "interaction": {
      "compare_author": 0.92,
      "compare_avg": 0.0756,
      "rate": 0.1285
    },
    "interaction_enrollment": {
      "compare_author": 0,
      "compare_avg": -0.0806,
      "rate": 0
    }
  },
  "latest_star_item_info": [
    {
      "item_id": "7688652613072028323",
      "item_date": "2026-09-23",
      "duration": 85,
      "like": 9370,
      "play": 421301,
      "comment": 33,
      "share": 2285,
      "item_title": "经历了才明白，它能正常嘘嘘有多珍贵！ #皇家处方粮#尿闭#应激#爪住夏天每一帧…"
    }
  ]
}
```

### Notes

- `onlyAssign`: `false` all videos, `true` sponsored (XingTu-assigned) videos only.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin XingTu KOL Profile](/model/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.
- [Douyin XingTu KOL Cost Metrics](/model/douyin/xingtu/kol-cp-info-v1): Get expected campaign metrics for a Douyin KOL from XingTu: expected views, CPM and CPE estimates, and hot-video counts.
- [Douyin XingTu KOL Audience](/model/douyin/xingtu/kol-fans-portrait-v1): Get the audience portrait of a Douyin KOL from XingTu: fan age, gender, region, device and interest distributions.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-video-performance-v1.json`](../../../../catalog/models/douyin/xingtu/kol-video-performance-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-video-performance-v1
