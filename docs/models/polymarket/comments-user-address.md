# Polymarket Get comments by user address API: pricing, parameters and code examples

`polymarket/comments-user-address` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get comments by user address from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/comments-user-address", "user_address": "0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/comments-user-address', {'user_address': '0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/comments-user-address", {
  "user_address": "0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/comments-user-address", sandbase.Params{
	"user_address": "0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6",
})
```

Same call via the path form: `POST /v1/api/polymarket/comments-user-address` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `offset` | integer |  | offset range 0– |
| `ascending` | boolean |  | ascending  |
| `user_address` | string | yes | user_address  |

## Details

Returns a list of comments posted by one Polymarket wallet address. Each item holds the comment text, timestamps, reaction and report counts, and the event or entity it was posted on. The only required input is `user_address`.

### Use cases

- Review what a specific trader has said across Polymarket events.
- Track how much engagement a wallet's comments receive through `reactionCount`.
- Find comments from a wallet that were reported, using `reportCount`.
- Link a wallet's comments to the events they were posted on using `parentEntityID`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/comments-user-address" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_address": "0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6", "limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_address` | string | Yes | user_address |
| `ascending` | boolean | No | ascending |
| `limit` | integer | No | limit |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |

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
    "reactionCount": 2,
    "reportCount": 0,
    "updatedAt": "2026-10-23T11:10:56.48298Z",
    "userAddress": "0xc22d0f7c330d5cc00a92578ed876b8c34aa42dd6"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[].body` | The text of the comment. |
| `[].id` | The comment ID, returned as a string. |
| `[].createdAt / updatedAt` | ISO 8601 UTC timestamps for when the comment was created and last updated. |
| `[].parentEntityID` | The ID of the item the comment was posted on. |
| `[].parentEntityType` | The type of the parent item, for example `Event`. |
| `[].reactionCount` | The number of reactions the comment has received. |
| `[].reportCount` | The number of reports filed against the comment. |
| `[].userAddress` | The wallet address of the commenter. |

### Notes

- Use `limit` and `offset` to page through results. Use `order` and `ascending` to sort them.
- `user_address` is a 0x wallet address. Get one from [Polymarket Get public profile by wallet address](/apis/polymarket/public-profile) or from search results.
- To read a single comment by its ID, call [Polymarket Get comments by comment id](/apis/polymarket/comments-by-id).
- When `parentEntityType` is `Event`, pass `parentEntityID` to [Polymarket Get event by id](/apis/polymarket/events-by-id) to see the event.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/comments-user-address.json`](../../../catalog/models/polymarket/comments-user-address.json) · Store page: https://www.sandbase.ai/model/polymarket/comments-user-address
