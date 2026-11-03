# Douyin Xingtu KOL Audience Portrait (V1) API: pricing, parameters and code examples

`douyin/xingtu/kol-audience-portrait-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns audience demographic and portrait insights for a Douyin Xingtu creator. Requires a creator identifier to retrieve detailed follower profile data.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-audience-portrait-v1", "kolId": "6677767167234015243"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-audience-portrait-v1', {'kolId': '6677767167234015243'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-audience-portrait-v1", {
  "kolId": "6677767167234015243"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-audience-portrait-v1", sandbase.Params{
	"kolId": "6677767167234015243",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-audience-portrait-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |

## Details

Look up audience portrait statistics for Douyin Xingtu creators using `kolId`.

### Use cases

- Analyze audience demographics for specific Douyin Xingtu creators.
- Evaluate follower profile alignment before booking marketing campaigns.
- Inspect audience composition metrics across creator accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-audience-portrait-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7048929565493690398"}'
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

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-audience-portrait-v1.json`](../../../../catalog/models/douyin/xingtu/kol-audience-portrait-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-audience-portrait-v1
