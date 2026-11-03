# TikTok Live API: pricing, parameters and code examples

`tiktok/live` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Check whether a TikTok creator is live and get the current live room (title, viewers, start time) by handle.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/live", "handle": "thejustalex"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/live', {'handle': 'thejustalex'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/live", {
  "handle": "thejustalex"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/live", sandbase.Params{
	"handle": "thejustalex",
})
```

Same call via the path form: `POST /v1/api/tiktok/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | TikTok username without the leading @ (e.g. "thejustalex").  |

## Details

The TikTok Live API checks whether a TikTok creator is live right now. It takes a creator `handle` and returns the current live room (title, viewers, start time) together with basic profile data. If the lookup finds nothing, it returns `found: false`.

### Use cases

- Alert a team when a partnered creator starts a live stream.
- Log the `title` and `viewers` of a creator's live room over time.
- Check a creator's follower count and verified status before a sponsorship deal.
- Build a list of which tracked creators are live at the moment.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "thejustalex"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | TikTok username without the leading @ (e.g. "thejustalex"). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatarUrl": "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/b169e9223700dc8d20d…",
    "bio": "🔴LIVE EVERYDAY🔴\n📧rainzbizemail@gmail.com📧",
    "coverUrl": "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/b169e9223700dc8d20d…",
    "displayName": "JustAlex",
    "enterCount": 1,
    "followers": 716096,
    "following": 2452,
    "handle": "thejustalex",
    "private": false,
    "roomId": "7644628722120805150",
    "secUid": "MS4wLjABAAAA3_8rhYkKsHyYO45EzOF7RBQJRs1EaHBqHFtYIaz3aka44bMVgCLONvFaXPkddJei",
    "startTime": 1779903940
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the handle was found, `false` when it was not. |
| `data.roomId` | ID of the live room, as a string. Use it to look up room details in other live APIs. |
| `data.title` | Title of the live stream. |
| `data.viewers` | Viewer number reported for the live room. |
| `data.startTime` | Start time of the live stream as a Unix timestamp in seconds. |
| `data.status` | Numeric status code of the live room. The response does not explain the codes, so test it against known live and offline creators. |
| `data.handle / data.displayName` | The creator's TikTok username and the name shown on the profile. |
| `data.followers / data.following` | Number of accounts that follow the creator, and number of accounts the creator follows. |
| `data.userId / data.secUid` | Account identifiers for the creator. Use them in other TikTok APIs that ask for a user ID. |
| `data.avatarUrl / data.coverUrl` | Image links for the creator's avatar and cover picture. |

### Notes

- Pass `handle` without the leading @, for example `thejustalex`.
- `roomId`, `userId` and `startTime` are the values to reuse in follow-up calls. `startTime` is in seconds, not milliseconds.
- For room details, try [TikTok Broadcast Room Information](/apis/tiktok/app-v3/live-room-info). For a plain online check, try [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/live.json`](../../../catalog/models/tiktok/live.json) · Store page: https://www.sandbase.ai/model/tiktok/live
