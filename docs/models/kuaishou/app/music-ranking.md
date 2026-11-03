# Kuaishou Music Ranking API: pricing, parameters and code examples

`kuaishou/app/music-ranking` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns ranked music tracks on Kuaishou, including track IDs, titles, hot counts, and audio URLs. Supports filtering by chart type and cursor pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/music-ranking"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/music-ranking', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/music-ranking", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/music-ranking", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/music-ranking` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Page size, default 20, range 1-50 default `20` |
| `tab_id` | integer |  | 100002=hot songs (default), 100063=Pi-plan ranking default `100002` |
| `pcursor` | string |  | Cursor, empty for first page default `""` |

## Details

Returns a ranked list of music tracks from a Kuaishou chart. Each track has an ID, title, artist, a hot count, cover images and audio file URLs. No input is required, and you can pass `tab_id` to pick the chart.

### Use cases

- Track which songs are trending as background music on Kuaishou.
- Build a weekly chart snapshot of top tracks and artists for a music report.
- Download cover images, lyric files and audio previews for tracks on a chart.
- Compare the hot songs chart with the Pi-plan chart to find tracks that appear on both.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/music-ranking" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Page size, default 20, range 1-50 |
| `pcursor` | string | No | Cursor, empty for first page |
| `tab_id` | integer | No | 100002=hot songs (default), 100063=Pi-plan ranking |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "debug_id": "c835f052",
  "debug_info": "gAAAAABq6Y7Z84ABb8lDV4hTWoPnhjPx10ReH8XwOG51x82Opzzb1k4QzkGhKkOPvLY6C6IrL3l-BwyH…",
  "host-name": "public-bjy-c34-kce-node3847.idchb1az2.hb1.kwaidc.com",
  "listTitleMessage": "榜单更新于2026年10月31日",
  "musics": [
    {
      "analysisResult": {
        "beats": [
          {
            "algorithm": "main",
            "beatsUrls": [
              {
                "cdn": "tx2.a.yximgs.com",
                "url": "http://tx2.a.yximgs.com/udata/music/bm_IFKjNoN6fjQ_164866fbdf_MMU_BEATS_main.dat"
              }
            ]
          }
        ]
      },
      "artist": "周杰伦",
      "audioType": 1,
      "audioUrls": [
        {
          "cdn": "v1-plat-fdl.wsukwai.com",
          "url": "https://v1-plat-fdl.wsukwai.com/ksc2/ij9zjAXvUWifRe8PCEOj9oX6NyGjjHdv05L9fM_9q-b…"
        }
      ],
      "avatarUrl": "http://tx2.a.yximgs.com/udata/music/bgm_IFKjNoN6fjQ_-MBE-bCbRC8_scaled.jpg",
      "avatarUrls": [
        {
          "cdn": "tx2.a.yximgs.com",
          "url": "http://tx2.a.yximgs.com/udata/music/bgm_IFKjNoN6fjQ_-MBE-bCbRC8_scaled.jpg"
        }
      ],
      "begin": 1,
      "chorus": 1,
      "clickMoreUrl": "kwai://tag/electrical/5xqbk8s4a3ina96",
      "copyrightTimeLimit": 60,
      "duration": 59,
      "durationInfo": [
        {
          "durationPlayTrail": 60000,
          "durationShooting": 60000,
          "product": "KUAISHOU",
          "scene": 2
        }
      ]
    }
  ],
  "pcursor": "25",
  "result": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `musics[]` | List of ranked tracks, in chart order. |
| `musics[].id` | Track ID, a short alphanumeric string such as `5xqbk8s4a3ina96`. |
| `musics[].name / musics[].artist` | Track title and artist name. |
| `musics[].hotCount` | Popularity count as a display string with a unit suffix, such as `1996万`. It is text, not a number. |
| `musics[].duration` | Track length as a number. The shown values are 59 and 60. |
| `musics[].audioUrls[].url / musics[].url` | Audio file links in `.m4a` format. Each entry in `audioUrls` also gives the `cdn` host that serves the file. |
| `musics[].image / musics[].avatarUrl` | Cover image links for the track. |
| `musics[].lrc` | Link to a lyrics file in `.trcx` format. `mmuLrcUrls` lists `.srt` lyric files. |
| `musics[].hasCopyright` | Boolean flag for whether the track has copyright set. |
| `listTitleMessage` | Chart update note in Chinese, such as a line saying when the chart was updated. |

### Notes

- Set `tab_id` to `100002` for the hot songs chart (default) or `100063` for the Pi-plan chart.
- Set `count` from 1 to 50 for page size. The default is 20.
- Leave `pcursor` empty for the first page. Pass the cursor value from the previous response to get the next page.
- To find a track by name instead of by chart, use [Kuaishou Music Search](/apis/kuaishou/app/search-music).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/music-ranking.json`](../../../../catalog/models/kuaishou/app/music-ranking.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/music-ranking
