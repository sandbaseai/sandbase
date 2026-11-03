# Facebook Profile ID API: pricing, parameters and code examples

`facebook/profile-id` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Resolve the numeric Facebook profile ID behind a profile path such as "zuck", for use with endpoints that need a profile ID.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/profile-id", "url": "zuck"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/profile-id', {'url': 'zuck'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/profile-id", {
  "url": "zuck"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/profile-id", sandbase.Params{
	"url": "zuck",
})
```

Same call via the path form: `POST /v1/api/facebook/profile-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The path portion of the Facebook profile URL, such as /<profile-path>. Do not include the scheme or host.  |

## Details

This API returns the numeric Facebook profile ID for a profile path such as `zuck`. It needs one input, the `url` path of the profile.

### Use cases

- Convert a profile path into a numeric ID before you call an endpoint that only accepts profile IDs.
- Store a numeric ID for each tracked profile next to its path in your own database.
- Build a lookup table that maps many profile paths to their IDs in one batch job.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/profile-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "zuck"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The path portion of the Facebook profile URL, such as /<profile-path>. Do not include the scheme or host. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "profile_id": "4"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `profile_id` | The numeric Facebook profile ID for the requested profile path. For the path `zuck` the value is `4`. |
| `profile_id` | The value arrives as a string of digits, not as a JSON number. Keep it as a string in your code. |
| `profile_id` | Pass this value to any endpoint that asks for a profile ID. It is the only field in the response. |

### Notes

- Send only the path part of the profile URL in `url`, such as `zuck`. Do not include the scheme or host.
- To get profile details next, call [Facebook Profile](/apis/facebook/profile). To list posts, call [Facebook Get Profile Posts](/apis/facebook/profile-posts).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/profile-id.json`](../../../catalog/models/facebook/profile-id.json) · Store page: https://www.sandbase.ai/model/facebook/profile-id
