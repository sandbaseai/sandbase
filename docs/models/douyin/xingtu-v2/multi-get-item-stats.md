# Douyin Xingtu Batch Video Stats API: pricing, parameters and code examples

`douyin/xingtu-v2/multi-get-item-stats` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.06 per call · **Modes:** sync

Returns batch performance statistics and details for up to 20 videos, including play counts, engagement metrics, and watch durations.

## Pricing

- **$0.06 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/multi-get-item-stats", "item_ids": ["7687093469244621938", "7686796523062249137", "7686841529931612005", "7686502146531783675", "7685975419837331142", "7685632954731224040", "7684504353231549617", "7682996027443604389", "7681673254012674789", "7679017665726767333", "7678315154521558291", "7664189446983601444", "7655247684618425946", "7615169499202358385", "7605141504243990257"], "need_cover_url": true, "platform_source": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/multi-get-item-stats', {'item_ids': ['7687093469244621938', '7686796523062249137', '7686841529931612005', '7686502146531783675', '7685975419837331142', '7685632954731224040', '7684504353231549617', '7682996027443604389', '7681673254012674789', '7679017665726767333', '7678315154521558291', '7664189446983601444', '7655247684618425946', '7615169499202358385', '7605141504243990257'], 'need_cover_url': True, 'platform_source': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/multi-get-item-stats", {
  "item_ids": [
    "7687093469244621938",
    "7686796523062249137",
    "7686841529931612005",
    "7686502146531783675",
    "7685975419837331142",
    "7685632954731224040",
    "7684504353231549617",
    "7682996027443604389",
    "7681673254012674789",
    "7679017665726767333",
    "7678315154521558291",
    "7664189446983601444",
    "7655247684618425946",
    "7615169499202358385",
    "7605141504243990257"
  ],
  "need_cover_url": true,
  "platform_source": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/multi-get-item-stats", sandbase.Params{
	"item_ids": []any{"7687093469244621938", "7686796523062249137", "7686841529931612005", "7686502146531783675", "7685975419837331142", "7685632954731224040", "7684504353231549617", "7682996027443604389", "7681673254012674789", "7679017665726767333", "7678315154521558291", "7664189446983601444", "7655247684618425946", "7615169499202358385", "7605141504243990257"},
	"need_cover_url": true,
	"platform_source": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/multi-get-item-stats` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_ids` | array | yes | Video (item) ID list, up to 20 per call (exceeding returns an error); auto de-dup  |
| `need_cover_url` | boolean |  | Whether to return cover URL, default true  |
| `platform_source` | integer |  | Platform source, default 1  |

## Details

Retrieves detailed metrics and engagement statistics for multiple videos using `item_ids`. Supports optional cover image URLs via `need_cover_url` and source filtering via `platform_source`.

### Use cases

- Track performance statistics across multiple Douyin videos simultaneously.
- Analyze viewer interaction rates and average watch durations for video content.
- Retrieve video details and thumbnail cover links in batch requests.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/multi-get-item-stats" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_ids": "<item_ids>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_ids` | array | Yes | Video (item) ID list, up to 20 per call (exceeding returns an error); auto de-dup |
| `need_cover_url` | boolean | No | Whether to return cover URL, default true |
| `platform_source` | integer | No | Platform source, default 1 |

### Notes

- Accepts up to 20 IDs in `item_ids` per call with automatic deduplication; exceeding this limit returns an error.
- `need_cover_url` defaults to true.
- `platform_source` defaults to 1.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/multi-get-item-stats.json`](../../../../catalog/models/douyin/xingtu-v2/multi-get-item-stats.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/multi-get-item-stats
