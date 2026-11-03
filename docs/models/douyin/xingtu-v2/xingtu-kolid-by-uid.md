# Douyin Xingtu Author ID by UID API: pricing, parameters and code examples

`douyin/xingtu-v2/xingtu-kolid-by-uid` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns the Xingtu creator identifier and basic profile details for a given Douyin user account. Provide a Douyin user ID to retrieve associated Xingtu platform metadata.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/xingtu-kolid-by-uid", "uid": "92769419069"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/xingtu-kolid-by-uid', {'uid': '92769419069'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/xingtu-kolid-by-uid", {
  "uid": "92769419069"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/xingtu-kolid-by-uid", sandbase.Params{
	"uid": "92769419069",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/xingtu-kolid-by-uid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Douyin user ID, obtainable from Douyin user-profile endpoints  |

## Details

Returns the Xingtu author ID and basic profile details for a Douyin account. It needs one input, the Douyin user ID in `uid`.

### Use cases

- Convert a Douyin user ID into the Xingtu author ID (`id`) so you can call other Xingtu author APIs.
- Check the creator's nickname and category tag before adding them to a campaign shortlist.
- Match a list of Douyin accounts to their Xingtu records in a bulk import.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/xingtu-kolid-by-uid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Douyin user ID, obtainable from Douyin user-profile endpoints |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "avatar_uri": "https://p11.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_3beaaeb52…",
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "core_user_id": "92769419069",
  "finish_rate_ovr": 0,
  "hot_list_ranks": [],
  "id": "6870164585236660237",
  "nick_name": "抖音作者助手",
  "tag": "教育培训"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | The Xingtu author ID for this account. Pass it to other Xingtu author APIs. |
| `core_user_id` | The Douyin user ID you sent in `uid`, returned as a string. |
| `nick_name` | The creator's display name on Douyin. |
| `tag` | The creator's category label, for example `教育培训` (education and training). |
| `avatar_uri` | URL of the creator's avatar image. |
| `finish_rate_ovr` | A completion rate value for the creator. It is `0` in this example. |
| `hot_list_ranks` | List of hot list rankings for the creator. It is empty in this example. |
| `base_resp.status_code / base_resp.status_message` | Status of the lookup. `0` and `Success` mean the call worked. |

### Notes

- Get the `uid` value from a Douyin user-profile API. It is a numeric string.
- The `id` in the response is a long numeric string. Keep it as a string to avoid rounding.
- Use `id` as the author ID in [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info) or [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info).
- If you only have a Douyin ID or a `sec_user_id`, use [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id) instead.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/xingtu-kolid-by-uid.json`](../../../../catalog/models/douyin/xingtu-v2/xingtu-kolid-by-uid.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/xingtu-kolid-by-uid
