# Weibo Social Ranking API: pricing, parameters and code examples

`weibo/web-v2/social-ranking` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Weibo social ranking data covering current affairs, social hotspots, and livelihood topics. Call this endpoint to track top-trending public interest discussions.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/social-ranking"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/social-ranking', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/social-ranking", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/social-ranking", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/social-ranking` with the body above minus `model`.

## Details

Returns the current Weibo social ranking list, which covers current affairs, social hotspots and livelihood topics. The API takes no input. Each entry has a topic title, a heat number, a category and a rank.

### Use cases

- Show the top Weibo public affairs topics on a news dashboard.
- Log `hot_num` for each topic over time to see which stories grow fastest.
- Filter entries by `category` to collect livelihood news or official clarification notices.
- Collect the `word_scheme` hashtags to use as keywords in a post search.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/social-ranking" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "band_list": [
    {
      "category": "民生新闻",
      "emoticon": "",
      "flag": 2,
      "hot_num": 2173490,
      "icon": "https://simg.s.weibo.com/moter/flags/2_0.png",
      "icon_desc": "热",
      "icon_desc_color": "#ff9406",
      "icon_height": 24,
      "icon_url": "https://simg.s.weibo.com/moter/flags/2_0.png",
      "icon_width": 24,
      "is_hot": 1,
      "loc_page": 4
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `band_list[]` | One ranked topic in the social ranking list. |
| `band_list[].word / note` | The topic title. Both fields hold the same text in the sample. |
| `band_list[].word_scheme` | The topic written as a Weibo hashtag, such as `#警方通报九寨沟景区游客冲突事件#`. Some entries have no `#` marks. |
| `band_list[].hot_num / num` | The heat value of the topic. Higher numbers rank higher. |
| `band_list[].rank / realpos` | The position in the list. `rank` starts at 0 and `realpos` starts at 1. |
| `band_list[].category / m_category` | The topic category, for example `民生新闻` (livelihood news) or `辟谣/通报` (rumor refutation or official notice). |
| `band_list[].icon_desc` | The short label shown on the topic, such as `热`, `新` or `沸`. The flags `is_hot`, `is_new` and `is_fei` match these labels. |
| `band_list[].flag` | Numeric code for the label type. The sample shows `1` with `新`, `2` with `热` and `16` with `沸`. |
| `band_list[].subject_querys` | Related event names keyed by query text. Each value has `subject_trend` (a trend title) and `subject_type`. |
| `band_list[].icon_url` | URL of the label image for the topic. |

### Notes

- Send an empty JSON object `{}`. The API has no request parameters and no pagination.
- To read the posts behind a topic, pass its `word` to [Weibo Topic Search](/apis/weibo/web-v2/topic-search) or [Weibo Real-Time Search](/apis/weibo/web-v2/realtime-search).
- For other rankings, see [Weibo Life Ranking](/apis/weibo/web-v2/life-ranking).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/social-ranking.json`](../../../../catalog/models/weibo/web-v2/social-ranking.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/social-ranking
