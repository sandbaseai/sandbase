# Weibo Hot Ranking Timeline API: pricing, parameters and code examples

`weibo/web-v2/hot-ranking-timeline` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns popular posts from Weibo hot rankings based on a specified ranking type. Supports pagination using cursor and identifier parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/hot-ranking-timeline", "count": 10, "max_id": "0", "ranking_type": "hour", "since_id": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/hot-ranking-timeline', {'count': 10, 'max_id': '0', 'ranking_type': 'hour', 'since_id': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/hot-ranking-timeline", {
  "count": 10,
  "max_id": "0",
  "ranking_type": "hour",
  "since_id": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/hot-ranking-timeline", sandbase.Params{
	"count": 10,
	"max_id": "0",
	"ranking_type": "hour",
	"since_id": "0",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/hot-ranking-timeline` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count (default 10) default `10` |
| `max_id` | string |  | Pagination cursor, pass "0" for first request default `"0"` |
| `since_id` | string |  | Pagination identifier, default is 0 default `"0"` |
| `ranking_type` | string | yes | Ranking type (required)  |

## Details

Returns a page of popular Weibo posts from a hot ranking list. It needs a `ranking_type` value such as `hour`, and it accepts `count`, `max_id` and `since_id` for paging.

### Use cases

- Pull the posts that currently lead the hourly Weibo hot ranking into a trend dashboard.
- Compare like and comment counts across ranked posts to find the ones with the most engagement.
- Collect the super topics attached to hot posts to see which fan communities drive current traffic.
- Download the image URLs of ranked posts for visual trend or media monitoring.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/hot-ranking-timeline" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ranking_type": "hour"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ranking_type` | string | Yes | Ranking type (required) |
| `count` | integer | No | Count (default 10) |
| `max_id` | string | No | Pagination cursor, pass "0" for first request |
| `since_id` | string | No | Pagination identifier, default is 0 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "max_id": 2,
  "ok": 1,
  "since_id": 0,
  "statuses": [
    {
      "analysis_extra": "",
      "annotations": [
        {
          "photo_sub_type": "0,0,0,0,0,0,0,0,0,0,0"
        }
      ],
      "attitudes_count": 73749,
      "attitudes_status": 0,
      "buttons": [
        {
          "actionlog": {
            "act_code": "91",
            "act_type": "1",
            "cardid": "102803_-_mbloglist_5361174142779827",
            "ext": "uid:1802369094|mid:5361174142779827|act:follow|time:1793691984|source:8999|recom…",
            "fid": "102803_ctg1_1761_-_ctg1_1761",
            "oid": "1802369094",
            "source": "hot",
            "uicode": ""
          },
          "name": "关注",
          "params": {
            "able_recommend": 1,
            "extparams": {
              "followcardid": "1028030098_5361174142779827"
            },
            "uid": 6643123988
          },
          "pic": "http://u1.sinaimg.cn/upload/2013/07/02/timeline_card_small_button_icon_add.png",
          "type": "follow"
        }
      ],
      "can_edit": false,
      "comment_manage_info": {
        "approval_comment_type": 0,
        "comment_anon_type": 0,
        "comment_permission_type": -1,
        "comment_sort_type": 0
      },
      "comments_count": 11539,
      "common_struct": [
        {
          "actionlog": {
            "act_code": "300",
            "cardid": "",
            "ext": "common_struct:topic|containerid:100808|uid:1802369094|mid:5361174142779827|analy…",
            "fid": null,
            "lfid": null,
            "luicode": null,
            "mid": 5361174142779827,
            "oid": "1022:100808f57b3faeb25f86b43a8cc58f02286f40"
          },
          "btn_show_type": "1",
          "buttons": [
            {
              "actionlog": {
                "act_code": 577,
                "cardid": "",
                "ext": "common_struct:topic|containerid:100808|uid:1802369094|mid:5361174142779827|analy…",
                "fid": null,
                "lfid": null,
                "luicode": null,
                "mid": 5361174142779827,
                "oid": "1022:100808f57b3faeb25f86b43a8cc58f02286f40"
              },
              "name": "关注",
              "params": {
                "scheme": "${scheme}",
                "type": "page",
                "uid": "1022:100808f57b3faeb25f86b43a8cc58f02286f40"
              },
              "pic": "https://n.sinaimg.cn/photo/ab36dac5/20170616/follow_hollow.png",
              "type": "follow"
            }
          ],
          "desc": "5.6亿帖子 1537万小飞侠",
          "hidden": 1,
          "img": "http://wx3.sinaimg.cn/thumbnail/e6e53908ly8iiaw440dk5j20u00u0q78.jpg",
          "name": "【超话】肖战",
          "page_id": "100808f57b3faeb25f86b43a8cc58f02286f40"
        }
      ],
      "content_auth": 0,
      "created_at": "Tue Nov 03 14:23:04 +0800 2026",
      "favorited": false
    }
  ],
  "total_number": 100
}
```

### Response fields

| Field | Meaning |
|---|---|
| `statuses[]` | List of ranked posts. Each item is one Weibo post. |
| `statuses[].mblogid / statuses[].mid / statuses[].id` | Identifiers of the post. `mblogid` is a short alphanumeric code, while `mid` and `id` hold the same long numeric ID as a string and a number. |
| `statuses[].created_at` | Publish time of the post as a text date with a `+0800` offset, for example `Tue Nov 03 14:23:04 +0800 2026`. |
| `statuses[].attitudes_count / statuses[].comments_count` | Number of likes and number of comments on the post. |
| `statuses[].number_display_strategy.display_text` | Short label Weibo shows for large counts, for example `100万+`. |
| `statuses[].isLongText` | `true` when the post has long text content. |
| `statuses[].pic_ids[]` | IDs of the images in the post. Use each ID as a key in `statuses[].pic_infos`. |
| `statuses[].pic_infos.*.original.url / statuses[].pic_infos.*.large.url` | Image URLs at different sizes, with `width` and `height` next to each URL. |
| `statuses[].common_struct[].name / statuses[].common_struct[].desc` | Name and short description of the topic or super topic linked to the post, for example `【超话】肖战`. |
| `max_id / since_id` | Paging values returned with the list. Use them in the next request. |

### Notes

- Pass `max_id` as `"0"` on the first request. Send the `max_id` value from the response to get the next page.
- `count` sets how many posts to return per request. The default is 10.
- Use the `mblogid` or `id` of a post with [Weibo Post Detail](/apis/weibo/web-v2/post-detail) or [Weibo Post Comments](/apis/weibo/web-v2/post-comments) to get more about a single post.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/hot-ranking-timeline.json`](../../../../catalog/models/weibo/web-v2/hot-ranking-timeline.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/hot-ranking-timeline
