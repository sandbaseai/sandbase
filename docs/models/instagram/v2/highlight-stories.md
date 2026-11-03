# Instagram Highlight Stories API: pricing, parameters and code examples

`instagram/v2/highlight-stories` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns all stories contained within a specific Instagram highlight using its unique identifier. Requires an existing highlight ID obtained from user highlight endpoints.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/highlight-stories", "highlight_id": "17895069621772257"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/highlight-stories', {'highlight_id': '17895069621772257'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/highlight-stories", {
  "highlight_id": "17895069621772257"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/highlight-stories", sandbase.Params{
	"highlight_id": "17895069621772257",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/highlight-stories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `highlight_id` | string | yes | Highlight ID (with or without "highlight:" prefix)  |

## Details

Retrieve all story items in an Instagram highlight by providing the `highlight_id`.

### Use cases

- View media and details for stories featured in an account highlight.
- Archive content saved in curated profile highlights.
- Analyze historical stories preserved in public highlights.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/highlight-stories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"highlight_id": "17895069621772257"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `highlight_id` | string | Yes | Highlight ID (with or without "highlight:" prefix) |

### Notes

- Accepts `highlight_id` with or without the "highlight:" prefix.
- Obtain the required `highlight_id` from user highlights endpoints first.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/highlight-stories.json`](../../../../catalog/models/instagram/v2/highlight-stories.json) · Store page: https://www.sandbase.ai/model/instagram/v2/highlight-stories
