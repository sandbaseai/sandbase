# Weibo Recommended Homepage Feed API: pricing, parameters and code examples

`weibo/web-v2/user-recommend-timeline` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended timeline posts from the Weibo homepage feed. Supports filtering by group ID or container ID, custom feed counts, refresh types, and cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-recommend-timeline"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-recommend-timeline', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-recommend-timeline", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-recommend-timeline", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-recommend-timeline` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count (default 10, suggested 5-20)  |
| `max_id` | string |  | Pagination cursor, pass "0" for first request  |
| `refresh` | integer |  | Refresh type (0=normal refresh, 1=force refresh)  |
| `extparam` | string |  | Extended parameters (default "discover\|new_feed")  |
| `group_id` | string |  | Group ID (can be obtained through fetch_all_groups)  |
| `containerid` | string |  | Container ID (usually same as group_id)  |

## Details

Returns a page of recommended posts from the Weibo homepage feed. All parameters are optional, so you can call it with an empty body. Narrow the feed with `group_id` or `containerid`, and page through it with `max_id`.

### Use cases

- Show the Weibo recommended feed inside an external reader app.
- Track `comments_count` and `attitudes_count` on recommended posts to see which ones draw reactions.
- Collect video posts from the feed, with their duration and cover images, for a content review.
- Check which recommended posts come from accounts the viewer already follows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-recommend-timeline" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `containerid` | string | No | Container ID (usually same as group_id) |
| `count` | integer | No | Count (default 10, suggested 5-20) |
| `extparam` | string | No | Extended parameters (default "discover/new_feed") |
| `group_id` | string | No | Group ID (can be obtained through fetch_all_groups) |
| `max_id` | string | No | Pagination cursor, pass "0" for first request |
| `refresh` | integer | No | Refresh type (0=normal refresh, 1=force refresh) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "max_id": 1,
  "ok": 1,
  "since_id": "{\"ul_sid\":\"\",\"ul_hid\":\"\",\"since_id\":\"5355421545268322\"}",
  "statuses": [
    {
      "analysis_extra": "recommend_source:251|hot_request_id:179369199166779500000065799989854242|gid:534…",
      "annotations": [
        {
          "photo_sub_type": ""
        }
      ],
      "attitudes_count": 16655,
      "attitudes_status": 0,
      "buttons": [
        {
          "actionlog": {
            "act_code": "91",
            "act_type": "1",
            "cardid": "102803_-_mbloglist_5355421545268322",
            "ext": "uid:6579998985|mid:5355421545268322|act:follow|time:1793691992|source:_|recommen…",
            "fid": "102803_ctg1_1761_-_ctg1_1761",
            "oid": "6579998985",
            "source": "hot",
            "uicode": ""
          },
          "name": "关注",
          "params": {
            "able_recommend": 1,
            "extparams": {
              "followcardid": "1028030000_5355421545268322_95e29e61",
              "followscene": "hotweibo"
            },
            "uid": 7740247568
          },
          "pic": "http://u1.sinaimg.cn/upload/2013/07/02/timeline_card_small_button_icon_add.png",
          "type": "follow"
        }
      ],
      "can_edit": false,
      "cardid": "raresvip_0113001563",
      "comment_manage_info": {
        "approval_comment_type": 0,
        "comment_anon_type": 0,
        "comment_permission_type": 0,
        "comment_sort_type": 0
      },
      "comments_count": 326,
      "content_auth": 0,
      "created_at": "Sun Oct 18 17:24:18 +0800 2026",
      "extra_button_info": {
        "actionlog": {
          "act_code": "1558",
          "act_type": "1",
          "code": "",
          "ext": "",
          "fid": null,
          "lfid": null,
          "luicode": null,
          "mark": ""
        },
        "extra_button_highlight_image": "http://h5.sinaimg.cn/upload/2016/09/27/555/timeline_icon_delete_highlighted.png",
        "extra_button_image": "http://h5.sinaimg.cn/upload/2016/09/27/555/timeline_icon_delete.png",
        "extra_button_type": 0
      }
    }
  ],
  "total_number": 100
}
```

### Response fields

| Field | Meaning |
|---|---|
| `statuses[]` | The list of recommended posts in this page. |
| `statuses[].mid / statuses[].idstr / statuses[].id` | The post ID, as a string in the first two and as a number in `id`. |
| `statuses[].mblogid` | Short post ID string, such as `RnfLAm6wW`. |
| `statuses[].created_at` | Publish time as a text date, for example `Sun Oct 18 17:24:18 +0800 2026`. |
| `statuses[].attitudes_count / statuses[].comments_count` | Number of likes (attitudes) and comments on the post. |
| `statuses[].isAd` | Whether the post is marked as an ad. |
| `statuses[].region_name` | Publish location label, such as `发布于 北京`. Not every post has it. |
| `statuses[].page_info.object_type` | Type of the attached object, such as `video`. Only posts with an attachment have `page_info`. |
| `statuses[].page_info.media_info.duration` | Length of the attached video. Read it together with `author_name` and `author_info.followers_count` in the same object. |
| `statuses[].page_info.cards[].content2` | Description text of the attached video card. |
| `statuses[].buttons[].params.uid` | User ID of the post author, attached to the follow button. |
| `since_id` | Cursor text for the next position in the feed. It is a JSON string that contains a `since_id` value. |

### Notes

- Pass `0` as `max_id` on the first request. The response also returns `max_id` and `since_id` for the next step.
- Get `group_id` values from [Weibo All Groups Information](/apis/weibo/web-v2/all-groups). `containerid` is usually the same value.
- To read the full text and details of one post, call [Weibo Post Detail](/apis/weibo/web-v2/post-detail) with the post ID.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-recommend-timeline.json`](../../../../catalog/models/weibo/web-v2/user-recommend-timeline.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-recommend-timeline
