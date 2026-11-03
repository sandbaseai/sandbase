# Douyin UID to Sec User ID API: pricing, parameters and code examples

`douyin/web/encrypt-uid-to-sec-user-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Converts a standard Douyin user UID into an encrypted sec_user_id. It takes a short_id value and returns the corresponding secure identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/encrypt-uid-to-sec-user-id", "uid": "92769419069"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/encrypt-uid-to-sec-user-id', {'uid': '92769419069'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/encrypt-uid-to-sec-user-id", {
  "uid": "92769419069"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/encrypt-uid-to-sec-user-id", sandbase.Params{
	"uid": "92769419069",
})
```

Same call via the path form: `POST /v1/api/douyin/web/encrypt-uid-to-sec-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User uid, which is the short_id of the Douyin number  |

## Details

This API converts a Douyin user `uid` into the encrypted `sec_user_id` for the same account. It needs one input, `uid`, which is the `short_id` of the Douyin number. The response returns the `sec_user_id` and echoes the `uid`.

### Use cases

- Get the `sec_user_id` for an account when you only have its numeric `uid`.
- Build the input for Douyin endpoints that accept a `sec_user_id`, such as a user's video posts or profile.
- Store a stable mapping between a known `uid` and its `sec_user_id` in a creator database.
- Check that a `uid` in a list resolves to the account you expect before running bulk lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/encrypt-uid-to-sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User uid, which is the short_id of the Douyin number |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "sec_user_id": "Cif6qQhZHylHHSzYUXX8PqJZ8x70Q7irzjB64CSSdp2mIJIW-Vi_qlgaSQo8AAAAAAAAAAAAAFEYeqIM…",
  "uid": "92769419069"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `sec_user_id` | The encrypted user identifier for the account. It is a long string of letters, digits, hyphens and underscores. Pass it as-is to endpoints that ask for a `sec_user_id`. |
| `uid` | The `uid` value from the request, returned unchanged. Use it to match a response to its request. |

### Notes

- Send `uid` as a string, not a number.
- Copy the full `sec_user_id` without trimming it. The value is long.
- Pass the returned `sec_user_id` to [Douyin User Video Posts](/apis/douyin/web/user-post-videos) to list the user's videos, or to [Douyin User Profile (Web)](/apis/douyin/web/user-profile) to read the profile.
- If you have a profile URL instead of a `uid`, use [Douyin sec_user_id from URL](/apis/douyin/web/sec-user-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/encrypt-uid-to-sec-user-id.json`](../../../../catalog/models/douyin/web/encrypt-uid-to-sec-user-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/encrypt-uid-to-sec-user-id
