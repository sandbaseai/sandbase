# Instagram Stories (basic) API: pricing, parameters and code examples

`instagram/stories-thin` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00188 per call · **Modes:** sync

Fetch a public Instagram account's currently live stories - media URL, owner, and posting time - by username. Lightweight projection; for media type, dimensions, and the 24h expiry time use instagram.stories_full.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00188**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/stories-thin", "username": "nba"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/stories-thin', {'username': 'nba'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/stories-thin", {
  "username": "nba"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/stories-thin", sandbase.Params{
	"username": "nba",
})
```

Same call via the path form: `POST /v1/api/instagram/stories-thin` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username/handle to fetch currently live stories for (without the @).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `durationSeconds`, and it is served only by a source that returns…  |

## Details

This API returns the currently live stories for a public Instagram account. It needs one input, the account `username` without the @. Each story comes with a media URL, a permalink, the owner's name and a creation timestamp.

### Use cases

- Archive an account's live stories before they disappear from Instagram.
- Monitor a brand or team account and alert when it posts a new story.
- Collect story media URLs for a content review or competitor tracking tool.
- Check whether a verified account is posting video stories and how long they run.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/stories-thin" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "nba"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username/handle to fetch currently live stories for (without the @). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `durationSeconds`, and it is served only by a source that returns ever |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "avatarUrl": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/870530727_18700682161024…",
        "createdUtc": 1793641838,
        "displayName": "NBA",
        "durationSeconds": 15,
        "id": "4021681708511308746",
        "mediaUrl": "https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m78/AQN3hjdE6SuRgC6FGlEF0bff…",
        "permalink": "https://www.instagram.com/reel/DfP4jTDgKvK/",
        "username": "nba",
        "verified": true
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the lookup returned a result. A lookup that finds nothing returns `false`. |
| `data.items[]` | One entry per live story. The list holds every story the account currently has up. |
| `data.items[].id` | Unique ID of the story, as a numeric string. |
| `data.items[].mediaUrl` | Direct URL of the story's image or video file. |
| `data.items[].permalink` | Instagram link to the story's post page. |
| `data.items[].createdUtc` | Time the story was posted, as a Unix timestamp in seconds. |
| `data.items[].durationSeconds` | Length of the story in seconds. It is `null` on the image story in the sample, so treat `null` as no duration. |
| `data.items[].username / data.items[].displayName` | The handle and display name of the account that posted the story. |
| `data.items[].verified` | `true` when the account is verified. |
| `data.items[].avatarUrl` | URL of the account's profile picture. |

### Notes

- Use the handle from the account's Instagram URL as `username`, with no @.
- Pass `requireFields: ["durationSeconds"]` to force a source that returns the duration. This can raise the price of the call.
- For media type, dimensions and expiry time, call [Instagram Stories (full)](/apis/instagram/stories-full).
- The `mediaUrl` and `avatarUrl` values are long CDN links with query strings. Store the full string.

### Pricing

Billed at the actual cost of each call, about $0.00188 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/stories-thin.json`](../../../catalog/models/instagram/stories-thin.json) · Store page: https://www.sandbase.ai/model/instagram/stories-thin
