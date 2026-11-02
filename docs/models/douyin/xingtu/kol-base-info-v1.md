# Douyin XingTu KOL Profile API: pricing, parameters and code examples

`douyin/xingtu/kol-base-info-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-base-info-v1", "kolId": "7038603512770461703", "platformChannel": "_1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-base-info-v1', {'kolId': '7038603512770461703', 'platformChannel': '_1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-base-info-v1", {
  "kolId": "7038603512770461703",
  "platformChannel": "_1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-base-info-v1", sandbase.Params{
	"kolId": "7038603512770461703",
	"platformChannel": "_1",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-base-info-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |
| `platformChannel` | string | yes | Platform channel, supports the following parameters: _1: Douyin Video; _10: Douyin Live  |

## Details

Pass a XingTu `kolId` and get the creator's marketplace profile: follower count, region, content tags and which collaboration types are open.

### Use cases

- Screen Douyin influencers before a campaign.
- Build a KOL database with categories and regions.
- Combine with price and fan-portrait APIs for full vetting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-base-info-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7038603512770461703", "platformChannel": "_1"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-k… |
| `platformChannel` | string | Yes | Platform channel, supports the following parameters: _1: Douyin Video; _10: Douyin Live |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "id": "7038603512770461703",
  "core_user_id": "93153724393",
  "follower": 886798,
  "city": "长沙市",
  "province": "湖南省",
  "is_star": true,
  "online_status": 1,
  "tags_level_two": "[\"\\u65e5\\u5e38\\u5ba0\\u7269\"]",
  "nick_name": "<user>",
  "sec_uid": "<sec_uid>"
}
```

### Notes

- Get `kolId` from a Douyin `sec_user_id` with the XingTu kolid by sec_user_id API.
- `platformChannel`: `_1` Douyin video, `_10` Douyin live.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin XingTu KOL Cost Metrics](/model/douyin/xingtu/kol-cp-info-v1): Get expected campaign metrics for a Douyin KOL from XingTu: expected views, CPM and CPE estimates, and hot-video counts.
- [Douyin XingTu KOL Audience](/model/douyin/xingtu/kol-fans-portrait-v1): Get the audience portrait of a Douyin KOL from XingTu: fan age, gender, region, device and interest distributions.
- [Douyin XingTu KOL Price](/model/douyin/xingtu/kol-service-price-v1): Get the XingTu rate card of a Douyin KOL: price per collaboration type (sponsored video, live and more), settlement type and industry tags.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-base-info-v1.json`](../../../../catalog/models/douyin/xingtu/kol-base-info-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-base-info-v1
