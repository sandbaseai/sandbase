# Weibo Hot Search Index API: pricing, parameters and code examples

`weibo/web-v2/hot-search-index` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the top 10 hot search ranking items currently trending on Weibo. It delivers active search topics without requiring any input parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/hot-search-index"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/hot-search-index', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/hot-search-index", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/hot-search-index", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/hot-search-index` with the body above minus `model`.

## Details

Returns the current Weibo hot search ranking as a list of trending topics, each with its rank, label and a numeric heat value. It needs no input, so send an empty JSON object `{}`.

### Use cases

- Show the current top Weibo topics on a media monitoring dashboard.
- Log the ranking at set times to see which topics enter or leave the list.
- Flag topics carrying a `新` (new) label to catch fresh stories early.
- Build search links to open the Weibo results page for each trending topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/hot-search-index" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "hotgovs": [
    {
      "emoticon_url": "",
      "flag": 2,
      "icon": "https://simg.s.weibo.com/moter/flags/2_0.png",
      "icon_desc": "热",
      "icon_desc_color": "#ff9406",
      "icon_height": 24,
      "icon_info": "<i class=\"icon-txt icon-txt-len-1\"  style=\"background-color:#ff9406;\">热</i>",
      "icon_width": 24,
      "name": "乌镇网事",
      "pos": 1,
      "search_url": "/weibo?q=%23%E4%B9%8C%E9%95%87%E7%BD%91%E4%BA%8B%23&Refer=new_time",
      "show_idx": 1
    }
  ],
  "list": [
    {
      "description": "2173490",
      "emoticon": "",
      "emoticon_url": "",
      "flag": 2,
      "icon": "https://simg.s.weibo.com/moter/flags/2_0.png",
      "icon_desc": "热",
      "icon_desc_color": "#ff9406",
      "icon_height": 24,
      "icon_info": "<i class=\"icon-txt icon-txt-len-1\"  style=\"background-color:#ff9406;\">热</i>",
      "icon_width": 24,
      "label_name": "热",
      "note": "赴港看演唱会女孩低保已被取消"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `list[].word / list[].note` | The topic text as shown in the ranking. Both hold the same phrase in the sample. |
| `list[].word_scheme` | The topic wrapped in `#` hashtag marks, for example `#赴港看演唱会女孩低保已被取消#`. |
| `list[].num / list[].description` | The numeric heat value for the topic. `description` holds the same number as a string. |
| `list[].realpos / list[].show_idx` | The rank position of the topic in the list, starting at `1`. |
| `list[].label_name / list[].icon_desc` | The short label on the topic, such as `热` (hot) or `新` (new). |
| `list[].flag` | A numeric code for the label type. In the sample, `2` goes with `热` and `1` goes with `新`. |
| `list[].icon / list[].icon_desc_color` | The label icon image URL and the hex color used for the label. |
| `list[].search_url` | A relative Weibo search path for the topic. It carries the encoded hashtag query and the `band_rank` value. |
| `hotgovs[].word / hotgovs[].pos` | A separate short list of topics with their position. The sample shows one item with `pos` set to `1`. |
| `hotgovs[].search_url` | A relative Weibo search path for the topic in `hotgovs`. |

### Notes

- The request takes no parameters. Send `{}` as the body.
- The `search_url` values are relative paths that start with `/weibo?q=`. Add the Weibo host yourself to build a full link.
- For a longer ranking, try [Weibo Real-Time Hot Search](/apis/weibo/web-v2/hot-search) or [Weibo Hot Search List](/apis/weibo/web-v2/hot-search-summary).
- To find posts about a topic, pass its `word` to [Weibo Topic Search](/apis/weibo/web-v2/topic-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/hot-search-index.json`](../../../../catalog/models/weibo/web-v2/hot-search-index.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/hot-search-index
