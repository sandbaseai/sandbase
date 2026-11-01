# Douyin Xingtu Author Business Card Info

`douyin/xingtu-v2/author-business-card-info` · api · Douyin

Returns business card details for a Douyin Xingtu creator based on the specified author ID. Useful for reviewing creator profile summaries and business contact information.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-business-card-info", "o_author_id": "7589271892177518598"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-business-card-info', {'o_author_id': '7589271892177518598'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-business-card-info", {
  "o_author_id": "7589271892177518598"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-business-card-info", sandbase.Params{
	"o_author_id": "7589271892177518598",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-business-card-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `o_author_id` | string | yes | Creator/author ID  |

## Details

Retrieves business card information for a creator using the `o_author_id` parameter. Use it to inspect creator credentials on the Douyin Xingtu platform.

### Use cases

- Retrieve creator business card details on Xingtu.
- Review creator background before initiating brand collaborations.
- Verify author profile card attributes by author ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-business-card-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "<o_author_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator/author ID |

### Notes

- Requires the creator ID passed via `o_author_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Content Hot Keywords](/model/douyin/xingtu-v2/author-content-hot-keywords): Returns trending content keywords for a Douyin creator.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-business-card-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-business-card-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-business-card-info
