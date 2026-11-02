# Douyin Xingtu KOL Touch Distribution API: pricing, parameters and code examples

`douyin/xingtu/kol-touch-distribution-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Returns touch distribution data for a Douyin Xingtu creator using their unique KOL identifier. Helps evaluate audience contact points and reach patterns.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-touch-distribution-v1", "kolId": "<kolId>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-touch-distribution-v1', {'kolId': '<kolId>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-touch-distribution-v1", {
  "kolId": "<kolId>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-touch-distribution-v1", sandbase.Params{
	"kolId": "<kolId>",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-touch-distribution-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |

## Details

Returns touch distribution metrics for a specified Douyin Xingtu creator by querying their `kolId`.

### Use cases

- Analyze audience touchpoint patterns for specific Douyin creators.
- Evaluate creator reach distribution before planning marketing campaigns.
- Track audience contact frequency across different creator profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-touch-distribution-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "<kolId>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xin… |

### Notes

- Obtain `kolId` from endpoints such as `douyin/xingtu/xingtu-kolid-by-uid`, `douyin/xingtu/xingtu-kolid-by-sec-user-id`, or `douyin/xingtu/xingtu-kolid-by-unique-id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/model/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/model/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/model/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-touch-distribution-v1.json`](../../../../catalog/models/douyin/xingtu/kol-touch-distribution-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-touch-distribution-v1
