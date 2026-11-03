# Douyin Web User Following List API: pricing, parameters and code examples

`douyin/web/user-following-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of accounts followed by a Douyin user. Filter by target user security ID and navigate paginated results using timestamps.

## Pricing

- **$0.001 per call** (USD)
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

Returns the list of accounts that a Douyin user follows. It needs the target user's `sec_user_id` and returns one page of followed accounts with paging timestamps.

### Use cases

- Pull the creators a specific Douyin account follows to see what that user is interested in.
- Build a follow graph by walking the accounts followed by a seed user.
- Check whether a brand or business account (see `account_cert_info`) appears among the accounts a user follows.
- Collect avatar images and video counts for followed accounts to fill a dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-following-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number, default is 20, it is recommended to keep it unchanged. |
| `max_time` | string | No | Maximum timestamp, default is 0, get from the returned data later, used for paging. |
| `sec_user_id` | string | No | User sec_user_id |
| `source_type` | integer | No | Source type, default is `1`, use `2` as the source type for the first request, and then use `1` as the source type for the subsequent request. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611031532315C2777D33738AB243FBF",
    "now": 1793691152000
  },
  "followings": [
    {
      "accept_private_policy": false,
      "account_cert_info": null,
      "account_region": "",
      "account_type": null,
      "activity": null,
      "activity_label": null,
      "ad_cover_title": null,
      "ad_cover_url": null,
      "ad_order_id": null,
      "age_gate_action": null,
      "age_gate_post_action": null,
      "age_gate_time": null
    }
  ],
  "has_more": true,
  "hotsoon_has_more": 0,
  "hotsoon_text": "",
  "log_pb": {
    "impr_id": "202611031532315C2777D33738AB243FBF"
  },
  "max_time": 1793329603,
  "min_time": 1788086525,
  "mix_count": 436,
  "myself_user_id": "1185696462159498",
  "offset": 0,
  "rec_has_more": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `followings[]` | One followed account per item. Each item holds profile and avatar data for that account. |
| `followings[].aweme_count` | Number of videos the followed account has posted. |
| `followings[].account_cert_info` | JSON string with account certification flags. For example `{"is_biz_account":1}` marks a business account. It is `null` when no flags are set. |
| `followings[].avatar_thumb / avatar_168x168 / avatar_300x300 / avatar_medium / avatar_larger` | Avatar images in different sizes. Each has a `url_list` with image URLs, plus `uri`, `width` and `height`. |
| `followings[].avatar_uri` | Storage path of the avatar image for the followed account. |
| `followings[].aweme_control` | Flags such as `can_comment`, `can_forward` and `can_share` that show what viewers may do with the account's videos. |
| `has_more` | `true` when more followed accounts remain after this page. |
| `max_time / min_time` | Timestamps that bound this page of results. Use `max_time` for the next page request. |
| `total` | Total number of accounts the user follows. |
| `myself_user_id` | Numeric user ID tied to the requested user. |

### Notes

- Get `sec_user_id` from a user's profile link. Use [Douyin sec_user_id from URL](/apis/douyin/web/sec-user-id) to extract it.
- Send `source_type` as `2` on the first request. Use `1` on every later request.
- To get the next page, set `max_time` to the `max_time` value from the previous response while `has_more` is `true`. The first request uses `0`.
- The `count` parameter defaults to 20.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-following-list.json`](../../../../catalog/models/douyin/web/user-following-list.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-following-list
