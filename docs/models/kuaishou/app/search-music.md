# Kuaishou Music Search API: pricing, parameters and code examples

`kuaishou/app/search-music` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Searches for Kuaishou music tracks by song name or artist keyword. Returns matched audio results with support for cursor-based pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-music", "keyword": "周杰伦"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-music', {'keyword': '周杰伦'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-music", {
  "keyword": "周杰伦"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-music", sandbase.Params{
	"keyword": "周杰伦",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-music` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | Cursor, empty for first page default `""` |

## Details

This API searches Kuaishou music tracks by a keyword such as a song name or artist. It returns a list of matching tracks with artist, audio file URLs, cover image URLs and the number of videos that use each track. It needs one input, `keyword`.

### Use cases

- Find a Kuaishou track by song name and get its audio file links.
- Check how many videos use a track through `photoCount` to compare how widely tracks are used.
- Collect artist names and cover images for tracks that match a brand or topic keyword.
- Page through all tracks for a keyword to build a list of candidate background music.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-music" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes |  |
| `pcursor` | string | No | Cursor, empty for first page |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "debug_id": "0aaa3f4e",
  "debug_info": "gAAAAABq6Y7kVwuWPVSr5AxutSUvuEhTYuEnWaNJikRmlceIe0iPndQ0PZLi3oQasB3YxlXnvm3d_XGC…",
  "extParams": {
    "disablePhotoInsert": false,
    "dynamicShard": false,
    "isCreativeMode": false,
    "isShowPymkUserPhotos": true,
    "isShowScrollTopButton": false,
    "livePendantResource": "https://static.yximgs.com/udata/pkg/ks-nearby/nearby_living_tag/origin_196uxh2cv…",
    "outerStreamFetch": 6,
    "pageSingleDoubleStyle": 0,
    "rsRecoAfterPlayInterval": 2,
    "searchTaskParam": {},
    "sessionParams": "",
    "streamExtParams": "{\"single\":false,\"predict\":false,\"searchDetailCost\":{\"filterItem\":1,\"getView\":47}…"
  },
  "host-name": "public-bjzey-c97-kce-node21.idchb1az3.hb1.kwaidc.com",
  "llsid": "2006451174999715826",
  "musics": [
    {
      "atmosphereType": 0,
      "extInfo": {
        "itemPlugin": true,
        "mortiseDelivery": false
      },
      "isSingleColumnMode": false,
      "itemTransferInfo": "{\"refer_single_double_type\":0}",
      "itemType": 2,
      "photoCount": 5656,
      "rank": 0,
      "tag": {
        "durationPlayTrail": 272000,
        "hideArtist": false,
        "id": 1125906107083767,
        "invalid": false,
        "isCollected": false,
        "isKaraoke": false,
        "music": {
          "analysisResult": {
            "beats": [
              {
                "algorithm": "main",
                "beatsUrls": [
                  {
                    "cdn": "tx2.a.yximgs.com",
                    "url": "http://tx2.a.yximgs.com/udata/music/bm_mKWV7i3cNc4_3c6ba8bf0c_MMU_BEATS_main.dat"
                  }
                ]
              }
            ]
          },
          "artist": "亿阳",
          "audioType": 1,
          "audioUrls": [
            {
              "cdn": "v1-plat-fdl.wsukwai.com",
              "url": "https://v1-plat-fdl.wsukwai.com/ksc2/NVfoQ6SQeydXGUJ_wXMDWTUsxW8mb2ITbzWWpdCDLCk…"
            }
          ],
          "avatarUrl": "http://tx2.a.yximgs.com/udata/music/bm_TDMexlTlk-Q_v.jpg",
          "avatarUrls": [
            {
              "cdn": "tx2.a.yximgs.com",
              "url": "http://tx2.a.yximgs.com/udata/music/bm_TDMexlTlk-Q_v.jpg"
            }
          ],
          "chorus": 89600,
          "copyrightTimeLimit": 60
        },
        "photoCount": 5656
      }
    }
  ],
  "pcursor": "1",
  "portalFlag": true,
  "recoPcursor": "no_more",
  "responseCode": 0,
  "result": 1,
  "ussid": "NF8wXzE3OTM2OTEzNjMzNTVfXzg2MDE"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `musics[]` | List of matched music tracks for the keyword. |
| `musics[].tag.id` | ID of the music track. |
| `musics[].tag.music.artist` | Artist name shown for the track. |
| `musics[].tag.music.audioUrls[].url` | Link to the track's audio file (`.m4a`). Each entry has a `cdn` host name and a `url`. |
| `musics[].tag.music.avatarUrl` | Cover image URL for the track. `avatarUrls[]` lists the same image on different hosts. |
| `musics[].photoCount / musics[].tag.photoCount` | Number of videos that use this track. |
| `musics[].tag.music.duration / musics[].tag.durationPlayTrail` | Track length values. `duration` appears on some tracks and `durationPlayTrail` on all of them. In the sample, `duration` is 131 and `durationPlayTrail` is 131000 for the same track. |
| `musics[].tag.music.chorus` | Chorus value for the track. Only some tracks include it. |
| `musics[].tag.music.analysisResult.beats[]` | Beat analysis files for the track. Each entry has an `algorithm` name (`main`, `downbeats`, `segmentation`) and `beatsUrls[]` with download links. |
| `musics[].rank` | Position value of the track in the result set. |
| `pcursor` | Cursor for the next page. Pass it as `pcursor` in the next request. |

### Notes

- Leave `pcursor` empty for the first page. Send the returned `pcursor` value to get the next page.
- `recoPcursor` returned `no_more` in the sample response.
- Audio URLs carry a `pkey` query parameter in the link, so use the full URL as returned.
- For chart-style music lists, see [Kuaishou Music Ranking](/apis/kuaishou/app/music-ranking).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-music.json`](../../../../catalog/models/kuaishou/app/search-music.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-music
