# Threads Profile Search API: pricing, parameters and code examples

`threads/web/search-profiles` · data API · Threads · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Searches Threads user profiles based on a specified text query string. Returns matching user accounts and profile information from the platform.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/search-profiles", "query": "mark"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/search-profiles', {'query': 'mark'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/search-profiles", {
  "query": "mark"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/search-profiles", sandbase.Params{
	"query": "mark",
})
```

Same call via the path form: `POST /v1/api/threads/web/search-profiles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query, for example: mark  |

## Details

Returns a list of Threads user accounts that match a text query. You send one `query` string, such as a name or handle, and get back each match with its username, display name, ID, and verification status.

### Use cases

- Find the official Threads account for a brand by searching its name.
- Collect candidate accounts for a keyword to review who uses similar handles.
- Resolve a handle to a numeric user ID before calling other Threads APIs.
- Check whether a matched account is verified and active on Threads.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/search-profiles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query, for example: mark |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "xdt_api__v1__users__search_connection": {
    "edges": [
      {
        "node": {
          "full_name": "OpenAI",
          "has_onboarded_to_text_post_app": true,
          "id": "63299409527",
          "is_active_on_text_post_app": true,
          "is_verified": true,
          "pk": "63299409527",
          "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/788716177_18115256264517…",
          "username": "openai"
        }
      }
    ],
    "inform_module": null
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `xdt_api__v1__users__search_connection.edges[].node.username` | The Threads handle of the matched account, such as `openai`. |
| `xdt_api__v1__users__search_connection.edges[].node.full_name` | The display name shown on the profile. |
| `xdt_api__v1__users__search_connection.edges[].node.id / pk` | The numeric user ID as a string. Both keys hold the same value in the sample. |
| `xdt_api__v1__users__search_connection.edges[].node.is_verified` | Whether the account carries a verified flag. |
| `xdt_api__v1__users__search_connection.edges[].node.is_active_on_text_post_app` | Whether the account is marked active on Threads. |
| `xdt_api__v1__users__search_connection.edges[].node.has_onboarded_to_text_post_app` | Whether the account has completed onboarding to Threads. |
| `xdt_api__v1__users__search_connection.edges[].node.profile_pic_url` | A link to the profile picture image. |

### Notes

- The only input is `query`. A name or handle both work as search text.
- Results are not exact matches only. A search for `OpenAI` also returned accounts like `choi.openai` and `openani.me`, so compare `username` before you pick one.
- Use `id` or `pk` as the user ID in [Threads User Info by ID](/apis/threads/web/user-info-by-id), or the `username` in [Threads User Profile](/apis/threads/web/user-info).
- To read an account's content, pass the match to [Threads User Posts](/apis/threads/web/user-posts).

### Pricing

$0.003 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Threads Post Detail](/apis/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Post Detail (V2)](/apis/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Recent Content Search](/apis/threads/web/search-recent): Searches recent Threads content matching a specified keyword query.

---
Machine-readable: [`catalog/models/threads/web/search-profiles.json`](../../../../catalog/models/threads/web/search-profiles.json) · Store page: https://www.sandbase.ai/model/threads/web/search-profiles
