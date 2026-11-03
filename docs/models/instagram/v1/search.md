# Instagram Keyword Search API: pricing, parameters and code examples

`instagram/v1/search` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Instagram users, hashtags, or places matching a search keyword. Filter results by specific target types using an optional filter parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/search", "query": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/search', {'query': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/search", {
  "query": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/search", sandbase.Params{
	"query": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword  |
| `select` | string |  | Filter type (optional)  |

## Details

Returns Instagram accounts that match a search keyword, with a position for each result and basic account details. It needs one input, `query`. An optional `select` value limits the result type, for example to `hashtags`.

### Use cases

- Find the official Instagram account of a brand by searching its name and checking `full_name` and `id`.
- Collect the numeric user IDs of accounts that match a topic keyword, then feed them to a profile lookup.
- Check whether similar-looking accounts exist for a name before you pick one to track.
- Page through a long list of matches for a keyword using the returned page token.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |
| `select` | string | No | Filter type (optional) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "133",
  "clear_client_cache": false,
  "has_more": true,
  "num_results": 20,
  "page_token": "a53f91e3…",
  "status": "ok",
  "users": [
    {
      "position": 0,
      "user": {
        "account_badges": [],
        "aigm_account_label_info": {
          "is_auto_detected": false,
          "is_enabled": false,
          "is_manually_enabled": false
        },
        "fbid_v2": 17841445531001821,
        "friendship_status": {
          "following": false,
          "incoming_request": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "outgoing_request": false
        },
        "full_name": "OpenAI",
        "has_anonymous_profile_picture": false,
        "id": "45374573700",
        "is_private": false
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `users[].position` | Zero-based rank of the result in the list. |
| `users[].user.id` | Instagram user ID as a string. Use it in APIs that look up a user by ID. |
| `users[].user.full_name` | Display name of the account. |
| `users[].user.is_private` | Whether the account is private. |
| `users[].user.fbid_v2` | Numeric Facebook-side ID attached to the account. |
| `users[].user.friendship_status.following / users[].user.friendship_status.is_restricted` | Relationship flags between the searching account and the result. Each is a boolean. |
| `num_results` | Number of results in this response. |
| `has_more` | Whether more results are available after this page. |
| `page_token` | Token for the next page of results. |
| `status` | Status of the call. `ok` means it succeeded. |

### Notes

- `query` is any search keyword, such as a brand or topic name. Set `select` to a value like `hashtags` to limit the result type.
- When `has_more` is `true`, use the `page_token` value to continue. The response does not show the name of the request parameter that accepts it.
- The `id` values are strings. Pass one to [Instagram User Profile by ID](/apis/instagram/v1/user-info-by-id) to get the full profile.
- To list posts for a hashtag you found, call [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/search.json`](../../../../catalog/models/instagram/v1/search.json) · Store page: https://www.sandbase.ai/model/instagram/v1/search
