# Instagram Media ID to Shortcode (V2)

`instagram/v2/media-id-to-shortcode` · api · Instagram

Converts an Instagram post media identifier into its corresponding shortcode. Useful for reconstructing direct post URLs from numeric identifiers.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/media-id-to-shortcode", "media_id": "3774507992167247878"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/media-id-to-shortcode', {'media_id': '3774507992167247878'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/media-id-to-shortcode", {
  "media_id": "3774507992167247878"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/media-id-to-shortcode", sandbase.Params{
	"media_id": "3774507992167247878",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/media-id-to-shortcode` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `media_id` | string | yes | Post media ID  |

## Details

Resolve an Instagram post shortcode from a given `media_id`. This allows building standard post URLs from numeric media identifiers.

### Use cases

- Reconstruct web links for posts stored only by numeric media ID.
- Convert legacy database identifiers into standard Instagram post URLs.
- Prepare link previews by resolving shortcodes for social dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/media-id-to-shortcode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"media_id": "3774507992167247878"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `media_id` | string | Yes | Post media ID |

### Notes

- Requires a valid numeric Instagram post `media_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/media-id-to-shortcode.json`](../../../../catalog/models/instagram/v2/media-id-to-shortcode.json) · Store page: https://www.sandbase.ai/model/instagram/v2/media-id-to-shortcode
