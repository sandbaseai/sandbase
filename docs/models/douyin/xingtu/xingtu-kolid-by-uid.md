# Douyin XingTu KOL ID by User ID

`douyin/xingtu/xingtu-kolid-by-uid` · api · Douyin

Returns the XingTu creator identifier, nickname, tag, and performance metrics for a specific Douyin account using their Douyin user ID.

## Pricing

- **$0.0015 per call** (USD)
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

Retrieve a Douyin creator's XingTu platform KOL identifier using their `uid`. This helps link standard Douyin profiles to commercial influencer records.

### Use cases

- Map a standard Douyin user profile to their commercial XingTu influencer ID.
- Inspect creator industry tags on the XingTu marketing platform.
- Check baseline creator metrics before calling detailed XingTu marketing endpoints.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/xingtu-kolid-by-uid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID, can be obtained from the following interfaces: `douyin/web/user-profile-by-uid`; `douyin/web/user-profile-by-short-id`; `douyin/web/user-profile`; `do… |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "core_user_id": "92769419069",
  "finish_rate_ovr": 0,
  "id": "6870164585236660237",
  "nick_name": "<user>",
  "tag": "教育培训"
}
```

### Notes

- Obtain `uid` from Douyin user profile endpoints such as `douyin/web/user-profile-by-uid` or `douyin/app-v3/user-profile`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/model/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/model/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/model/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/xingtu-kolid-by-uid.json`](../../../../catalog/models/douyin/xingtu/xingtu-kolid-by-uid.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/xingtu-kolid-by-uid
