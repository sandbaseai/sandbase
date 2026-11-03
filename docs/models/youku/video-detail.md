# Youku Video Details API: pricing, parameters and code examples

`youku/video-detail` · data API · Youku · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get details for a Youku video identified by video ID. Use it to look up a known video for content review, cataloging, or subsequent video analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youku/video-detail", "videoId": "XNjU1ODM3MjI4NA=="}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youku/video-detail', {'videoId': 'XNjU1ODM3MjI4NA=='})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youku/video-detail", {
  "videoId": "XNjU1ODM3MjI4NA=="
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youku/video-detail", sandbase.Params{
	"videoId": "XNjU1ODM3MjI4NA==",
})
```

Same call via the path form: `POST /v1/api/youku/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `videoId` | string | yes | The unique identifier for the video.  |

## Details

Returns the details of one Youku video as the platform's page data. The response includes the title, description, rating, uploader, duration and playback flags. It needs one input, the `videoId`.

### Use cases

- Check the title, description and category of a known Youku video before approving it for a content review.
- Add a video to a catalog with its title, cover image, area and duration.
- Read the uploader name and `ownerUid` to find who published a video.
- Filter videos by flags such as `isShort`, `allowDownload` or `allowComment` before further analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youku/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"videoId": "XNjU1ODM3MjI4NA=="}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `videoId` | string | Yes | The unique identifier for the video. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "componentList": [
    {
      "componentId": "h5-detail-vip-guide",
      "componentName": "播放页会员引导组件",
      "dataNode": [
        {
          "data": {
            "action": {
              "callback": null,
              "contentType": null,
              "contentValue": null,
              "extra": null,
              "report": {
                "arg1": "h5_detail_vip_guide",
                "index": 1,
                "pageName": "page_playpage",
                "reportDataOpt": null,
                "scmAB": "20140719.manual",
                "scmC": "102330",
                "scmD": "crm_20140732-manual-263001_336001_1352001_207-102944_100140_0_1_21429_781_179369…",
                "spmAB": "a2h0j.10182321"
              },
              "reportConfig": null,
              "reportDisabled": false,
              "type": "JUMP_TO_NEWPAY"
            },
            "bgPic": "https://gw.alicdn.com/imgextra/i4/O1CN01Y8nnrH1L6Y7EbSbBU_!!6000000001250-2-tps-…",
            "content": {
              "bgPic": "https://gw.alicdn.com/imgextra/i4/O1CN01Y8nnrH1L6Y7EbSbBU_!!6000000001250-2-tps-…",
              "bgPicNew": "https://img.alicdn.com/imgextra/i3/O1CN01KO4sixAik7I2AooQ_!!6000000006165-1-tps-…",
              "btnText": "",
              "buttonText": null,
              "cornText": "",
              "id": null,
              "jumpType": "JUMP_TO_NEWPAY",
              "jumpUrl": "https://activity.youku.com/app/visp/cashier_5/index?en_sid=927201&en_vid=1639593…"
            },
            "mark": {
              "data": {
                "color": "RED"
              },
              "type": "SIMPLE"
            }
          },
          "id": null,
          "type": 10066
        }
      ],
      "id": 102527,
      "props": {},
      "title": "",
      "type": 10066
    }
  ],
  "drawerList": [
    {
      "componentList": [
        102527
      ],
      "id": 13679,
      "type": 10001
    }
  ],
  "headers": {
    "manufacturingDate": "20261103 15:48:07",
    "nobelTrackInfo": "1148:2646@a2h04.8165646@0@,100075:100120@atest.10010010@0@"
  },
  "nobelInfo": {
    "a2h04.8165646": {
      "0": [
        {
          "nobelId": "1148:2646"
        }
      ]
    },
    "abTestId": "100075:100120",
    "atest.10010010": {
      "0": [
        {
          "nobelId": "100075:100120"
        }
      ]
    }
  },
  "nobelTrackHeader": "",
  "playPageData": {
    "PopCallApp": {
      "btnTitle": "打开",
      "expires": 1,
      "jumpUrl": "",
      "logo": "https://gw.alicdn.com/imgextra/i3/O1CN01CO6s7L1qQvicY255E_!!6000000005491-2-tps-…",
      "subtitle": "为好内容全力以赴",
      "title": "优酷",
      "type": "JUMP_TO_NATIVE",
      "unit": "hour"
    },
    "bottomCallApp": {
      "btnTitle": "打开优酷APP更流畅",
      "jumpUrl": "",
      "type": "JUMP_TO_NATIVE"
    },
    "callSwitch": true,
    "headerCallApp": {
      "btnTitle": "下载APP",
      "jumpUrl": "",
      "type": "JUMP_TO_NATIVE"
    }
  },
  "pushInfo": {},
  "videoMap": {
    "adRestricted": 0,
    "albumId": null,
    "allowComment": true,
    "allowDownload": true,
    "allowLike": true,
    "allowShare": true,
    "allowUnionRefresh": 1,
    "animeEdition": null,
    "audiolang": [],
    "autoPay": false,
    "completed": false,
    "downloadStatus": []
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `componentList[].dataNode[].data.introTitle` | Title shown on the video's play page. |
| `componentList[].dataNode[].data.desc` | Text description of the video. |
| `componentList[].dataNode[].data.area[] / componentList[].dataNode[].data.doubanRate` | `area` lists the regions tied to the video. `doubanRate` is a rating string, here `6.0`. |
| `componentList[].dataNode[].data.img` | Cover image URL. The uploader node uses the same key for the uploader's avatar. |
| `componentList[].dataNode[].data.title / componentList[].dataNode[].data.ownerUid` | In the uploader node, `title` is the uploader's channel name and `ownerUid` is the uploader's ID. |
| `componentList[].dataNode[].data.subtitles[].subtitle` | Short uploader stat text, such as the follower count (`7.9万粉丝`). The `subtitleType` key gives its type, for example `FOLLOW`. |
| `componentList[].dataNode[].data.reservation.reservationPeopleNum / componentList[].dataNode[].data.reservation.reservationPeopleNumDesc` | Number of people who reserved the video, as a number and as display text. |
| `videoMap.duration` | Video length. The sample value is `15.13`. |
| `videoMap.pageTitle / videoMap.showCategory` | Page title of the video and its category, here `电影` (movie). |
| `videoMap.isShort / videoMap.episodeTotal` | `isShort` marks a short video. `episodeTotal` is the number of episodes. |
| `videoMap.allowComment / videoMap.allowDownload / videoMap.allowLike / videoMap.allowShare` | Boolean flags for which actions the video allows. |

### Notes

- The `videoId` is a base64-style string that ends in `==`, for example `XNjU1ODM3MjI4NA==`. To find IDs, use [Youku Video Search](/apis/youku/search-video).
- The `componentList` holds page components. Each has a `componentId`, such as `h5-detail-info`, and some entries can be empty objects. Look up the component by `componentId` instead of by position.
- To look up the uploader, use [Youku User Profile](/apis/youku/user-detail) with the uploader ID from `ownerUid`.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/youku/video-detail.json`](../../../catalog/models/youku/video-detail.json) · Store page: https://www.sandbase.ai/model/youku/video-detail
