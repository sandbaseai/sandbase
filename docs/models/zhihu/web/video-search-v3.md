# Zhihu Video Search (V3) API: pricing, parameters and code examples

`zhihu/web/video-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Zhihu video search results matching a specified keyword. Supports pagination using offset and limit parameters, and accepts a search hash ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/video-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/video-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/video-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/video-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/video-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of videos per page default `"20"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `search_hash_id` | string |  | Search Hash ID default `""` |

## Details

Returns Zhihu search results for a keyword, mostly video entries with title, author, cover image and comment count. The only required input is `keyword`. Results page with `offset` and `limit`.

### Use cases

- Find Zhihu videos that mention a brand or product such as OpenAI.
- Collect video authors and their follower counts to find creators who cover a topic.
- Gather cover images and video stream URLs for videos that match a keyword.
- Page through all matches for a keyword to track new Zhihu video content over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/video-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of videos per page |
| `offset` | string | No | Offset |
| `search_hash_id` | string | No | Search Hash ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ab_params": "sb_cardfilter=1;dm_center_feature=1;dm_hotvideo=0;dm_paid_recency=0;dm_l1_rel=0;…",
  "data": [
    {
      "highlight": {
        "creator": "太空就是我",
        "description": "目前看用低端设备也能跑#<em>openai</em> #chatgpt #人工智能",
        "title": "聊聊<em>OpenAi</em>"
      },
      "hit_labels": null,
      "id": "1789796275463544832",
      "index": 0,
      "object": {
        "attached_info_bytes": "OpECCgtwbGFjZWhvbGRlchIgM2U0OWQ5ODY2OGJkMDc0NDhkMzQzNjYyZWViNDQzYzQYYyITMTc4OTc5…",
        "author": {
          "authority_info": [],
          "avatar_url": "https://pica.zhimg.com/50/v2-518e0f06c688a3657539e130dcdf6d5a_l.jpg?source=4e949…",
          "badge": [],
          "badge_v2": {
            "detail_badges": [],
            "icon": "",
            "merged_badges": [],
            "night_icon": "",
            "title": ""
          },
          "badge_v2_string": "{\"title\":\"\",\"merged_badges\":[],\"detail_badges\":null,\"icon\":\"\",\"night_icon\":\"\"}",
          "follower_count": 489,
          "gender": 1,
          "headline": "破繭尋光 選擇美麗"
        },
        "badge": [],
        "badge_v2": {
          "detail_badges": [],
          "icon": "",
          "merged_badges": [],
          "night_icon": "",
          "title": ""
        },
        "badge_v2_string": "{\"title\":\"\",\"merged_badges\":[],\"detail_badges\":null,\"icon\":\"\",\"night_icon\":\"\"}",
        "comment_count": 0,
        "cover_info": {
          "data_url": "",
          "height": 1920,
          "type": "image",
          "url": "https://picx.zhimg.com/80/v2-3d1e45814a107d146ae472b01ef5b199_qhd.jpg?source=4e9…",
          "width": 1080
        },
        "cover_url": "https://picx.zhimg.com/v2-3d1e45814a107d146ae472b01ef5b199.jpg?source=4e949a73"
      },
      "type": "zvideo"
    }
  ],
  "domain_info": {
    "first_category": ""
  },
  "filter_items": null,
  "hit_labels": null,
  "is_brand_word": false,
  "is_koc_words": false,
  "item_in_view": [
    {
      "index": 5,
      "token": "b62a7302…",
      "type": "user_survey"
    }
  ],
  "paging": {
    "is_end": false,
    "next": "https://api.zhihu.com/search_v3?advert_count=0&correction=1&filter_fields=%7B%27…"
  },
  "pendant": null,
  "related_search_result": [],
  "search_action_info": {
    "attached_info_bytes": "OqQBEiAzZTQ5ZDk4NjY4YmQwNzQ0OGQzNDM2NjJlZWI0NDNjNEoGb3BlbmFpUABYFGABagZPcGVuQUlw…",
    "isfeed": false,
    "lc_idx": 20,
    "search_hash_id": "3e49d98668bd07448d343662eeb443c4"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].type` | Kind of result. `zvideo` marks a video entry. `search_result` marks a text post that can embed a video. |
| `data[].id` | ID of the result as a string. |
| `data[].highlight.title / data[].highlight.description / data[].highlight.creator` | Title, description and creator name with the matched keyword wrapped in `<em>` tags. |
| `data[].object.author.follower_count` | Number of followers of the video author. |
| `data[].object.author.headline` | Short profile line of the author. |
| `data[].object.comment_count` | Number of comments on the item. |
| `data[].object.cover_url` | URL of the cover image for the item. |
| `data[].object.created_time` | Creation time of a `search_result` item. It looks like a Unix timestamp in seconds. |
| `data[].object.content[].playlist[]` | Video files for an embedded video, each with `quality`, `format`, `height`, `bitrate`, `size` and `url`. |
| `search_action_info.search_hash_id` | Hash ID for this search. You can pass it back in `search_hash_id` on later requests. |
| `paging.is_end` | Tells you whether the last page has been reached. `paging.next` holds the URL for the next page. |

### Notes

- Use `offset` and `limit` to move through pages. Check `paging.is_end` to know when to stop.
- The response mixes `zvideo` entries with `search_result` entries, so check `data[].type` before you read fields. Fields such as `cover_info` appear on videos, while `content` and `excerpt` appear on text posts.
- To search Zhihu articles and answers instead, call [Zhihu Article Search](/apis/zhihu/web/article-search-v3).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/video-search-v3.json`](../../../../catalog/models/zhihu/web/video-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/video-search-v3
