# Douyin Xingtu Author Base Info API: pricing, parameters and code examples

`douyin/xingtu-v2/author-base-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-base-info", "o_author_id": "6677767167234015243"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-base-info', {'o_author_id': '6677767167234015243'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-base-info", {
  "o_author_id": "6677767167234015243"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-base-info", sandbase.Params{
	"o_author_id": "6677767167234015243",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-base-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `recommend` | boolean |  | Whether to return recommendation info, default True  |
| `o_author_id` | string | yes | Creator/author ID  |
| `need_sec_uid` | boolean |  | Whether to return sec_uid, default True  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |
| `need_linkage_info` | boolean |  | Whether to return linkage info, default True  |

## Details

Fetch foundational profile details for a Douyin Xingtu creator using `o_author_id`. You can configure toggles to include security identifiers, recommendation metadata, and linkage info.

### Use cases

- Look up core creator profile metadata on Douyin Xingtu.
- Retrieve creator sec_uid values for downstream platform requests.
- Inspect author recommendation and linkage data for talent discovery.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-base-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "<o_author_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator/author ID |
| `recommend` | boolean | No | Whether to return recommendation info, default True |
| `need_sec_uid` | boolean | No | Whether to return sec_uid, default True |
| `platform_source` | integer | No | Platform source, default 1 |
| `platform_channel` | integer | No | Platform channel, default 1 |
| `need_linkage_info` | boolean | No | Whether to return linkage info, default True |

### Notes

- `o_author_id` is required to identify the creator.
- `platform_source` and `platform_channel` both default to 1.
- `recommend`, `need_sec_uid`, and `need_linkage_info` default to true.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.
- [Douyin Xingtu Author Content Hot Keywords](/apis/douyin/xingtu-v2/author-content-hot-keywords): Returns trending content keywords for a Douyin creator.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-base-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-base-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-base-info
