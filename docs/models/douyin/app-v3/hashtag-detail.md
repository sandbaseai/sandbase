# Douyin Hashtag Details

`douyin/app-v3/hashtag-detail` · api · Douyin

Retrieves comprehensive information and metadata for a specific Douyin hashtag using its unique challenge identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/hashtag-detail", "ch_id": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/hashtag-detail', {'ch_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/hashtag-detail", {
  "ch_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/hashtag-detail", sandbase.Params{
	"ch_id": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/hashtag-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ch_id` | integer | yes | Hashtag id  |

## Details

Fetch detailed information about a Douyin hashtag by querying its unique identifier with `ch_id`.

### Use cases

- Retrieve metadata and profile details for a Douyin hashtag.
- Monitor engagement metrics associated with specific topic tags.
- Analyze hashtag performance for marketing campaign research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/hashtag-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ch_id": "<ch_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ch_id` | integer | Yes | Hashtag id |

### Notes

- Requires the hashtag identifier supplied via `ch_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/hashtag-detail.json`](../../../../catalog/models/douyin/app-v3/hashtag-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/hashtag-detail
