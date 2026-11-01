# Douyin Xingtu Batch Author Details

`douyin/xingtu-v2/multi-get-author-info` · api · Douyin

Returns Xingtu creator profile information for multiple creator accounts in a single request. It takes a list of creator IDs along with optional platform source and channel options.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/multi-get-author-info", "author_ids": "<author_ids>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/multi-get-author-info', {'author_ids': '<author_ids>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/multi-get-author-info", {
  "author_ids": "<author_ids>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/multi-get-author-info", sandbase.Params{
	"author_ids": "<author_ids>",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/multi-get-author-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `author_ids` | array | yes | Creator ID list, up to 50 per call (exceeding returns an error)  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Use this endpoint to retrieve creator profile data for multiple creators at once using `author_ids`.

### Use cases

- Look up Xingtu profile details for multiple creators simultaneously.
- Monitor influencer metadata across creator rosters.
- Enrich creator management records with current Xingtu account details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/multi-get-author-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_ids": "<author_ids>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `author_ids` | array | Yes | Creator ID list, up to 50 per call (exceeding returns an error) |
| `platform_source` | integer | No | Platform source, default 1 |
| `platform_channel` | integer | No | Platform channel, default 1 |

### Notes

- `author_ids` accepts up to 50 creator IDs per call, and exceeding this limit returns an error.
- `platform_source` defaults to 1 when omitted.
- `platform_channel` defaults to 1 when omitted.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/multi-get-author-info.json`](../../../../catalog/models/douyin/xingtu-v2/multi-get-author-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/multi-get-author-info
