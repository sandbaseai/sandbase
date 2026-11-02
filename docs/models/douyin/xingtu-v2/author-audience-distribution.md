# Douyin Xingtu Author Audience Distribution API: pricing, parameters and code examples

`douyin/xingtu-v2/author-audience-distribution` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel options.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-audience-distribution", "link_type": 5, "o_author_id": "7029342444797820939"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-audience-distribution', {'link_type': 5, 'o_author_id': '7029342444797820939'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-audience-distribution", {
  "link_type": 5,
  "o_author_id": "7029342444797820939"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-audience-distribution", sandbase.Params{
	"link_type": 5,
	"o_author_id": "7029342444797820939",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-audience-distribution` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `link_type` |  | yes | Link type, optional  |
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Retrieve audience profile distribution data for Douyin Xingtu creators by passing the creator identifier `o_author_id` and `link_type`.

### Use cases

- Analyze creator audience demographics for brand campaign targeting.
- Evaluate audience profile distributions across candidate Douyin creators.
- Verify target audience alignment prior to campaign collaboration.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-audience-distribution" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "<o_author_id>", "link_type": "<link_type>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `link_type` | string | Yes | Link type, optional |
| `o_author_id` | string | Yes | Creator ID |
| `platform_source` | integer | No | Platform source, default 1 |
| `platform_channel` | integer | No | Platform channel, default 1 |

### Notes

- `platform_source` defaults to 1 when omitted.
- `platform_channel` defaults to 1 when omitted.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.
- [Douyin Xingtu Author Content Hot Keywords](/model/douyin/xingtu-v2/author-content-hot-keywords): Returns trending content keywords for a Douyin creator.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-audience-distribution.json`](../../../../catalog/models/douyin/xingtu-v2/author-audience-distribution.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-audience-distribution
