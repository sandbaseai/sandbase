# Kuaishou User Video List (V2) API: pricing, parameters and code examples

`kuaishou/app/user-post-v2` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Retrieves a list of video feeds posted by a specific Kuaishou user. Supports sorting by latest or hot posts and cursor-based pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/user-post-v2", "user_id": "3795214411"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/user-post-v2', {'user_id': '3795214411'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/user-post-v2", {
  "user_id": "3795214411"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/user-post-v2", sandbase.Params{
	"user_id": "3795214411",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/user-post-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort type, latest (default) / hot. one of: `latest`, `hot` |
| `pcursor` | string |  | Video cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests.  |
| `user_id` | string | yes | 用户ID/User ID  |

## Details

Returns a list of videos posted by one Kuaishou user, with captions, engagement counts, duration, cover images and author avatar URLs. It needs the user's `user_id`, and you can sort by `latest` or `hot`.

### Use cases

- Track new uploads from a Kuaishou creator by polling the `latest` sort.
- Compare `like_count`, `comment_count` and `collect_count` across one creator's videos.
- Collect cover image URLs and captions to build a gallery of a creator's posts.
- Pull a creator's top videos with `sort` set to `hot`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/user-post-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3795214411"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes |  |
| `pcursor` | string | No | Video cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. |
| `sort` | string | No | Sort type, latest (default) / hot. |

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
            "actionUrl": "kwai://search?keyword=李秀妍&sessionId=MzIwXzBfMTc5MzY5MTM3MTM2Nl9fODE5OA&source=se…",
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
          "all_source": "p2q_semantic_recall_v8,p2q_semantic_recall_v4,p2q_recall_exp_v16,p2q_recall_exp_…",
          "entry_source": "search_entrance_featured_bottom_bar_profile",
          "is_hotbar": "\u0000",
          "query_id": "b2cff3d98343317003b3003769567d54",
          "query_list_id": "MzIwXzBfMTc5MzY5MTM3MTM2Nl9fODE5OA",
          "query_name": "李秀妍",
          "rel_score": "0.059634",
          "stg_recall_source": "p2q_recall_exp_v12"
        }
      },
      "canShowQuickCommentGuide": true,
      "caption": "#李秀妍u #刘屹琦 #喜爱度激励计划",
      "captionToComment": "#李秀妍u #刘屹琦 #喜爱度激励计划",
      "collect_count": 9,
      "commentGuessSearch": {
        "displayPrefix": "相关搜索：",
        "extParams": "{\"all_source\":\"p2q_semantic_recall_v8,p2q_semantic_recall_v4,p2q_recall_exp_v16,…",
        "iconUrl": "https://ali2.a.kwimgs.com/udata/pkg/se-cdn/search_blue3x.png",
        "searchWord": "李秀妍",
        "searchWordMD5": "b2cff3d98343317003b3003769567d54",
        "searchWordUrl": "kwai://search?keyword=李秀妍&sessionId=MzIwXzBfMTc5MzY5MTM3MTM2Nl9fODE5OA&source=se…",
        "sessionId": "MzIwXzBf…"
      },
      "commentInfo": {
        "commentEducationGuide": {
          "guideType": 0,
          "triggerCharCount": 0
        },
        "enableAIPresetGuide": false,
        "permissions": 191
      },
      "commentTopBarPriority": [
        {
          "bizType": "PLC",
          "subBizType": "51"
        }
      ],
      "comment_count": 2,
      "contactRelationFriend": false,
      "coronaCaption": {
        "captionSource": 1,
        "detailCaption": {
          "caption": "#李秀妍u #刘屹琦 #喜爱度激励计划",
          "captionSource": 1,
          "tagClickable": false
        },
        "tabCaption": "#李秀妍u #刘屹琦 #喜爱度激励计划"
      }
    }
  ],
  "host-name": "public-bjx-c26-kce-node1143.idchb1az1.hb1.kwaidc.com",
  "isUnfollowFeeds": false,
  "llsid": "2010240768896749585",
  "pcursor": "1.789836380852E12",
  "result": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `feeds[]` | One posted video. The list holds one entry per video on the page. |
| `feeds[].caption` | Caption text of the video, including hashtags. |
| `feeds[].like_count / feeds[].comment_count / feeds[].collect_count / feeds[].forward_count` | Counts of likes, comments, saves and shares for the video. |
| `feeds[].duration` | Length of the video. The value `28266` suggests milliseconds, but the response does not state the unit. |
| `feeds[].ext_params.w / feeds[].ext_params.h` | Width and height of the video. |
| `feeds[].cover_thumbnail_urls[].url` | Cover image URL for the video. Each entry lists the `cdn` host it is served from. |
| `feeds[].headurls[].url` | Avatar image URL of the posting user. Each entry lists the `cdn` host. |
| `feeds[].exp_tag` | Tag string for the item. It contains an ID with a `_p0` suffix. |
| `feeds[].liked / feeds[].following` | Flags for whether the current viewer liked the video or follows the author. Both are `0` in this response. |

### Notes

- Leave `pcursor` empty on the first call. For later pages, pass the `pcursor` value from the previous response.
- `sort` accepts `latest` (default) or `hot`.
- To find a `user_id` from a name, try [Kuaishou User Search (V2)](/apis/kuaishou/app/search-user-v2).
- For a creator's profile details, call [Kuaishou Single User Data (V2)](/apis/kuaishou/app/one-user-v2).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/user-post-v2.json`](../../../../catalog/models/kuaishou/app/user-post-v2.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/user-post-v2
