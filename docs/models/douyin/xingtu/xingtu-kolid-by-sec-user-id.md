# Douyin XingTu kolId Lookup API: pricing, parameters and code examples

`douyin/xingtu/xingtu-kolid-by-sec-user-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Convert a Douyin user's sec_user_id into the XingTu kolId used by the XingTu KOL profile, price, fan portrait and performance APIs.

## Pricing

- **$0.001 per call** (USD)
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

This API takes a Douyin `sec_user_id` and returns the creator's XingTu ID, called `kolId`, plus a few basic profile values. The `id` field in the response is the value other XingTu APIs ask for.

### Use cases

- Convert a Douyin account into a XingTu `kolId` before you request its profile, price or audience data.
- Check whether a Douyin creator has a XingTu entry by looking for a returned `id`.
- Read a creator's XingTu category tag, such as `萌宠`, to sort accounts into niches.
- Match Douyin accounts from your own list to XingTu IDs in bulk.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/xingtu-kolid-by-sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAXakJHNxB0cmKZ6c6FthE2_vA7he6kHmgSBp9YjggHR8"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | sec_user_id, can be obtained from the following interfaces: `douyin/web/user-profile`; `douyin/web/user-profile-v2`; `douyin/web/user-profile-v3`; `douyin/app-v3/user-profile` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "avatar_uri": "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_8c900db621…",
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "core_user_id": "93153724393",
  "finish_rate_ovr": 0.6239,
  "hot_list_ranks": [],
  "id": "7038603512770461703",
  "nick_name": "是甜口的鸭蛋",
  "tag": "萌宠"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | The XingTu `kolId` for the creator. Pass this value to the other XingTu KOL APIs. |
| `core_user_id` | A numeric user ID for the creator, returned as a string. |
| `nick_name` | The creator's display name on Douyin. |
| `tag` | The creator's category tag on XingTu. The sample value `萌宠` means pets. |
| `finish_rate_ovr` | A rate between 0 and 1 returned for the creator. The sample value is `0.6239`. The name suggests an overall finish rate. |
| `avatar_uri` | URL of the creator's avatar image. |
| `hot_list_ranks` | List of hot list rankings for the creator. It is empty in the sample response. |
| `base_resp.status_code / base_resp.status_message` | Status of the request. `0` and `Success` mean the lookup worked. |

### Notes

- Get `sec_user_id` from `douyin/web/user-profile`, `douyin/web/user-profile-v2`, `douyin/web/user-profile-v3` or `douyin/app-v3/user-profile`.
- Use the returned `id` as the `kolId` input for [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1), [Douyin XingTu KOL Price](/apis/douyin/xingtu/kol-service-price-v1) and [Douyin XingTu KOL Audience](/apis/douyin/xingtu/kol-fans-portrait-v1).
- If you only have a user ID or unique ID, use [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid) instead.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.
- [Douyin XingTu KOL Cost Metrics](/apis/douyin/xingtu/kol-cp-info-v1): Get expected campaign metrics for a Douyin KOL from XingTu: expected views, CPM and CPE estimates, and hot-video counts.
- [Douyin XingTu KOL Audience](/apis/douyin/xingtu/kol-fans-portrait-v1): Get the audience portrait of a Douyin KOL from XingTu: fan age, gender, region, device and interest distributions.

---
Machine-readable: [`catalog/models/douyin/xingtu/xingtu-kolid-by-sec-user-id.json`](../../../../catalog/models/douyin/xingtu/xingtu-kolid-by-sec-user-id.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/xingtu-kolid-by-sec-user-id
