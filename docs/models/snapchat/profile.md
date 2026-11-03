# Snapchat Profile API: pricing, parameters and code examples

`snapchat/profile` · data API · Snapchat · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Fetch a Snapchat user's public profile by username: display name, bio, subscriber count, and recent public content.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "snapchat/profile", "username": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('snapchat/profile', {'username': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("snapchat/profile", {
  "username": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "snapchat/profile", sandbase.Params{
	"username": "nasa",
})
```

Same call via the path form: `POST /v1/api/snapchat/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | The Snapchat username or profile URL to look up (e.g. fcbarcelona or https://www.snapchat.com/add/fcbarcelona).  |

## Details

This API returns the public profile of a Snapchat account: display name, bio, category, subscriber count, and a list of public stories. It needs one input, `username`, which can be a handle or a Snapchat profile URL.

### Use cases

- Track the subscriber count of a brand or public figure on Snapchat over time.
- Check a Snapchat account's bio, category, and linked website before a partnership or outreach.
- Collect story titles and thumbnails to see what an account posts publicly.
- Confirm that a handle exists and map it to its canonical profile URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/snapchat/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | The Snapchat username or profile URL to look up (e.g. fcbarcelona or https://www.snapchat.com/add/fcbarcelona). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "bio": "Explore the universe and discover our home planet with official NASA snaps.",
        "category": "Government Org",
        "displayName": "NASA",
        "handle": "nasa",
        "image": "https://cf-st.sc-cdn.net/aps/bolt/aHR0cHM6Ly9jZi1zdC5zYy1jZG4ubmV0L2QvUVg2VHZkaD…",
        "stories": [
          {
            "id": "ddf02468-ae16-4fc6-b1bc-bde7e1e22218",
            "storyTitle": "Moon Joy",
            "thumbnailUrl": "https://cf-st.sc-cdn.net/d/wAUDrJs74QBAl504N3DhT.410?mo=GjUaFDIBBDoBfUIGCMWw5M4G…"
          }
        ],
        "subscribers": 751900,
        "url": "https://www.snapchat.com/add/nasa",
        "website": "https://www.nasa.gov"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the profile was found. A lookup that finds nothing returns `false`. |
| `data.items[].displayName` | The public name shown on the profile. |
| `data.items[].handle` | The Snapchat username of the account. |
| `data.items[].bio` | The profile bio text. |
| `data.items[].category` | The category label on the profile, such as `Government Org`. |
| `data.items[].subscribers` | The number of subscribers the profile has. |
| `data.items[].url / data.items[].website` | `url` is the Snapchat profile link. `website` is the external site listed on the profile. |
| `data.items[].image` | URL of the profile image. |
| `data.items[].stories[].id` | A UUID that identifies the story. |
| `data.items[].stories[].storyTitle / data.items[].stories[].thumbnailUrl` | The title of a public story and the URL of its thumbnail image. |

### Notes

- Pass either the plain handle, such as `nasa`, or the full profile URL, such as `https://www.snapchat.com/add/nasa`, in `username`.
- The profile sits in `data.items[]`, which is a list. Read the first item for the requested account.
- Check `found` before reading `data.items`, since a missing profile still returns a successful response.

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/snapchat/profile.json`](../../../catalog/models/snapchat/profile.json) · Store page: https://www.sandbase.ai/model/snapchat/profile
