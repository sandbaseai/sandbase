# Polymarket Get comments by comment id API: pricing, parameters and code examples

`polymarket/comments-by-id` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get comments by comment id from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/comments-by-id", "id": 3305081}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/comments-by-id', {'id': 3305081})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/comments-by-id", {
  "id": 3305081
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/comments-by-id", sandbase.Params{
	"id": 3305081,
})
```

Same call via the path form: `POST /v1/api/polymarket/comments-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | id  |
| `get_positions` | boolean |  | get_positions  |

## Details

Returns a single Polymarket comment by its numeric comment id. The response is a list that holds the comment text, the author profile, and the reactions on the comment. It needs the `id` of the comment. You can also send `get_positions`.

### Use cases

- Fetch the text and timestamps of a comment you saw in a feed or a link.
- Check who wrote a comment and which wallet address is behind it.
- Count the reactions and reports on a comment to judge how it was received.
- Find the event a comment belongs to by reading its parent entity fields.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/comments-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 3305081}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | id |
| `get_positions` | boolean | No | get_positions |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "body": "idor-poc-1792753844",
    "createdAt": "2026-10-23T11:10:47.356694Z",
    "id": "3305081",
    "parentEntityID": 2890,
    "parentEntityType": "Event",
    "profile": {
      "baseAddress": "0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6",
      "bio": "",
      "displayUsernamePublic": false,
      "name": "Stable-Declaration",
      "profileImage": "https://polymarket-upload.s3.us-east-2.amazonaws.com/profile-image-7727089-ebb22…",
      "proxyWallet": "0x06892a304377a4334340678e2d36e19d679cca34",
      "pseudonym": "Stable-Declaration"
    },
    "reactionCount": 2,
    "reactions": [
      {
        "commentID": 3305081,
        "id": "3198145",
        "profile": {
          "proxyWallet": "0x45bc5604d3285ac448ae4a39470b9e6085a0df83"
        },
        "reactionType": "HEART",
        "userAddress": "0x936810690af85a4e357c7ac707e2b81e64a39582"
      }
    ],
    "reportCount": 0,
    "updatedAt": "2026-10-23T11:10:56.48298Z",
    "userAddress": "0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `body` | The text of the comment. |
| `id` | The comment id, returned as a string. |
| `createdAt / updatedAt` | ISO 8601 UTC timestamps for when the comment was created and last updated. |
| `parentEntityType / parentEntityID` | The kind of item the comment is attached to (here `Event`) and the id of that item. |
| `userAddress` | The wallet address of the comment author. |
| `profile.name / profile.pseudonym` | The public name and pseudonym of the author. |
| `profile.proxyWallet` | The proxy wallet address linked to the author profile. |
| `reactionCount / reportCount` | The number of reactions and the number of reports on the comment. |
| `reactions[].reactionType` | The type of reaction, for example `HEART`. |
| `reactions[].userAddress` | The wallet address of the user who reacted. |

### Notes

- The response is a JSON list, so read the comment from the first item.
- Take the `id` from a comment list, such as [Polymarket List comments](/apis/polymarket/comments) or [Polymarket Get comments by user address](/apis/polymarket/comments-user-address).
- Use `parentEntityID` with [Polymarket Get event by id](/apis/polymarket/events-by-id) when `parentEntityType` is `Event`.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/comments-by-id.json`](../../../catalog/models/polymarket/comments-by-id.json) · Store page: https://www.sandbase.ai/model/polymarket/comments-by-id
