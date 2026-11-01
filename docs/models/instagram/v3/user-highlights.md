# Instagram User Highlights (V3)

`instagram/v3/user-highlights` · api · Instagram

Returns profile highlights for a specified Instagram account. Supports forward and backward cursor-based pagination to browse collections.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-highlights", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-highlights', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-highlights", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-highlights", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-highlights` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `last` | integer |  | Highlights per page for backward pagination, use with `before`  |
| `after` | string |  | Forward pagination cursor, from previous response `data.page_info.end_cursor`  |
| `first` | integer |  | Number of highlights per page (default 10, max 50) default `10`; range 1–50 |
| `before` | string |  | Backward pagination cursor, from previous response `data.page_info.start_cursor`  |
| `username` | string | yes | Instagram username (required)  |

## Details

Retrieve highlight collections for an account by providing `username`. Navigate through result pages using `first`, `after`, `before`, and `last`.

### Use cases

- Display story highlight reels from an account profile.
- Archive story highlight collections for creator monitoring.
- Navigate paginated highlight feeds across public profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-highlights" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |
| `last` | integer | No | Highlights per page for backward pagination, use with `before` |
| `after` | string | No | Forward pagination cursor, from previous response `data.page_info.end_cursor` |
| `first` | integer | No | Number of highlights per page (default 10, max 50) |
| `before` | string | No | Backward pagination cursor, from previous response `data.page_info.start_cursor` |

### Notes

- `first` sets the number of highlights returned per page (default 10, max 50).
- Use `after` with `data.page_info.end_cursor` from the previous response for forward pagination.
- Use `before` with `last` and `data.page_info.start_cursor` for backward pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-highlights.json`](../../../../catalog/models/instagram/v3/user-highlights.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-highlights
