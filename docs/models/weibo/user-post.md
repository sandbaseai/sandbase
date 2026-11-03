# Weibo User Published Posts API: pricing, parameters and code examples

`weibo/user-post` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get posts published by a Weibo user identified by UID, using page numbers and a required sinceId cursor after the first page. Use it to browse an account's posting history or continue through its post feed.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/user-post", "uid": "2803301701"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/user-post', {'uid': '2803301701'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/user-post", {
  "uid": "2803301701"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/user-post", sandbase.Params{
	"uid": "2803301701",
})
```

Same call via the path form: `POST /v1/api/weibo/user-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Weibo User ID (UID).  |
| `page` | integer |  | Page number, starting with 1. default `1` |
| `sinceId` | string |  | Pagination cursor (since_id). Required if page > 1.  |

## Details

This API returns a page of posts published by one Weibo account. It needs the account's `uid`. For later pages it also needs the `sinceId` cursor.

### Use cases

- Archive an account's posting history with text, counts and image links.
- Track like, comment and repost counts on a brand or celebrity account.
- Download the images attached to each post using the `pic_infos` URLs.
- Check which post an account has pinned to the top of its feed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/user-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "2803301701"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Weibo User ID (UID). |
| `page` | integer | No | Page number, starting with 1. |
| `sinceId` | string | No | Pagination cursor (since_id). Required if page > 1. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "bottom_tips_text": "",
    "bottom_tips_visible": false,
    "list": [
      {
        "analysis_extra": "follow:0",
        "annotations": [
          {
            "photo_sub_type": "0,0,0,0,0,0,0,0,0"
          }
        ],
        "attitudes_count": 1103,
        "attitudes_status": 0,
        "can_edit": false,
        "cardid": "star_1624",
        "comment_manage_info": {
          "approval_comment_type": 0,
          "comment_anon_type": 0,
          "comment_permission_type": -1,
          "comment_sort_type": 0
        },
        "comments_count": 567,
        "content_auth": 3,
        "content_auth_list": [
          {
            "content_auth": 3,
            "rank": 90,
            "show_type": 0
          }
        ],
        "created_at": "Tue Nov 03 07:44:51 +0800 2026",
        "favorited": false
      }
    ],
    "since_id": "5360945434198751kp2",
    "status_visible": 0,
    "topicList": [],
    "total": 154903
  },
  "ok": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.list[]` | One post published by the user. Each item holds the post text, counts, images and flags. |
| `data.list[].id / idstr / mid` | Numeric and string forms of the post ID. `idstr` and `mid` hold the same value as `id` in the sample. |
| `data.list[].mblogid` | Short post ID string, for example `RpCOks7zT`. |
| `data.list[].created_at` | Publish time as text in the form `Tue Nov 03 07:44:51 +0800 2026`. |
| `data.list[].attitudes_count / comments_count` | Number of likes and number of comments on the post. |
| `data.list[].number_display_strategy.display_text` | Shortened display form of a large count, for example `100万+`. |
| `data.list[].isTop` | Pinned flag. The value `1` appears on a post pinned at the top of the feed. |
| `data.list[].pic_ids[]` | IDs of the images attached to the post. Use them as keys into `pic_infos`. |
| `data.list[].pic_infos` | Image details keyed by picture ID. Each has several sizes such as `bmiddle`, `large` and `original`, each with `url`, `width` and `height`. |
| `data.list[].isAd` | Boolean flag that marks whether the post is an ad. |

### Notes

- Get the `uid` from a Weibo profile, or from [Weibo User Profile](/apis/weibo/user-detail).
- The first call needs only `uid`. `page` starts at 1.
- For `page` above 1, send the `sinceId` cursor with the request. The README says it is required for those pages.
- For one post in full, call [Weibo Post Detail](/apis/weibo/web-v2/post-detail).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/weibo/user-post.json`](../../../catalog/models/weibo/user-post.json) · Store page: https://www.sandbase.ai/model/weibo/user-post
