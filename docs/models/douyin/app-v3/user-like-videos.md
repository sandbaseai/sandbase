# Douyin User Liked Videos (App V3) API: pricing, parameters and code examples

`douyin/app-v3/user-like-videos` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of videos liked by a specific Douyin user. Supports cursor-based pagination and custom item counts per page.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/user-like-videos", "sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/user-like-videos', {'sec_user_id': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/user-like-videos", {
  "sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/user-like-videos", sandbase.Params{
	"sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/user-like-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `counts` | integer |  | Number per page  |
| `max_cursor` | integer |  | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response.  |
| `sec_user_id` | string | yes | User sec_user_id  |

## Details

Returns the videos a Douyin user has liked, as a paged list. It needs the user's `sec_user_id`. You can set the page size with `counts` and page forward with `max_cursor`.

### Use cases

- Review which videos a specific Douyin account has liked.
- Collect a user's liked videos page by page for content or interest research.
- Check whether a user's liked list is returned at all before building a pipeline around it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/user-like-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | User sec_user_id |
| `counts` | integer | No | Number per page |
| `max_cursor` | integer | No | Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": null,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153140EA2A63AD2C803311DE9E",
    "now": 1793691100000
  },
  "log_pb": {
    "impr_id": "20261103153140EA2A63AD2C803311DE9E"
  },
  "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
  "status_code": 0,
  "uid": "3635433641882579"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list` | List of liked videos. It is `null` in this response, which means no videos came back for this user and request. |
| `status_code` | Result code of the call. `0` in this response. |
| `sec_uid` | The `sec_user_id` of the user whose likes were requested, echoed back. |
| `uid` | Numeric user ID of the same user. |
| `extra.now` | Server time of the response as a number. The value looks like a millisecond timestamp. |
| `extra.logid / log_pb.impr_id` | Request identifiers. Both hold the same value in this response. |
| `extra.fatal_item_ids` | List of item IDs that failed to load. It is empty in this response. |

### Notes

- Get `sec_user_id` from a Douyin user profile, for example with [Douyin User Profile (App V3)](/apis/douyin/app-v3/user-profile).
- For the first page, send `max_cursor` as `0`. For the next page, send the `max_cursor` value from the previous response.
- `aweme_list` can be `null` when no videos are returned, so check for `null` before reading it.
- To see videos the user posted instead of liked, use [Douyin User Videos](/apis/douyin/app-v3/user-post-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/user-like-videos.json`](../../../../catalog/models/douyin/app-v3/user-like-videos.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/user-like-videos
