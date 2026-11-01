# Douyin Xingtu Author Cooperation Info

`douyin/xingtu-v2/author-cp-info` · api · Douyin

Returns Douyin Xingtu creator cooperation details for a specified author ID. Query profile and partnership data using creator IDs alongside optional platform channel filters.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-cp-info", "o_author_id": "6677767167234015243"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-cp-info', {'o_author_id': '6677767167234015243'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-cp-info", {
  "o_author_id": "6677767167234015243"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-cp-info", sandbase.Params{
	"o_author_id": "6677767167234015243",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-cp-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Retrieve Douyin Xingtu creator cooperation details by querying `o_author_id`. You can also configure optional platform source and channel options to target specific partner data.

### Use cases

- Review creator collaboration statistics before launching marketing campaigns.
- Inspect commercial cooperation profiles for Douyin Xingtu authors.
- Evaluate influencer partnership data across specific platform channels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-cp-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "<o_author_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `platform_source` | integer | No | Platform source, default 1 |
| `platform_channel` | integer | No | Platform channel, default 1 |

### Notes

- `platform_source` defaults to 1 if not specified.
- `platform_channel` defaults to 1 if not specified.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-cp-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-cp-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-cp-info
