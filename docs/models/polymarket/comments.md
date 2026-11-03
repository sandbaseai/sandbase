# Polymarket List comments API: pricing, parameters and code examples

`polymarket/comments` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

List comments from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/comments"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/comments', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/comments", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/comments", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `offset` | integer |  | offset range 0– |
| `ascending` | boolean |  | ascending  |
| `holders_only` | boolean |  | holders_only  |
| `get_positions` | boolean |  | get_positions  |
| `parent_entity_id` | integer |  | parent_entity_id  |
| `parent_entity_type` | string |  | parent_entity_type one of: `Event`, `Series`, `market` |

## Details

Returns a list of comments posted on a Polymarket event, series, or market. You pass the parent type with `parent_entity_type` and its numeric ID with `parent_entity_id`. Each comment includes the text, the author profile, and its reactions.

### Use cases

- Pull the discussion under a Polymarket event to read what traders say about an outcome.
- Track which comments get the most reactions on a given market.
- Collect commenter wallet addresses to look up their positions or profiles.
- Archive comment threads for an event with `limit` and `offset` paging.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"parent_entity_type": "Event", "parent_entity_id": 2890, "limit": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ascending` | boolean | No | ascending |
| `get_positions` | boolean | No | get_positions |
| `holders_only` | boolean | No | holders_only |
| `limit` | integer | No | limit |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |
| `parent_entity_id` | integer | No | parent_entity_id |
| `parent_entity_type` | string | No | parent_entity_type |

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
| `id` | The comment ID, returned as a string. |
| `createdAt / updatedAt` | ISO 8601 UTC timestamps for when the comment was created and last updated. |
| `parentEntityID / parentEntityType` | The ID and type of the event, series, or market the comment belongs to. |
| `userAddress` | The wallet address of the user who wrote the comment. |
| `profile.name / profile.pseudonym` | The display name and pseudonym of the commenter. |
| `profile.proxyWallet` | The proxy wallet address of the commenter. |
| `reactionCount` | The number of reactions on the comment. |
| `reactions[].reactionType` | The kind of reaction, such as `HEART`. |
| `reactions[].userAddress` | The wallet address of the user who reacted. |

### Notes

- `parent_entity_type` accepts `Event`, `Series`, or `market`. Set `parent_entity_id` to the numeric ID of that parent.
- Page through results with `limit` and `offset`. Use `order` and `ascending` to control sorting.
- To fetch one comment by its ID, call [Polymarket Get comments by comment id](/apis/polymarket/comments-by-id). To list comments from one wallet, call [Polymarket Get comments by user address](/apis/polymarket/comments-user-address).
- To find event IDs, call [Polymarket List events](/apis/polymarket/events).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/comments.json`](../../../catalog/models/polymarket/comments.json) · Store page: https://www.sandbase.ai/model/polymarket/comments
