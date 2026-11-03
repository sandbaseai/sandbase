# Douyin User Search (Creator) API: pricing, parameters and code examples

`douyin/creator/user-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches for Douyin accounts and returns user profile records matching the query. Looks up profiles using a Douyin ID or user nickname.

## Pricing

- **$0.001 per call** (USD)
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

Search Douyin accounts by nickname or Douyin ID (抖音号) and get each match's nickname, Douyin ID (`short_id`), numeric `user_id` and avatar. Useful when you only know an account's name.

### Use cases

- Resolve a brand or creator name into the Douyin account ID before calling profile or video APIs.
- Check whether a Douyin ID is taken.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/user-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_name": "中国人工智能学会"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_name` | string | Yes | Username (supports Douyin ID and nickname) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 0,
  "status_msg": "",
  "user_infos": [
    {
      "avatar": "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_ae902e4896a…",
      "nick_name": "中国人工智能学会",
      "short_id": "CAAI_Douyin",
      "user_id": "97074768765"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_infos[]` | Matching accounts. |
| `nick_name` | Display name. |
| `short_id` | Douyin ID shown on the profile (抖音号). |
| `user_id` | Numeric user ID. |
| `avatar` | Avatar URL. |

### Notes

- Results come from the Douyin creator platform search, so the closest names come first; check `nick_name` before using `user_id`.
- For profile and posts, most Douyin APIs take `sec_user_id`; get it from a profile link or the video detail APIs.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/user-search.json`](../../../../catalog/models/douyin/creator/user-search.json) · Store page: https://www.sandbase.ai/model/douyin/creator/user-search
