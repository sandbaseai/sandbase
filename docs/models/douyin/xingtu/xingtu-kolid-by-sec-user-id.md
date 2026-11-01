# Douyin XingTu kolId Lookup

`douyin/xingtu/xingtu-kolid-by-sec-user-id` · api · Douyin

Convert a Douyin user's sec_user_id into the XingTu kolId used by the XingTu KOL profile, price, fan portrait and performance APIs.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/xingtu-kolid-by-sec-user-id", "sec_user_id": "MS4wLjABAAAAXakJHNxB0cmKZ6c6FthE2_vA7he6kHmgSBp9YjggHR8"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/xingtu-kolid-by-sec-user-id', {'sec_user_id': 'MS4wLjABAAAAXakJHNxB0cmKZ6c6FthE2_vA7he6kHmgSBp9YjggHR8'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/xingtu-kolid-by-sec-user-id", {
  "sec_user_id": "MS4wLjABAAAAXakJHNxB0cmKZ6c6FthE2_vA7he6kHmgSBp9YjggHR8"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/xingtu-kolid-by-sec-user-id", sandbase.Params{
	"sec_user_id": "MS4wLjABAAAAXakJHNxB0cmKZ6c6FthE2_vA7he6kHmgSBp9YjggHR8",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/xingtu-kolid-by-sec-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_user_id` | string | yes | sec_user_id, can be obtained from the following interfaces: `douyin/web/user-profile`; `douyin/web/user-profile-v2`; `douyin/web/user-profile-v3`; `douyin/app-v3/user-profile`  |

## Details

Pass a Douyin `sec_user_id` and get the creator's XingTu `kolId`, plus basic tags.

### Use cases

- First step before calling any XingTu KOL API.
- Check whether a creator is on XingTu.
- Map Douyin accounts to marketplace IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/xingtu-kolid-by-sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAXakJHNxB0cmKZ6c6FthE2_vA7he6kHmgSBp9YjggHR8"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | sec_user_id, can be obtained from the following interfaces: `douyin/web/user-profile`; `douyin/web/user-profile-v2`; `d… |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "id": "7038603512770461703",
  "core_user_id": "93153724393",
  "nick_name": "<user>",
  "tag": "萌宠",
  "finish_rate_ovr": 0.9637
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin XingTu KOL Profile](/model/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.
- [Douyin XingTu KOL Cost Metrics](/model/douyin/xingtu/kol-cp-info-v1): Get expected campaign metrics for a Douyin KOL from XingTu: expected views, CPM and CPE estimates, and hot-video counts.
- [Douyin XingTu KOL Audience](/model/douyin/xingtu/kol-fans-portrait-v1): Get the audience portrait of a Douyin KOL from XingTu: fan age, gender, region, device and interest distributions.

---
Machine-readable: [`catalog/models/douyin/xingtu/xingtu-kolid-by-sec-user-id.json`](../../../../catalog/models/douyin/xingtu/xingtu-kolid-by-sec-user-id.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/xingtu-kolid-by-sec-user-id
