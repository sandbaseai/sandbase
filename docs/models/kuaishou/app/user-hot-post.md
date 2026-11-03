# Kuaishou User Hot Posts API: pricing, parameters and code examples

`kuaishou/app/user-hot-post` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns popular posts from a specified Kuaishou user profile, including captions and interaction metrics such as comments and collects.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/user-hot-post", "user_id": "3795214411"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/user-hot-post', {'user_id': '3795214411'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/user-hot-post", {
  "user_id": "3795214411"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/user-hot-post", sandbase.Params{
	"user_id": "3795214411",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/user-hot-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pcursor` | string |  | 作品游标/Post cursor  |
| `user_id` | string | yes | 用户ID/User ID  |

## Details

Returns a list of popular posts from one Kuaishou user profile. Each post includes the caption, video duration, cover images, and counts for likes, comments, collects and forwards. The only required input is the user's numeric `user_id`.

### Use cases

- Rank a creator's posts by `like_count` to find which videos performed best.
- Compare `comment_count` and `collect_count` across a creator's popular posts to see which content gets saved or discussed.
- Collect `caption` text and hashtags from top posts to study how a creator titles popular videos.
- Download cover image URLs from `cover_thumbnail_urls` to build a gallery of a creator's top posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/user-hot-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3795214411"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes |  |
| `pcursor` | string | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "feeds": [
    {
      "adminTags": [],
      "bottomEntryInfo": {
        "bizExtraData": {},
        "bottomBizType": 14,
        "bottomStyleInfo": {
          "bottomStrongStyle": {
            "actionUrl": "",
            "backgroundColor": "",
            "bottomStrongStyleType": 0,
            "enableForceClose": false,
            "fontColor": "",
            "fontSize": 0,
            "iconHeight": 0,
            "iconUrl": ""
          },
          "bottomWeakStyle": {
            "actionUrl": "kwai://search?keyword=回村往事&sessionId=MzIwXzBfMTc5MzY5MTM3MTEwN19fMjE3MA&source=s…",
            "backgroundColor": "#444444",
            "bottomWeakStyleType": 0,
            "enableForceClose": false,
            "fontColor": "#FFFFFF",
            "fontSize": 13,
            "iconHeight": 48,
            "iconRightMargin": 4.0
          },
          "delayShowWeakStyle": false,
          "playVideoEndToStrongMillis": 0,
          "showStrongVideoCountdownMillis": 0,
          "showStrongVideoMillis": 0,
          "strongStyleCloseHideWeakStyle": false,
          "styleTriggers": []
        },
        "eventTrackData": {
          "all_source": "p2q_semantic_recall_v4",
          "entry_source": "search_entrance_featured_bottom_bar_profile",
          "is_hotbar": "\u0000",
          "query_id": "189c614ada146afe04ed891f00542f89",
          "query_list_id": "MzIwXzBfMTc5MzY5MTM3MTEwN19fMjE3MA",
          "query_name": "回村往事",
          "rel_score": "0.957747",
          "stg_recall_source": "p2q_semantic_recall_v4"
        }
      },
      "canShowQuickCommentGuide": true,
      "caption": "回村往事@李秀妍u(O4489551526) #李秀妍u",
      "captionToComment": "回村往事@李秀妍u(O4489551526) #李秀妍u",
      "collect_count": 8386,
      "commentGuessSearch": {
        "displayPrefix": "相关搜索：",
        "extParams": "{\"all_source\":\"p2q_semantic_recall_v8,p2q_recall_exp_v17\",\"entrySource\":\"search_…",
        "iconUrl": "https://ali2.a.kwimgs.com/udata/pkg/se-cdn/search_blue3x.png",
        "searchWord": "李秀妍和榜一大哥的视频",
        "searchWordMD5": "c541e248be165bd097c418eb43aa4a47",
        "searchWordUrl": "kwai://search?keyword=李秀妍和榜一大哥的视频&sessionId=MzIwXzBfMTc5MzY5MTM3MTEwN19fMjE3MA&s…",
        "sessionId": "MzIwXzBf…"
      },
      "commentInfo": {
        "commentCountSpecialEffect": true,
        "commentEducationGuide": {
          "guideType": 0,
          "triggerCharCount": 0
        },
        "commentIconType": 0,
        "enableAIPresetGuide": false,
        "permissions": 191
      },
      "commentTopBarPriority": [
        {
          "bizType": "PLC",
          "subBizType": "51"
        }
      ],
      "comment_count": 4097,
      "contactRelationFriend": false,
      "coronaVipInfo": {
        "enableFilmAd": false,
        "filmAdInfo": {
          "pageId": 100014436,
          "posId": 9777,
          "subPageId": 100017199
        },
        "inspireAdInfo": {
          "pageId": 100011251,
          "posId": 20578,
          "subPageId": 100024209
        },
        "vipPhoto": false
      }
    }
  ],
  "host-name": "public-bjx-c34-kce-node2128.idchb1az1.hb1.kwaidc.com",
  "isUnfollowFeeds": false,
  "llsid": "2006449521242258738",
  "pcursor": "20",
  "result": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `feeds[]` | One popular post from the user's profile. |
| `feeds[].caption` | Post text, including hashtags and @mentions. It can be an empty string. |
| `feeds[].like_count / feeds[].comment_count / feeds[].collect_count / feeds[].forward_count` | Counts of likes, comments, collects and forwards for the post. |
| `feeds[].duration` | Length of the video as a number, for example `129349`. The `ext_params.video` field holds a nearly identical number. |
| `feeds[].ext_params.w / feeds[].ext_params.h` | Video width and height values, for example `720` and `960`. |
| `feeds[].cover_thumbnail_urls[].url` | Cover image URL for the post. Each entry also has a `cdn` host name. |
| `feeds[].headurls[].url` | Avatar image URL of the post author. Each entry also has a `cdn` host name. |
| `feeds[].commentGuessSearch.searchWord` | Suggested related search phrase shown with the post's comments. |
| `feeds[].editInfo.editTime` | Time the post was last edited, as a 13-digit timestamp such as `1775816488646`. |
| `feeds[].exp_tag` | Tag string that contains the post identifier, for example `1_i/2006449521242258738_phot`. |

### Notes

- Pass `pcursor` to request further results. Leave it out for the first request.
- The `user_id` is a numeric string, such as `3795214411`. To find a user's ID, try [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id).
- For a user's full video list instead of popular posts, use [Kuaishou User Video List (V2)](/apis/kuaishou/app/user-post-v2).
- Many fields, such as `bottomEntryInfo` and `feedSwitches`, hold display and tracking settings and are not needed for most uses.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/user-hot-post.json`](../../../../catalog/models/kuaishou/app/user-hot-post.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/user-hot-post
