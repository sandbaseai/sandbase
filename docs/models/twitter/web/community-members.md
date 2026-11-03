# Twitter Community members (no pagination) API: pricing, parameters and code examples

`twitter/web/community-members` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get community members (no pagination) on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/community-members", "community_id": "1493290339532222469"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/community-members', {'community_id': '1493290339532222469'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/community-members", {
  "community_id": "1493290339532222469"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/community-members", sandbase.Params{
	"community_id": "1493290339532222469",
})
```

Same call via the path form: `POST /v1/api/twitter/web/community-members` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor (no pagination, has no effect)  |
| `community_id` | string | yes | Community ID  |

## Details

This API returns a list of members of a Twitter Community. It needs a `community_id` and returns each member's name, handle, user ID, profile image and Blue verification flag.

### Use cases

- Build a list of accounts that belong to a niche Community, such as a crypto group.
- Check which members of a Community have Blue verification.
- Collect member `user_id` values to look up full profiles in other APIs.
- Track who appears in a Community by comparing member lists over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/community-members" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"community_id": "1493290339532222469"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `community_id` | string | Yes | Community ID |
| `cursor` | string | No | Cursor (no pagination, has no effect) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "members": [
    {
      "blue_verified": true,
      "name": "DustyBC Crypto",
      "profile_image": "https://pbs.twimg.com/profile_images/1644089081360445442/XLMlSx4u_normal.jpg",
      "screen_name": "DustyBC",
      "user_id": "913778551555608576"
    }
  ],
  "next_cursor": "CycRAAAAAAwABAwKmwzBVQo+vRNHWkZXlyACCm07AAABfvmCq3QADJorCj69f/////////8KbTt/////…",
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `members[]` | List of Community members returned in this response. |
| `members[].user_id` | Numeric ID of the member's account, as a string. |
| `members[].screen_name` | The member's handle, without the @ sign. |
| `members[].name` | The member's display name. |
| `members[].blue_verified` | `true` if the account has Blue verification, `false` if not. |
| `members[].profile_image` | URL of the member's profile image. The URL points to a small `_normal` size version. |
| `next_cursor` | Cursor string returned with the list. |
| `status` | Request status. `ok` means the call worked. |

### Notes

- Get `community_id` from a Community search or from the Community info API. Try [Twitter Search communities](/apis/twitter/web/search-communities) or [Twitter Community info](/apis/twitter/web/community-info).
- This API has no pagination. The `cursor` parameter has no effect, even though the response includes `next_cursor`.
- Use `user_id` or `screen_name` from each member with [Twitter (X) User Profile](/apis/twitter/web/user-profile) to get full profile details.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/web/community-members.json`](../../../../catalog/models/twitter/web/community-members.json) · Store page: https://www.sandbase.ai/model/twitter/web/community-members
