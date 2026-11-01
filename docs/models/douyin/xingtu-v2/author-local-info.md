# Douyin Xingtu Author Location Info

`douyin/xingtu-v2/author-local-info` · api · Douyin

Returns location details for a Douyin Xingtu creator using their author ID, with optional filters for time range and platform settings.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-local-info", "o_author_id": "7146074596666507300"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-local-info', {'o_author_id': '7146074596666507300'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-local-info", {
  "o_author_id": "7146074596666507300"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-local-info", sandbase.Params{
	"o_author_id": "7146074596666507300",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-local-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `time_range` | integer |  | Time range in days, default 30  |
| `o_author_id` | string | yes | Creator/author ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Fetch creator location data on Douyin Xingtu using `o_author_id`. You can adjust the evaluation period via `time_range`.

### Use cases

- Inspect local geographical presence for a Douyin creator.
- Evaluate creator regional distribution over a designated time range.
- Assess creator local audience trends for regional campaign planning.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-local-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "<o_author_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator/author ID |
| `time_range` | integer | No | Time range in days, default 30 |
| `platform_source` | integer | No | Platform source, default 1 |
| `platform_channel` | integer | No | Platform channel, default 1 |

### Notes

- `o_author_id` is required to identify the creator.
- `time_range` sets the duration in days and defaults to 30.
- `platform_source` and `platform_channel` both default to 1.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-local-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-local-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-local-info
