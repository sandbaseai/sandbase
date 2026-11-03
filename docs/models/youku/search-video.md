# Youku Video Search API: pricing, parameters and code examples

`youku/search-video` · data API · Youku · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search Youku videos by keyword with page-based pagination. Use it to discover videos related to a topic, title, creator, or other search term.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youku/search-video", "keyword": "电影"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youku/search-video', {'keyword': '电影'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youku/search-video", {
  "keyword": "电影"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youku/search-video", sandbase.Params{
	"keyword": "电影",
})
```

Same call via the path form: `POST /v1/api/youku/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination, starting from 1. default `1` |
| `keyword` | string | yes | Keyword to search for.  |

## Details

Returns Youku search results for a keyword, including result cards for movies and shows with titles, categories, cast notes, and poster images. It needs one input, `keyword`, and accepts an optional `page` number.

### Use cases

- Find Youku movies and shows that match a topic or title keyword.
- Collect the `showid` of search hits to look up each title in detail.
- Read the cast and director line of each hit to match titles to a person.
- Build a list of filter options such as duration and sort order that Youku offers for a query.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youku/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "电影"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword to search for. |
| `page` | integer | No | Page number for pagination, starting from 1. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "api": "mtop.youku.soku.yksearch",
  "data": {
    "data": {
      "action": {
        "report": {
          "pageName": "page_searchresults",
          "trackInfo": {
            "aaid": "9fbffd5aabe0f1eeaa005d2258486410",
            "eid": "212c455717936920795481822ec135",
            "engine": "expid~req.ugc105.sort1004.rank105.qa0$eid~212c455717936920795481822ec135$bts~sok…",
            "k": "电影",
            "search_from": "1",
            "searchtab": "0",
            "source_from": "home"
          }
        }
      },
      "displaySearchTerms": "电影",
      "filter": {
        "cate": [
          {
            "id": "0",
            "title": "全部"
          }
        ],
        "duration": [
          {
            "title": "全部",
            "value": "0-0"
          }
        ],
        "format": [
          {
            "title": "全部",
            "value": 0
          }
        ],
        "newType": true,
        "tab": [
          {
            "id": "0",
            "orders": [
              {
                "title": "综合排序",
                "value": 0
              }
            ],
            "title": "综合排序"
          }
        ]
      },
      "globalControlParam": {
        "closeRetentionPop": true
      },
      "highlightWord": "电影",
      "hitNFMode": true,
      "isEnd": 0,
      "isModule": true,
      "pg": 1,
      "pz": 30,
      "rstate": 0,
      "status": "success"
    },
    "id": 0,
    "level": 0,
    "more": true,
    "nodes": [
      {
        "data": {
          "cateId": 7,
          "docSource": 15,
          "filters": [
            {
              "key": "3",
              "type": "0",
              "values": [
                {
                  "title": "综合",
                  "value": "sort~#0"
                }
              ]
            }
          ],
          "logCate": "programset",
          "schema": "15",
          "schemeName": "15"
        },
        "hasAfterSplitLine": true,
        "id": 0,
        "level": 1,
        "more": false,
        "nodes": [
          {
            "id": 0,
            "level": 2,
            "more": false,
            "nodes": [
              {
                "data": {
                  "areaTitle": "<em>电影</em>-影视",
                  "limitTitle": "电影"
                },
                "id": 0,
                "level": 3,
                "more": false,
                "style": [
                  {
                    "type": 0
                  }
                ],
                "type": 9003
              }
            ],
            "render": [
              {
                "type": "gaiax",
                "url": "youku://gaiax?templateId=pflix_search_component_1003&templateVersion=0.0.1&bizId…"
              }
            ],
            "style": [
              {
                "type": 0
              }
            ],
            "type": 9003
          }
        ],
        "style": [
          {
            "type": 0
          }
        ],
        "type": 1004
      }
    ],
    "type": 0
  },
  "ret": [
    "SUCCESS::调用成功"
  ],
  "traceId": "212c455717936920795481822ec135",
  "v": "2.0"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.data.total` | Total number of results for the keyword. |
| `data.data.pg / data.data.pz` | Current page number and page size. In this response they are `1` and `30`. |
| `data.data.isEnd` | Flag for the end of the results. It is `0` here, so more pages exist. |
| `data.nodes[].nodes[].nodes[].data.action.report.trackInfo.object_title` | Title of the result item, such as `空枪`. |
| `data.nodes[].nodes[].nodes[].data.action.report.trackInfo.object_url` | Youku app link for the item. It contains the `showid` of the title. |
| `data.nodes[].nodes[].nodes[].data.cats` | Category label of the item, such as `电影` (movie). |
| `data.nodes[].nodes[].nodes[].data.notice` | Text line with the director and lead cast of the item. |
| `data.nodes[].nodes[].nodes[].data.posterDTO.vThumbUrl` | URL of the poster image for the item. |
| `data.nodes[].nodes[].nodes[].data.posterDTO.labelInfo.text.title / data.nodes[].nodes[].nodes[].data.posterDTO.labelInfo.text.subTitle` | Label shown on the poster, such as a rating source and score (`豆瓣`, `8.0分`) or a ranking tag (`热度榜`, `TOP`). |
| `data.data.filter.tab[].orders[]` | Sort options with a `title` and a `value`, such as `综合排序` (`0`), `新发布` (`1`) and `播放多` (`2`). |

### Notes

- Set `page` to `2` or higher to get later pages. The first page is `1`.
- The response is deeply nested. Result cards sit in the `nodes` tree under `data.nodes`.
- The `showid` appears in `object_url` and in `item_log` as `show_id`. Use it to look up a title with [Youku Video Details](/apis/youku/video-detail).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/youku/search-video.json`](../../../catalog/models/youku/search-video.json) · Store page: https://www.sandbase.ai/model/youku/search-video
