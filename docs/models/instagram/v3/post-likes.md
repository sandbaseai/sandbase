# Instagram Post Likes (V3) API: pricing, parameters and code examples

`instagram/v3/post-likes` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns a list of users who liked a specific Instagram post. Queries engagement details using the unique post shortcode from the post URL.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/post-likes", "code": "Dd9RyBWBVih"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/post-likes', {'code': 'Dd9RyBWBVih'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/post-likes", {
  "code": "Dd9RyBWBVih"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/post-likes", sandbase.Params{
	"code": "Dd9RyBWBVih",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/post-likes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` | string | yes | Post shortcode (from post URL, e.g. instagram.com/p/{code}/)  |

## Details

Retrieve the profiles of users who liked a specific Instagram post by providing the post shortcode via `code`.

### Use cases

- Inspect audience engagement on public Instagram posts.
- Gather profile details of accounts interacting with specific media.
- Track liking activity across brand campaigns.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/post-likes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code": "Dd9RyBWBVih"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | string | Yes | Post shortcode (from post URL, e.g. instagram.com/p/{code}/) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "users": [
    {
      "full_name": "Balaji Mallaiyan",
      "id": "21708437252",
      "pk_id": "21708437252",
      "profile_pic_id": "3874493532866832816_21708437252",
      "profile_pic_url": "https://instagram.fpit1-1.fna.fbcdn.net/v/t51.82787-19/670562331_181186270157252…",
      "username": "<user>",
      "friendship_status": {
        "following": false
      }
    }
  ]
}
```

### Notes

- Provide the post shortcode in `code`, extracted from the URL path (e.g. instagram.com/p/{code}/).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/post-likes.json`](../../../../catalog/models/instagram/v3/post-likes.json) · Store page: https://www.sandbase.ai/model/instagram/v3/post-likes
