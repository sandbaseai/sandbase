# Instagram Stories (full) API: pricing, parameters and code examples

`instagram/stories-full` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0022 per call · **Modes:** sync

Fetch a public Instagram account's currently live stories with media, type, dimensions, posting time, and 24-hour expiry by username.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0022**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/stories-full", "username": "nba"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/stories-full', {'username': 'nba'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/stories-full", {
  "username": "nba"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/stories-full", sandbase.Params{
	"username": "nba",
})
```

Same call via the path form: `POST /v1/api/instagram/stories-full` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username or handle without the @.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `soundTitle`, and it is served only by a source that returns every…  |

## Details

Returns the stories that a public Instagram account has live right now. Each story includes its media URLs, type, size, posting time, expiry time, and sound details when present. The only required input is a `username`.

### Use cases

- Archive an account's stories before they expire by saving the `image` or `videoUrl` files.
- Track which stories carry a paid partnership label for sponsorship monitoring.
- Find stories that use a named sound by reading `soundTitle` and `soundAuthor`.
- Check how often a brand posts stories by comparing `createdUtc` values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/stories-full" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "nba"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username or handle without the @. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `soundTitle`, and it is served only by a source that returns every one |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "audioId": null,
        "avatarUrl": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/870530727_18700682161024…",
        "code": "DfP4jTDgKvK",
        "createdUtc": 1793641838,
        "displayName": "NBA",
        "durationSeconds": 15,
        "expiresUtc": 1793728238,
        "height": 1920,
        "id": "4021681708511308746",
        "image": "https://scontent-lax3-2.cdninstagram.com/v/t51.71878-15/886632526_11417059416508…",
        "mediaType": 2,
        "paidPartnership": true
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].id / data.items[].code` | Unique story ID and short code for the story. Use them to identify or deduplicate stories. |
| `data.items[].createdUtc / data.items[].expiresUtc` | Posting time and expiry time of the story as Unix timestamps in seconds. In the sample, expiry is 86400 seconds after posting. |
| `data.items[].mediaType` | Numeric media type. In the sample, `1` is a story with only an `image` and `2` is a story that also has a `videoUrl`. |
| `data.items[].image / data.items[].videoUrl` | Media file URLs. `videoUrl` appears only on video stories. |
| `data.items[].width / data.items[].height` | Pixel dimensions of the story media. |
| `data.items[].durationSeconds` | Length of a video story in seconds. It is `null` for image stories. |
| `data.items[].audioId / data.items[].soundTitle / data.items[].soundAuthor` | Audio ID, sound name, and sound author for stories with sound. They are `null` when the story has no sound data. |
| `data.items[].paidPartnership` | `true` when the story is marked as a paid partnership. |
| `data.items[].username / data.items[].displayName / data.items[].userId / data.items[].verified` | Account that posted the story: handle, display name, numeric user ID, and verified status. |
| `found` | `true` when the lookup found the account's stories. |

### Notes

- Pass the handle without the @, for example `nba`.
- Set `requireFields` to `audioId`, `soundAuthor`, or `soundTitle` to force a source that returns those fields. This can raise the price.
- Use [Instagram User Highlights](/apis/instagram/user-highlights) for saved stories that stay on a profile after the 24-hour window.
- Use [Instagram Stories (basic)](/apis/instagram/stories-thin) for a lighter version of this data.

### Pricing

Billed at the actual cost of each call, about $0.0022 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/stories-full.json`](../../../catalog/models/instagram/stories-full.json) · Store page: https://www.sandbase.ai/model/instagram/stories-full
