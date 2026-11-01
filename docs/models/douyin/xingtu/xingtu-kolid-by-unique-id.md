# Douyin XingTu KOL ID by Unique ID

`douyin/xingtu/xingtu-kolid-by-unique-id` · api · Douyin

Returns a Douyin XingTu KOL identifier and profile summary for a given account unique identifier. Useful for mapping public user accounts to XingTu creator data.

## Pricing

- **$0.0015 per call** (USD)
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

Look up a creator's XingTu KOL ID using their Douyin `unique_id`.

### Use cases

- Map standard Douyin user accounts to their XingTu commercial creator profiles.
- Retrieve core user identifiers and profile categories for influencer marketing analysis.
- Check influencer performance metrics such as task completion rates on XingTu.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/xingtu-kolid-by-unique-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"unique_id": "dyczxzs"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `unique_id` | string | Yes | unique_id, can be obtained from the following interfaces: `douyin/web/user-profile`; `douyin/web/user-profile-v2`; `douyin/web/user-profile-v3`; `douyin/app-v3… |

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

- The `unique_id` parameter can be obtained from Douyin user profile endpoints such as `douyin/web/user-profile` or `douyin/app-v3/user-profile`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/model/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/model/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/model/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/xingtu-kolid-by-unique-id.json`](../../../../catalog/models/douyin/xingtu/xingtu-kolid-by-unique-id.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/xingtu-kolid-by-unique-id
