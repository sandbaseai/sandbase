# Douyin XingTu KOL ID by User ID API: pricing, parameters and code examples

`douyin/xingtu/xingtu-kolid-by-uid` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the XingTu creator identifier, nickname, tag, and performance metrics for a specific Douyin account using their Douyin user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/xingtu-kolid-by-uid", "uid": "92769419069"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/xingtu-kolid-by-uid', {'uid': '92769419069'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/xingtu-kolid-by-uid", {
  "uid": "92769419069"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/xingtu-kolid-by-uid", sandbase.Params{
	"uid": "92769419069",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/xingtu-kolid-by-uid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID, can be obtained from the following interfaces: `douyin/web/user-profile-by-uid`; `douyin/web/user-profile-by-short-id`; `douyin/web/user-profile`; `douyin/web/user-profile-v2`; `douyin/web/user-profile-v3`;…  |

## Details

Returns the XingTu creator record for a Douyin account, including the XingTu creator ID, nickname, and content tag. It needs the Douyin user ID in `uid`.

### Use cases

- Convert a Douyin `uid` into the XingTu `id` so you can call other XingTu creator APIs.
- Read the creator's `tag` to sort a list of accounts by content category.
- Check whether a Douyin account has a XingTu creator record before you start a brand outreach workflow.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/xingtu-kolid-by-uid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID, can be obtained from the following interfaces: `douyin/web/user-profile-by-uid`; `douyin/web/user-profile-by-short-id`; `douyin/web/user-profile`; `douyin/web/user-profile-v2`; `douyin/web/user-profile-v3`; `dou |

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
| `id` | The XingTu creator ID for this account. Pass this value to other XingTu creator APIs. |
| `core_user_id` | The Douyin user ID of the account. It matches the `uid` you sent. |
| `nick_name` | The creator's display name on XingTu. |
| `tag` | The creator's content category label, for example `教育培训` (education and training). |
| `avatar_uri` | URL of the creator's avatar image. |
| `finish_rate_ovr` | A numeric completion rate metric for the creator. The sample response returns `0`. |
| `hot_list_ranks` | List of hot list rankings for the creator. The sample response returns an empty list. |
| `base_resp.status_code / base_resp.status_message` | Result status of the lookup. `0` and `Success` mean the call worked. |

### Notes

- Get `uid` from [Douyin User Profile (App V3)](/apis/douyin/app-v3/user-profile) or from the other Douyin profile APIs listed in the `uid` parameter description.
- The `id` in the response is a long numeric string. Keep it as a string to avoid precision loss.
- Use the returned `id` as the creator ID in [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1) or [Douyin XingTu KOL Price](/apis/douyin/xingtu/kol-service-price-v1).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/apis/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/xingtu-kolid-by-uid.json`](../../../../catalog/models/douyin/xingtu/xingtu-kolid-by-uid.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/xingtu-kolid-by-uid
