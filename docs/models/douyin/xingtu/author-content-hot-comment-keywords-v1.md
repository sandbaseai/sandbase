# Douyin Xingtu Author Hot Comment Keywords API: pricing, parameters and code examples

`douyin/xingtu/author-content-hot-comment-keywords-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Returns hot comment keywords from content produced by a Douyin Xingtu creator. Queries data using the creator's KOL identifier.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/author-content-hot-comment-keywords-v1", "kolId": "7048929565493690398"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/author-content-hot-comment-keywords-v1', {'kolId': '7048929565493690398'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/author-content-hot-comment-keywords-v1", {
  "kolId": "7048929565493690398"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/author-content-hot-comment-keywords-v1", sandbase.Params{
	"kolId": "7048929565493690398",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/author-content-hot-comment-keywords-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |

## Details

Retrieves the most frequent comment keywords across a creator's Douyin Xingtu content using their `kolId`.

### Use cases

- Analyze audience sentiment and discussion trends on creator videos.
- Evaluate audience engagement topics before sponsoring creator content.
- Track recurring keywords and themes in Douyin Xingtu video comments.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/author-content-hot-comment-keywords-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "<kolId>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xin… |

### Notes

- The required `kolId` can be retrieved using the Xingtu KOL ID lookup endpoints by UID, sec_user_id, or unique ID.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/model/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/model/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.
- [Douyin XingTu KOL Profile](/model/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.

---
Machine-readable: [`catalog/models/douyin/xingtu/author-content-hot-comment-keywords-v1.json`](../../../../catalog/models/douyin/xingtu/author-content-hot-comment-keywords-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/author-content-hot-comment-keywords-v1
