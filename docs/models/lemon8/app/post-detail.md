# Lemon8 Post Details API: pricing, parameters and code examples

`lemon8/app/post-detail` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specified Lemon8 post using its unique post ID. Retrieve post metadata and content metrics by providing the target item identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/post-detail", "item_id": "7613037734357123615"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/post-detail', {'item_id': '7613037734357123615'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/post-detail", {
  "item_id": "7613037734357123615"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/post-detail", sandbase.Params{
	"item_id": "7613037734357123615",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Post ID, can be obtained from the interface `/lemon8/app/get_item_id`  |

## Details

Retrieve detailed information for a specific Lemon8 post by supplying `item_id`. This endpoint returns post data and associated metrics for the target post.

### Use cases

- Inspecting detailed metadata and metrics for an individual Lemon8 post.
- Tracking performance analytics on specific Lemon8 content items.
- Displaying Lemon8 post details within external dashboards or applications.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7361926875709129222"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Post ID, can be obtained from the interface `/lemon8/app/get_item_id` |

### Notes

- The `item_id` value can be obtained from the `/lemon8/app/get_item_id` endpoint.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Banners](/model/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/model/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/model/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/post-detail.json`](../../../../catalog/models/lemon8/app/post-detail.json) · Store page: https://www.sandbase.ai/model/lemon8/app/post-detail
