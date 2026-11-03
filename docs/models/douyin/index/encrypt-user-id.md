# Douyin Index User ID Encryption API: pricing, parameters and code examples

`douyin/index/encrypt-user-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Converts a standard numeric Douyin uid into the encrypted user_id required by Douyin Index endpoints for debugging or custom queries.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/encrypt-user-id", "uid": "92769419069"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/encrypt-user-id', {'uid': '92769419069'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/encrypt-user-id", {
  "uid": "92769419069"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/encrypt-user-id", sandbase.Params{
	"uid": "92769419069",
})
```

Same call via the path form: `POST /v1/api/douyin/index/encrypt-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Douyin uid, numeric string  |

## Details

This API converts a numeric Douyin `uid` into the encrypted `user_id` string used by Douyin Index endpoints. It needs one input, the `uid` as a numeric string, and returns both values.

### Use cases

- Get the encrypted `user_id` for a creator before you build a custom Douyin Index query.
- Check that your own uid-to-`user_id` conversion matches the value this API returns.
- Convert a list of numeric creator uids into the IDs that Douyin Index creator endpoints expect.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/encrypt-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Douyin uid, numeric string |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "uid": "92769419069",
  "user_id": "jchgjebjagj"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `uid` | The numeric Douyin uid you sent in the request, returned unchanged. |
| `user_id` | The encrypted form of the uid. Pass this value to Douyin Index endpoints that ask for an encrypted user ID. |

### Notes

- Send `uid` as a string of digits, for example `92769419069`. Do not send it as a number.
- The response has only two keys, `uid` and `user_id`. The call returns no creator profile data.
- Use the returned `user_id` in creator endpoints such as [Douyin Creator Top Videos](/apis/douyin/index/daren-great-user-top-video) or [Douyin Daren Fan Analysis](/apis/douyin/index/daren-great-user-fans-info), if their parameters ask for an encrypted ID.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/encrypt-user-id.json`](../../../../catalog/models/douyin/index/encrypt-user-id.json) · Store page: https://www.sandbase.ai/model/douyin/index/encrypt-user-id
