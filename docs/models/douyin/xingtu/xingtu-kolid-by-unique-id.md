# Douyin XingTu KOL ID by Unique ID API: pricing, parameters and code examples

`douyin/xingtu/xingtu-kolid-by-unique-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a Douyin XingTu KOL identifier and profile summary for a given account unique identifier. Useful for mapping public user accounts to XingTu creator data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/xingtu-kolid-by-unique-id", "unique_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/xingtu-kolid-by-unique-id', {'unique_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/xingtu-kolid-by-unique-id", {
  "unique_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/xingtu-kolid-by-unique-id", sandbase.Params{
	"unique_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/xingtu-kolid-by-unique-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `unique_id` | string | yes | unique_id, can be obtained from the following interfaces: `douyin/web/user-profile`; `douyin/web/user-profile-v2`; `douyin/web/user-profile-v3`; `douyin/app-v3/user-profile`  |

## Details

Returns the XingTu KOL ID and a short profile summary for a Douyin account. It needs the account's `unique_id` as input.

### Use cases

- Convert a Douyin `unique_id` into the XingTu `id` needed to call other XingTu creator APIs.
- Match public Douyin accounts to their XingTu creator records when building an influencer list.
- Read the creator's `nick_name` and `tag` category to sort candidate accounts by content niche.
- Link a XingTu creator back to a Douyin account through `core_user_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/xingtu-kolid-by-unique-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"unique_id": "dyczxzs"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `unique_id` | string | Yes | unique_id, can be obtained from the following interfaces: `douyin/web/user-profile`; `douyin/web/user-profile-v2`; `douyin/web/user-profile-v3`; `douyin/app-v3/user-profile` |

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
| `id` | The XingTu KOL ID for the account. Pass this value to other XingTu APIs that take a KOL ID. |
| `core_user_id` | The core user ID of the account, returned as a string. |
| `nick_name` | The creator's display name. |
| `tag` | The creator's content category label, for example `教育培训` (education and training). |
| `finish_rate_ovr` | A numeric completion rate value for the creator. The example returns `0`. |
| `hot_list_ranks[]` | List of hot list rankings for the creator. It is empty in the example. |
| `avatar_uri` | URL of the creator's avatar image. |
| `base_resp.status_code / base_resp.status_message` | Status of the lookup. `0` and `Success` mean the call worked. |

### Notes

- Get `unique_id` from [Douyin User Profile (App V3)](/apis/douyin/app-v3/user-profile) or the `douyin/web/user-profile` family of APIs.
- IDs such as `id` and `core_user_id` come back as strings. Keep them as strings to avoid losing digits.
- Use the returned `id` as the KOL ID input for APIs such as [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1) or [Douyin XingTu KOL Price](/apis/douyin/xingtu/kol-service-price-v1).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/apis/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/xingtu-kolid-by-unique-id.json`](../../../../catalog/models/douyin/xingtu/xingtu-kolid-by-unique-id.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/xingtu-kolid-by-unique-id
