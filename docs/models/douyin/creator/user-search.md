# Douyin User Search (Creator) API: pricing, parameters and code examples

`douyin/creator/user-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Searches for Douyin accounts and returns user profile records matching the query. Looks up profiles using a Douyin ID or user nickname.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/user-search", "user_name": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/user-search', {'user_name': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/user-search", {
  "user_name": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/user-search", sandbase.Params{
	"user_name": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/creator/user-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_name` | string | yes | Username (supports Douyin ID and nickname)  |

## Details

Search Douyin accounts by specifying `user_name`. The query supports searches by Douyin ID as well as profile nickname.

### Use cases

- Locate account profiles by entering a Douyin ID.
- Search for profiles by display nickname.
- Retrieve account identifiers such as user ID and short ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/user-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_name": "中国人工智能学会"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_name` | string | Yes | Username (supports Douyin ID and nickname) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "user_infos": [
    {
      "nick_name": "<user>",
      "short_id": "<user>",
      "user_id": "<user>"
    }
  ]
}
```

### Notes

- The `user_name` parameter accepts either a Douyin ID or a user nickname.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/model/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/model/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/model/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/user-search.json`](../../../../catalog/models/douyin/creator/user-search.json) · Store page: https://www.sandbase.ai/model/douyin/creator/user-search
