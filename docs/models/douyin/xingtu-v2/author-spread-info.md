# Douyin Xingtu Author Spread Info API: pricing, parameters and code examples

`douyin/xingtu-v2/author-spread-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Retrieves commercial spread and reach capability data for a specific creator. Accepts filtering by time range, video type, flow type, and assignment status.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-spread-info", "o_author_id": "6677767167234015243", "range": 2, "type": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-spread-info', {'o_author_id': '6677767167234015243', 'range': 2, 'type': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-spread-info", {
  "o_author_id": "6677767167234015243",
  "range": 2,
  "type": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-spread-info", sandbase.Params{
	"o_author_id": "6677767167234015243",
	"range": 2,
	"type": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-spread-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | integer |  | Video type, 1=personal video  |
| `range` | integer |  | Time range, 2=last 30 days, 3=last 90 days  |
| `flow_type` | integer |  | Flow type, default 0  |
| `o_author_id` | string | yes | Creator/author ID  |
| `only_assign` | boolean |  | Only assigned videos, default False  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Look up commercial spread metrics for a creator on Douyin Xingtu using `o_author_id`. Filter performance stats across specific time windows using `range`.

### Use cases

- Evaluate commercial reach and spread capability for potential influencer partnerships.
- Analyze creator performance across 30-day or 90-day historical time windows.
- Compare personal video metrics against assigned commercial content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-spread-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7589271892177518598"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator/author ID |
| `type` | integer | No | Video type, 1=personal video |
| `range` | integer | No | Time range, 2=last 30 days, 3=last 90 days |
| `flow_type` | integer | No | Flow type, default 0 |
| `only_assign` | boolean | No | Only assigned videos, default False |
| `platform_source` | integer | No | Platform source, default 1 |
| `platform_channel` | integer | No | Platform channel, default 1 |

### Notes

- Use `range` to set the time window: 2 for the last 30 days, or 3 for the last 90 days.
- Set `type` to 1 to filter for personal video spread data.
- The `only_assign` flag filters exclusively for assigned videos when set to true.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-spread-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-spread-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-spread-info
