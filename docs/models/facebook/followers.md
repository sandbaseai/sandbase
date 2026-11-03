# Facebook Followers API: pricing, parameters and code examples

`facebook/followers` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.12 per call · **Modes:** sync

List the public followers (or accounts followed) of any Facebook page or profile URL as normalized JSON records.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.12**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/followers", "url": "https://www.facebook.com/nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/followers', {'url': 'https://www.facebook.com/nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/followers", {
  "url": "https://www.facebook.com/nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/followers", sandbase.Params{
	"url": "https://www.facebook.com/nike",
})
```

Same call via the path form: `POST /v1/api/facebook/followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Facebook page or profile URL to list follows for (e.g. https://www.facebook.com/nasa).  |
| `limit` | integer |  | Maximum number of results to return (1-20, default 20). You are billed per result returned, so a lower limit costs less. range 1–20 |
| `followType` | string |  | Which relation to fetch: 'follower' or 'following' (e.g. follower). default `"follower"` |

## Details

Returns a list of public followers, or accounts followed, for a Facebook page or profile. It needs a Facebook page or profile `url`. Each record has an ID, name, type, profile URL and image URL.

### Use cases

- Sample the public followers of a brand page such as Nike to see what kinds of accounts follow it.
- List the accounts a profile follows by setting `followType` to `following`.
- Collect follower profile URLs to pass to a profile lookup for further research.
- Check whether a page exposes public followers by testing the `found` flag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/nike", "limit": 3}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Facebook page or profile URL to list follows for (e.g. https://www.facebook.com/nasa). |
| `followType` | string | No | Which relation to fetch: 'follower' or 'following' (e.g. follower). |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). You are billed per result returned, so a lower limit costs less. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "id": "100068981584033",
        "image": "https://scontent.fnbo1-2.fna.fbcdn.net/v/t39.30808-1/475753792_917567940552584_4…",
        "name": "Phawulothando",
        "type": "profile",
        "url": "https://www.facebook.com/people/Phawulothando/100068981584033/"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the lookup returned data. A lookup that finds nothing returns `false`. |
| `data.items[]` | One follower or followed account per entry. The list holds at most `limit` entries. |
| `data.items[].id` | Numeric Facebook ID of the follower account, returned as a string. |
| `data.items[].name` | Display name of the follower account. |
| `data.items[].type` | Kind of account. The sample values are `profile`. |
| `data.items[].url` | Facebook URL of the follower account. You can use it as the `url` input in other Facebook APIs. |
| `data.items[].image` | URL of the account's profile picture. |

### Notes

- Set `limit` between 1 and 20. The default is 20.
- Set `followType` to `follower` (default) or `following` to choose the direction.
- To get more detail on an account in the list, pass its `url` to [Facebook Profile](/apis/facebook/profile).
- If you only have a page name and need its ID, use [Facebook Profile ID](/apis/facebook/profile-id).

### Pricing

Billed at the actual cost of each call, about $0.12 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/followers.json`](../../../catalog/models/facebook/followers.json) · Store page: https://www.sandbase.ai/model/facebook/followers
