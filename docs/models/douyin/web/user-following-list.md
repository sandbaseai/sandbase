# Douyin Web User Following List API: pricing, parameters and code examples

`douyin/web/user-following-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a list of accounts followed by a Douyin user. Filter by target user security ID and navigate paginated results using timestamps.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-following-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-following-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-following-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-following-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/web/user-following-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, default is 20, it is recommended to keep it unchanged. default `20` |
| `max_time` | string |  | Maximum timestamp, default is 0, get from the returned data later, used for paging. default `"0"` |
| `sec_user_id` | string |  | User sec_user_id default `"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70"` |
| `source_type` | integer |  | Source type, default is `1`, use `2` as the source type for the first request, and then use `1` as the source type for the subsequent request. default `1` |

## Details

Fetch the accounts followed by a user using `sec_user_id`. Pagination is supported through `max_time` alongside `source_type` adjustments.

### Use cases

- Inspect the list of profiles followed by a specific user.
- Map user interest graphs by tracking followed creator profiles.
- Audit account connections and relationship networks across audiences.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-following-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number, default is 20, it is recommended to keep it unchanged. |
| `max_time` | string | No | Maximum timestamp, default is 0, get from the returned data later, used for paging. |
| `sec_user_id` | string | No | User sec_user_id |
| `source_type` | integer | No | Source type, default is `1`, use `2` as the source type for the first request, and then use `1` as the source type for the subsequent request. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "followings": [
    {
      "account_cert_info": "{}",
      "apple_account": 0,
      "authority_status": 0,
      "aweme_count": 222,
      "comment_filter_status": 0,
      "create_time": 1591592883,
      "favoriting_count": 690,
      "fb_expire_time": 0,
      "follow_status": 0,
      "follower_count": 143488,
      "original_musician": {
        "digg_count": 0,
        "music_count": 0,
        "music_used_count": 0
      },
      "search_impr": {
        "entity_id": "1257480849466808"
      }
    }
  ]
}
```

### Notes

- Use `2` for `source_type` on the initial call, then use `1` for subsequent calls.
- Pass the returned timestamp value to `max_time` to paginate through results.
- The `count` parameter defaults to 20 items per page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-following-list.json`](../../../../catalog/models/douyin/web/user-following-list.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-following-list
