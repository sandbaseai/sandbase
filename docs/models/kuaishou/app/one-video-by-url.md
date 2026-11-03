# Kuaishou Video Details by URL API: pricing, parameters and code examples

`kuaishou/app/one-video-by-url` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns video and photo information for a single Kuaishou post using its shared link. Input the full share URL to retrieve media metadata.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/one-video-by-url", "share_text": "https://v.kuaishou.com/cNYP0Z"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/one-video-by-url', {'share_text': 'https://v.kuaishou.com/cNYP0Z'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/one-video-by-url", {
  "share_text": "https://v.kuaishou.com/cNYP0Z"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/one-video-by-url", sandbase.Params{
	"share_text": "https://v.kuaishou.com/cNYP0Z",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/one-video-by-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_text` | string | yes | 作品链接/Photo URL  |

## Details

Returns metadata for a single Kuaishou post: caption, engagement counts, duration, cover images, author avatar and video file URLs. It needs one input, `share_text`, which is the full share URL of the post.

### Use cases

- Fetch the caption, hashtags and like count of a post from a shared Kuaishou link.
- Get the video file URLs of a post so you can archive or preview the media.
- Track `like_count`, `comment_count` and `collect_count` for a specific post over time.
- Pull cover image URLs to build link previews for Kuaishou posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/one-video-by-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_text": "https://v.kuaishou.com/cNYP0Z"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_text` | string | Yes |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "host-name": "public-bjx-c34-kce-node832.idchb1az1.hb1.kwaidc.com",
  "photos": [
    {
      "adminTags": [],
      "canShowQuickCommentGuide": true,
      "caption": "哥哥我会魔法一人就能变成两@李秀妍u(O4489551526) #李秀妍u #为自己代言",
      "captionSearchInfo": {
        "actionUrlList": [
          "kwai://search?keyword=%E5%93%A5%E5%93%A5%E6%88%91%E4%BC%9A%E9%AD%94%E6%B3%95&ses…"
        ],
        "captionSearchType": 2,
        "dataSource": 0,
        "extParams": "{\"entrySourceList\":[\"search_entrance_cap_keyword\"]}\n",
        "offsetList": [
          0
        ],
        "queryIdList": [
          "12884d6cc3162e18e00d3f66e82dc247"
        ],
        "searchWordList": [
          "哥哥我会魔法"
        ],
        "sessionId": "MzIwXzBf…"
      },
      "captionToComment": "哥哥我会魔法一人就能变成两@李秀妍u(O4489551526) #李秀妍u #为自己代言",
      "collect_count": 9947,
      "commentGuessSearch": {
        "displayPrefix": "相关搜索：",
        "extParams": "{\"all_source\":\"p2q_semantic_recall_v8\",\"entrySource\":\"search_entrance_comment_tr…",
        "iconUrl": "https://ali2.a.kwimgs.com/udata/pkg/se-cdn/search_blue3x.png",
        "searchWord": "李秀妍跳舞后背录屏",
        "searchWordMD5": "1f4a5960222268ee00ee0f66d2039d43",
        "searchWordUrl": "kwai://search?keyword=李秀妍跳舞后背录屏&sessionId=MzIwXzBfMTc5MzY5MTM3MDY4OV9fNTc4OA&sou…",
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
      "comment_count": 3053,
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
      },
      "cover_thumbnail_urls": [
        {
          "cdn": "zj66.a.kwimgs.com",
          "url": "http://zj66.a.kwimgs.com/upic/2024/12/29/22/BMjAyNDEyMjkyMjE1NDJfMzc5NTIxNDQxMV8…"
        }
      ]
    }
  ],
  "result": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `photos[]` | List of posts found for the link. A single share URL returns one item. |
| `photos[].caption` | Post text, including mentions and hashtags. |
| `photos[].like_count / comment_count / collect_count / forward_count` | Engagement counts for the post: likes, comments, collects and forwards. |
| `photos[].duration` | Video length. The value 30266 matches `ext_params.video`, so it looks like milliseconds, which fits a clip of about 30 seconds. |
| `photos[].main_mv_urls[].url` | Direct video file URL. Each item also has a `cdn` host name, so the same file is listed on several hosts. |
| `photos[].cover_thumbnail_urls[].url` | Cover image URL for the post, listed once per CDN host. |
| `photos[].headurls[].url` | Avatar image URL, listed once per CDN host. |
| `photos[].ext_params.w / h` | Width and height of the video in pixels. |
| `photos[].captionSearchInfo.searchWordList` | Search keywords parsed from the caption. |
| `photos[].commentTopBarPriority[]` | Order of the bars shown above the comments, each with `bizType` and `subBizType`. |

### Notes

- Pass the full share link, such as `https://v.kuaishou.com/cNYP0Z`, in `share_text`.
- The response has `result` set to `1` in the example call.
- Video and cover URLs include a `pkey` or `tag` query value, so use the full URL as returned.
- To read the comments of the post, call [Kuaishou Video Comments (App)](/apis/kuaishou/app/video-comment).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/one-video-by-url.json`](../../../../catalog/models/kuaishou/app/one-video-by-url.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/one-video-by-url
