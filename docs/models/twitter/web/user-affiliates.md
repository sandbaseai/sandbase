# Twitter User affiliates API: pricing, parameters and code examples

`twitter/web/user-affiliates` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get user affiliates on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-affiliates", "screen_name": "NASA"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-affiliates', {'screen_name': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-affiliates", {
  "screen_name": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-affiliates", sandbase.Params{
	"screen_name": "NASA",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-affiliates` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor  |
| `screen_name` | string | yes | Screen Name  |

## Details

Returns the accounts affiliated with a Twitter account, such as the staff, missions and sub-accounts of an organization. It needs the `screen_name` of the parent account, for example `NASA`.

### Use cases

- List the official sub-accounts and people tied to an organization account like NASA.
- Compare follower counts across the affiliated accounts of a brand or agency.
- Build a directory of an organization's missions, teams and staff accounts with their bios.
- Collect `user_id` values of affiliated accounts to feed into other profile lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-affiliates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "NASA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `screen_name` | string | Yes | Screen Name |
| `cursor` | string | No | Cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "affilates": [
    {
      "description": "Official Twitter account of NASA’s Chandra X-ray Observatory. Operated for NASA …",
      "followers_count": 418886,
      "friends_count": 198,
      "media_count": 4664,
      "name": "Chandra Observatory",
      "profile_image": null,
      "screen_name": "chandraxray",
      "statuses_count": 78136,
      "user_id": "12415722"
    }
  ],
  "next_cursor": "DAAHCgABHWL0WQD__-wLAAIAAAAIMzAyNTU4MzMIAAMAAAACAAA"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `affilates` | List of affiliated accounts. The key is spelled `affilates` in the response. |
| `affilates[].screen_name / affilates[].name` | The handle and display name of the affiliated account. |
| `affilates[].user_id` | Numeric ID of the account, returned as a string. |
| `affilates[].description` | Bio text of the affiliated account. Long bios are cut off with an ellipsis. |
| `affilates[].followers_count / affilates[].friends_count` | Number of followers and number of accounts it follows. |
| `affilates[].statuses_count / affilates[].media_count` | Number of posts and number of media posts on the account. |
| `affilates[].profile_image` | Profile image value. It is `null` in this response. |
| `next_cursor` | Cursor string for the next page of affiliates. |

### Notes

- Pass `next_cursor` from the response as `cursor` in the next request to get the next page.
- The `screen_name` is the handle without the `@` sign, for example `NASA`.
- Use [Twitter (X) User Profile](/apis/twitter/web/user-profile) to get full details for an affiliated account.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/web/user-affiliates.json`](../../../../catalog/models/twitter/web/user-affiliates.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-affiliates
