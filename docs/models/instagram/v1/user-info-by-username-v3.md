# Instagram User Profile by Username (V3) API: pricing, parameters and code examples

`instagram/v1/user-info-by-username-v3` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed Instagram user account information, including bio links, by querying an account handle.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/user-info-by-username-v3", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/user-info-by-username-v3', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/user-info-by-username-v3", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/user-info-by-username-v3", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/user-info-by-username-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username  |

## Details

Returns profile data for one Instagram account, including follower and following counts, biography, verification status and the list of links in the bio. It needs one input, the account handle in `username`.

### Use cases

- Read the links in an account's bio, including each link's `title` and `url`, to check where a brand sends its audience.
- Check `follower_count` and `is_verified` for an account before you add it to an influencer list.
- Pull the `id` for a handle so you can call APIs that take a numeric user ID.
- Save the biography text and profile picture URL of an account for a profile card or a brand monitoring record.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/user-info-by-username-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username |

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
      "lynx_url": "https://l.instagram.com/?u=https%3A%2F%2Fhelp.instagram.com%2F&e=AUDalAOqK26dSSL…",
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
  "external_lynx_url": "https://l.instagram.com/?u=https%3A%2F%2Fhelp.instagram.com%2F&e=AUAq3xoFe1w-NbE…",
  "external_url": "http://help.instagram.com"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Numeric Instagram user ID of the account, returned as a string. |
| `full_name` | Display name shown on the profile. |
| `biography` | Bio text of the account. |
| `follower_count / following_count` | Number of accounts that follow this account, and number of accounts it follows. |
| `is_verified / is_private / is_business` | Flags for a verified badge, a private account, and a business account. |
| `bio_links[].url` | Destination URL of each link in the bio. |
| `bio_links[].title` | Label of the bio link. It can be an empty string. |
| `bio_links[].lynx_url` | Instagram redirect version of the link that wraps the destination URL. |
| `external_url` | Main external link shown on the profile. |
| `hd_profile_pic_url_info.url` | URL of the high-resolution profile picture. |

### Notes

- Pass the handle in `username` without the leading @.
- Many fields can come back as `null`, for example `media_count` and `is_professional_account`. Do not rely on them being filled.
- Use the `id` value with [Instagram User Profile by ID](/apis/instagram/v1/user-info-by-id) to look up the same account by its numeric ID.
- To list the account's posts, call [Instagram User Posts (V1)](/apis/instagram/v1/user-posts).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/user-info-by-username-v3.json`](../../../../catalog/models/instagram/v1/user-info-by-username-v3.json) · Store page: https://www.sandbase.ai/model/instagram/v1/user-info-by-username-v3
