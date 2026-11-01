# Bilibili User Profile

`bilibili/web/user-profile` · api · Bilibili

Returns profile details and charging sponsor information for a specified Bilibili account based on the provided user UID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-profile", "uid": "316183842"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-profile', {'uid': '316183842'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-profile", {
  "uid": "316183842"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-profile", sandbase.Params{
	"uid": "316183842",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |

## Details

Retrieve profile information for a Bilibili account by supplying the target user's `uid`.

### Use cases

- View public profile details for a given Bilibili user.
- Inspect sponsor and charging ranking lists for an account.
- Monitor account profile data for creator tracking tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "1437582453"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "elec": {
      "show_info": {
        "list": [
          {
            "rank": 1,
            "uname": "蓮卫兵"
          }
        ]
      }
    }
  }
}
```

### Notes

- Provide the user ID in `uid` to look up account details.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/user-profile.json`](../../../../catalog/models/bilibili/web/user-profile.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-profile
