# Instagram User Details by ID (V2) API: pricing, parameters and code examples

`instagram/v1/user-info-by-id-v2` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed Instagram user information including bio links by providing an account identifier. Query the endpoint using an Instagram user ID to inspect profile metadata.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-info-by-id-v2", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-info-by-id-v2', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-info-by-id-v2", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-info-by-id-v2", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-info-by-id-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Instagram user ID  |

## Details

Returns profile details for one Instagram account, including follower and following counts, biography, verification status and the list of links in the bio. It needs the numeric Instagram user ID in `user_id`.

### Use cases

- Read the follower count and following count of an account from its numeric ID.
- Collect every link in a creator's bio, with its title and destination URL.
- Check whether an account is verified, private or a business account before you add it to a list.
- Get the HD profile picture URL and display name for an account you only know by ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-info-by-id-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "account_badges": [],
  "account_type": 3,
  "address_street": null,
  "aigm_account_label_info": null,
  "attempts": "0",
  "bio_links": [
    {
      "creation_source": "NONE",
      "image_url": "",
      "is_pinned": false,
      "link_type": "external",
      "lynx_url": "https://l.instagram.com/?u=https%3A%2F%2Fhelp.instagram.com%2F&e=AUDN5uLwUC61ORj…",
      "media_accent_color_hex": "",
      "media_type": "none",
      "title": "",
      "url": "http://help.instagram.com"
    }
  ],
  "biography": "Discover what's new on Instagram 🔎✨",
  "biography_with_entities": {
    "entities": []
  },
  "category": "",
  "city_name": null,
  "external_lynx_url": "https://l.instagram.com/?u=https%3A%2F%2Fhelp.instagram.com%2F&e=AUCAKRFROoo1ycN…",
  "external_url": "http://help.instagram.com"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Instagram user ID of the account. It matches the `user_id` you sent. |
| `full_name` | Display name shown on the profile. |
| `biography` | Bio text of the profile. |
| `follower_count / following_count` | Number of followers the account has and number of accounts it follows. |
| `is_verified / is_private / is_business` | Flags for verified badge, private account and business account. |
| `bio_links[].url` | Destination URL of each link in the bio. |
| `bio_links[].title` | Label shown for the bio link. It can be an empty string. |
| `bio_links[].lynx_url` | Instagram redirect version of the bio link URL. |
| `external_url` | Main external website URL on the profile. |
| `hd_profile_pic_url_info.url` | URL of the high-resolution profile picture. |

### Notes

- Get the numeric ID from a username with [Instagram User Info by Username](/apis/instagram/v1/user-info-by-username).
- Some fields can return `null`, such as `media_count` and `is_professional_account`. Do not rely on them being filled.
- For a different profile layout from the same ID, try [Instagram User Profile by ID](/apis/instagram/v1/user-info-by-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-info-by-id-v2.json`](../../../../catalog/models/instagram/v1/user-info-by-id-v2.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-info-by-id-v2
