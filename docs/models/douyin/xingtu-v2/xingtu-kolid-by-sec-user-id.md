# Douyin XingTu kolId by sec_user_id (V2) API: pricing, parameters and code examples

`douyin/xingtu-v2/xingtu-kolid-by-sec-user-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns Xingtu creator identifiers and basic profile metrics for a Douyin account using its secure user ID. It provides the Xingtu author ID, core user ID, and performance indicators.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/xingtu-kolid-by-sec-user-id", "sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/xingtu-kolid-by-sec-user-id', {'sec_user_id': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/xingtu-kolid-by-sec-user-id", {
  "sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/xingtu-kolid-by-sec-user-id", sandbase.Params{
	"sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_user_id` | string | yes | Douyin user sec_user_id, obtainable from Douyin user-profile endpoints  |

## Details

Returns the Xingtu creator ID and basic profile data for a Douyin account. It needs one input, the account's `sec_user_id`.

### Use cases

- Map a Douyin account to its Xingtu author ID before calling other Xingtu APIs.
- Match a creator's `core_user_id` with records from other Douyin data sources.
- Check a creator's profile tag and `finish_rate_ovr` value when screening influencers for a campaign.
- Check whether a creator appears on Xingtu hot lists by reading `hot_list_ranks`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | Douyin user sec_user_id, obtainable from Douyin user-profile endpoints |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "avatar_uri": "https://p11.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_9186d2f6f…",
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "core_user_id": "3635433641882579",
  "finish_rate_ovr": 0.6146,
  "hot_list_ranks": [],
  "id": "7452669161240526898",
  "nick_name": "栗子味",
  "tag": "时尚"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | The Xingtu author ID (kolId) of the creator. Pass this value to other Xingtu APIs that ask for an author ID. |
| `core_user_id` | The core Douyin user ID of the account, returned as a string. |
| `nick_name` | The creator's display name. |
| `tag` | The creator's category tag, for example `时尚` (fashion). |
| `finish_rate_ovr` | A rate between 0 and 1 returned as a decimal. The key name suggests an overall finish (completion) rate. |
| `hot_list_ranks` | List of hot list rankings for the creator. It is empty when the creator has no ranking. |
| `avatar_uri` | URL of the creator's avatar image. |
| `base_resp.status_code / base_resp.status_message` | Status of the lookup. `0` and `Success` mean the call worked. |

### Notes

- Get `sec_user_id` from a Douyin user profile endpoint. It is a long string that starts with `MS4w`.
- Use the returned `id` as the author ID in related APIs such as [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info) or [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution).
- If you have a Douyin ID instead of a `sec_user_id`, use [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id.json`](../../../../catalog/models/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id
