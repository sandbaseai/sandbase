# Bilibili User Relation Statistics API: pricing, parameters and code examples

`bilibili/web/user-relation-stat` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns relationship statistics, including following and follower counts, for a specified Bilibili account using their user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-relation-stat", "uid": "178360345"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-relation-stat', {'uid': '178360345'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-relation-stat", {
  "uid": "178360345"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-relation-stat", sandbase.Params{
	"uid": "178360345",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-relation-stat` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |

## Details

Returns relationship counts for one Bilibili account, including how many accounts it follows and how many follow it. It needs the numeric user ID in `uid`.

### Use cases

- Record the `follower` count of a Bilibili creator each day to chart audience growth.
- Show following and follower numbers on a creator card inside your own dashboard.
- Compare `follower` to `following` across a list of accounts to sort them by audience size.
- Confirm that a `uid` matches the `mid` you expect before you run further lookups on the account.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-relation-stat" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "178360345"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "black": 0,
  "fans_effect": null,
  "fans_medal_toast": null,
  "follower": 73,
  "following": 27,
  "mid": 178360345,
  "whisper": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `follower` | Number of accounts that follow this user. |
| `following` | Number of accounts this user follows. |
| `mid` | Numeric Bilibili user ID of the account. It matches the `uid` you sent. |
| `black` | Blacklist count for the account. The response shows `0` and gives no further detail. |
| `whisper` | Whisper count for the account. The response shows `0` and gives no further detail. |
| `fans_effect / fans_medal_toast` | Fan-related display settings. Both are `null` in this response. |

### Notes

- Pass the numeric Bilibili user ID as a string in `uid`, for example `178360345`.
- If you only have a profile link, call [Bilibili User ID Extraction](/apis/bilibili/web/get-user-id) first to get the ID.
- For name, avatar and other profile details, call [Bilibili User Profile](/apis/bilibili/web/user-profile).
- For total views and likes of the creator, call [Bilibili Creator View and Like Statistics](/apis/bilibili/web/user-up-stat).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/user-relation-stat.json`](../../../../catalog/models/bilibili/web/user-relation-stat.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-relation-stat
