# Toutiao Article Details (App) API: pricing, parameters and code examples

`toutiao/app/article-info` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns details and interface settings for a specified Toutiao post. Provide the post ID to inspect article properties and action settings.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/app/article-info", "group_id": "7450114952884503059"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/app/article-info', {'group_id': '7450114952884503059'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/app/article-info", {
  "group_id": "7450114952884503059"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/app/article-info", sandbase.Params{
	"group_id": "7450114952884503059",
})
```

Same call via the path form: `POST /v1/api/toutiao/app/article-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `group_id` | string | yes | Post ID, can be obtained from the link  |

## Details

Retrieve information and action control settings for a Toutiao article using its `group_id`.

### Use cases

- Look up interface controls and settings for a Toutiao post.
- Extract article information directly using the post identifier.
- Inspect configuration details associated with a specific article link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/app/article-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"group_id": "7450114952884503059"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `group_id` | string | Yes | Post ID, can be obtained from the link |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "h5_extra": {
      "itemCell": {
        "actionCtrl": {
          "actionBar": {
            "actionSettingList": [
              {
                "actionType": 1
              }
            ]
          }
        }
      }
    }
  }
}
```

### Notes

- Obtain the required `group_id` directly from the Toutiao post link.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Toutiao Post Comments](/model/toutiao/app/comments): Returns user comments and interaction metrics for a specific Toutiao post.
- [Toutiao Profile User ID](/model/toutiao/app/user-id): Resolves a Toutiao user profile URL into numeric and secure user identifiers.
- [Toutiao User Profile](/model/toutiao/app/user-info): Get a Toutiao (Jinri Toutiao) user profile by user ID: name, bio, avatar, follower, following and like counts, and content tabs.

---
Machine-readable: [`catalog/models/toutiao/app/article-info.json`](../../../../catalog/models/toutiao/app/article-info.json) · Store page: https://www.sandbase.ai/model/toutiao/app/article-info
