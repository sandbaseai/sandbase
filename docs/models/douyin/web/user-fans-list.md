# Douyin Web User Fans List API: pricing, parameters and code examples

`douyin/web/user-fans-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of followers for a specified Douyin user account. Supports result pagination via timestamp parameters and custom page counts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-fans-list", "count": 20, "max_time": "0", "sec_user_id": "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70", "source_type": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-fans-list', {'count': 20, 'max_time': '0', 'sec_user_id': 'MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70', 'source_type': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-fans-list", {
  "count": 20,
  "max_time": "0",
  "sec_user_id": "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70",
  "source_type": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-fans-list", sandbase.Params{
	"count": 20,
	"max_time": "0",
	"sec_user_id": "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70",
	"source_type": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-fans-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, default is 20, it is recommended to keep it unchanged. default `20` |
| `max_time` | string |  | Maximum timestamp, default is 0, get from the returned data later, used for paging. default `"0"` |
| `sec_user_id` | string |  | User sec_user_id default `"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70"` |
| `source_type` | integer |  | Source type, default is `1`, use `2` as the source type for the first request, and then use `1` as the source type for the subsequent request. default `1` |

## Details

Returns a page of followers for a Douyin account. Each follower is a user profile object with avatar images and post count. The input is the account's `sec_user_id`.

### Use cases

- Pull the follower list of a Douyin creator to review who follows the account.
- Page through all followers of an account and store each profile with its avatar links.
- Compare the `total` follower count of several creators during influencer research.
- Spot followers that have posted few or no videos by checking `aweme_count`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-fans-list" \
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
  "all_fans_group_title": "全部关注他(她)的人",
  "display_fans_score_info": true,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153231977D6BDD71CAD9F35C83",
    "now": 1793691151000
  },
  "followers": [
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
  "group_types": null,
  "has_more": true,
  "hotsoon_has_more": 0,
  "hotsoon_text": "",
  "log_pb": {
    "impr_id": "20261103153231977D6BDD71CAD9F35C83"
  },
  "max_time": 1792839294,
  "min_time": 1780926925,
  "mix_count": 127
}
```

### Response fields

| Field | Meaning |
|---|---|
| `followers[]` | List of follower profiles for the requested account. Each item is one user. |
| `followers[].aweme_count` | Number of videos the follower has posted. |
| `followers[].avatar_thumb / avatar_168x168 / avatar_300x300 / avatar_medium / avatar_larger` | Avatar images in different sizes. Each has a `uri`, `width`, `height` and a `url_list` of image links. |
| `followers[].aweme_control` | Flags such as `can_comment`, `can_forward` and `can_share` for the follower's videos. |
| `total` | Total number of followers of the requested account. |
| `has_more` | `true` when more followers are available on a next page. |
| `max_time / min_time` | Timestamps of the page boundaries. Use `max_time` for the next request's `max_time` parameter. |
| `status_code` | Status of the call. `0` in the sample response. |
| `extra.logid / log_pb.impr_id` | Request identifiers returned with the response. |

### Notes

- Get `sec_user_id` from a user profile link with [Douyin sec_user_id from URL](/apis/douyin/web/sec-user-id).
- For the first request, set `source_type` to `2`. For later pages, set it to `1`.
- To get the next page, check that `has_more` is `true`, then send the returned `max_time` value as the `max_time` parameter.
- The sample response shows `min_time` and `max_time` as Unix-style second values, such as `1792839294`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-fans-list.json`](../../../../catalog/models/douyin/web/user-fans-list.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-fans-list
