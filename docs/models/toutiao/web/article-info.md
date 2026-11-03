# Toutiao Article Details (Web) API: pricing, parameters and code examples

`toutiao/web/article-info` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed post information and interface action settings for a specified Toutiao article based on its unique post identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/web/article-info", "aweme_id": "7450114952884503059"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/web/article-info', {'aweme_id': '7450114952884503059'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/web/article-info", {
  "aweme_id": "7450114952884503059"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/web/article-info", sandbase.Params{
	"aweme_id": "7450114952884503059",
})
```

Same call via the path form: `POST /v1/api/toutiao/web/article-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Post ID  |

## Details

Returns the details of one Toutiao article: title, HTML body, publish time, source account, images, engagement counters and action bar settings. It needs one input, the article's post ID in `aweme_id`.

### Use cases

- Archive the title, HTML body and original source link (`src_link`) of a news article by its ID.
- Track the read, show, like, comment and share counts of a single article over repeated calls.
- Identify the publishing account of an article and read its verification text and description.
- Download the cover and detail images of an article in several sizes and formats.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/web/article-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7450114952884503059"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Post ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "aggr_type": 1,
    "audio_id": "7450115760640229924",
    "content": "\n\n\n<header><div class=\"tt-title\">“海阳船”再发“海阳箭”——谷神星一号海遥四运载火箭发射成功</div><div class=…",
    "content_hash": "e6b66251",
    "group_id": 7450114952884503059,
    "group_source": 2,
    "h5_extra": {
      "audio_info": {
        "audioDuration": 248,
        "audioGroupID": "7450115760640229924",
        "audioID": 7450115760640229924,
        "audioWatchBar": "LARGE_BAR",
        "audioWatchBarContent": "听全文",
        "audioWatchCount": 27,
        "audioWatchCountShowText": "文章较长试试听",
        "logPB": {
          "audioGroupSource": "578",
          "category_name": "toutiao_audio",
          "recommend_reason": "文章较长试试听",
          "stream_channel_id": "0"
        }
      },
      "avatar": "https://p3-sign.toutiaoimg.com/user-avatar/14194628f142c924cb14b638f6b04d91~300x…",
      "diversity": {
        "publish_loc_info": "山东"
      },
      "g_composition": 8,
      "g_source": 2,
      "is_lite": 1,
      "is_original": false,
      "itemCell": {
        "actionCtrl": {
          "actionBar": {
            "actionSettingList": [
              {
                "actionType": 1,
                "styleSetting": {
                  "iconKey": "分享的Icon",
                  "layoutDirection": 0,
                  "text": "分享"
                }
              }
            ]
          },
          "actionTimeInSec": "0",
          "banBury": false,
          "banComment": false,
          "banDigg": false,
          "feedbackBotSchema": "sslocal://gpt_detail/second_page?bot_id=7504969938109579302&ailog_extra=%7B%22bo…",
          "preloadWeb": 2
        },
        "articleBase": {
          "articleVersion": 0,
          "gidStr": "7450114952884503059",
          "itemStatus": 20
        },
        "articleClassification": {
          "aggrType": 1,
          "articleSubType": 0,
          "articleType": 0,
          "bizID": 10,
          "bizTag": 22,
          "groupSource": 2,
          "isOriginal": false,
          "isSubject": false
        },
        "cellCtrl": {},
        "extra": {
          "ping": "pong"
        },
        "imageList": {},
        "itemCounter": {
          "buryCount": 0,
          "commentCount": 1,
          "diggCount": 3,
          "forwardCount": 0,
          "readCount": 95,
          "repinCount": 1,
          "shareCount": 9,
          "showCount": 3479
        },
        "relatedInfo": {}
      },
      "media": {
        "auth_info": "闪电新闻官方账号",
        "avatar_url": "https://p3-sign.toutiaoimg.com/user-avatar/14194628f142c924cb14b638f6b04d91~300x…",
        "can_be_praised": false,
        "car_author": 0,
        "creator_id": 51050126444,
        "description": "闪电新闻，先声夺人。山东广播电视台倾力打造的融媒体客户端。",
        "id": 51201073347,
        "master_media_info": ""
      },
      "media_user_id": "51050126444",
      "name": "闪电新闻",
      "publish_stamp": "1734615075"
    },
    "image_detail": [
      {
        "height": 4000,
        "image_type": 1,
        "uri": "large/tos-cn-i-tjoges91tu/0db73b409bfcbc388e7995c7460eff7a",
        "url": "https://p3-sign.toutiaoimg.com/large/tos-cn-i-tjoges91tu/0db73b409bfcbc388e7995c…",
        "url_list": [
          {
            "url": "https://p3-sign.toutiaoimg.com/large/tos-cn-i-tjoges91tu/0db73b409bfcbc388e7995c…"
          }
        ],
        "width": 6000
      }
    ],
    "is_wenda": 0,
    "item_id": 7450114952884503059,
    "main_image_list": [
      {
        "height": 370,
        "image_type": 0,
        "uri": "tos-cn-i-tjoges91tu/0db73b409bfcbc388e7995c7460eff7a",
        "url": "https://p3-sign.toutiaoimg.com/tos-cn-i-tjoges91tu/0db73b409bfcbc388e7995c7460ef…",
        "url_list": [
          {
            "url": "https://p3-sign.toutiaoimg.com/tos-cn-i-tjoges91tu/0db73b409bfcbc388e7995c7460ef…"
          }
        ],
        "width": 540
      }
    ],
    "media_user_id": 51050126444
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title / data.source` | Article title and the name of the publishing source account. |
| `data.content` | Article body as an HTML string, including the title block and author bar. |
| `data.publish_time / data.publish_stamp` | Publish time as a text date (`2024-12-19 21:31`) and as a Unix timestamp string. |
| `data.src_link` | Link to the original article on the source publisher's own site. |
| `data.h5_extra.itemCell.itemCounter.readCount / showCount / diggCount / commentCount / shareCount / repinCount` | Engagement counters for the article. `showCount` is the number of shows and `readCount` is the number of reads. |
| `data.h5_extra.media.auth_info / data.h5_extra.media.description` | Verification label and profile description of the publishing account. |
| `data.media_user_id` | ID of the publishing account. The same value appears as a string in `data.h5_extra.media_user_id`. |
| `data.h5_extra.itemCell.actionCtrl.actionBar.actionSettingList[]` | Action bar buttons for the article. Each entry has an `actionType` and a `styleSetting` with the button `text` and icon key. |
| `data.h5_extra.itemCell.actionCtrl.banComment / banDigg / banBury` | Flags that show whether commenting, liking and burying are turned off for the article. |
| `data.image_detail[].url / data.origin_image_list[].url / data.thumb_image[].url` | Image URLs in detail, original and thumbnail versions. Each entry also gives `width` and `height`. |

### Notes

- `data.group_id`, `data.item_id` and `data.str_item_id` all hold the same ID as the `aweme_id` you sent.
- `data.h5_extra.audio_info` gives `audioDuration` and the audio ID when an audio version of the article exists.
- To read the reader comments on a post, call [Toutiao Post Comments](/apis/toutiao/app/comments).
- For the author's profile, use [Toutiao User Profile](/apis/toutiao/app/user-info) with the account ID.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Toutiao Specified Video Details](/apis/toutiao/web/video-info): Returns detailed information for a specified Toutiao video post.

---
Machine-readable: [`catalog/models/toutiao/web/article-info.json`](../../../../catalog/models/toutiao/web/article-info.json) · Store page: https://www.sandbase.ai/model/toutiao/web/article-info
