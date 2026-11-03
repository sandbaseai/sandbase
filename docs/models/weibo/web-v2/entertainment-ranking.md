# Weibo Entertainment Ranking API: pricing, parameters and code examples

`weibo/web-v2/entertainment-ranking` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Weibo entertainment ranking data across entertainment, film, television, and variety shows. Provides current trending topics and media leaderboards.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/entertainment-ranking"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/entertainment-ranking', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/entertainment-ranking", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/entertainment-ranking", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/entertainment-ranking` with the body above minus `model`.

## Details

Returns the current Weibo entertainment ranking as a list of trending topics. Each entry has a topic title, a heat number, a category such as artist or TV series, and its position. The API takes no input.

### Use cases

- Show the top entertainment topics on Weibo right now in a dashboard or daily digest.
- Track which artists or TV series appear in the ranking by reading `category` and `subject_querys`.
- Compare `hot_num` between topics to see which entertainment story draws the most attention.
- Collect `word_scheme` values to build a list of hashtags to search or monitor.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/entertainment-ranking" \
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
      "category": "艺人",
      "emoticon": "",
      "flag": 2,
      "hot_num": 1437012,
      "icon_desc": "热",
      "icon_desc_color": "#ff9406",
      "is_hot": 1,
      "loc_page": 4,
      "m_category": "艺人",
      "note": "曝陈奕迅疑女儿被绿与黄泽林绝交",
      "num": 1437012,
      "rank": 0
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `band_list[]` | One ranked entertainment topic. The list is ordered by rank. |
| `band_list[].word / note` | The topic title text. In the sample, both fields hold the same text. |
| `band_list[].word_scheme` | The topic written as a Weibo hashtag, wrapped in `#` for hashtag topics. Plain topics have no `#`. |
| `band_list[].hot_num / num` | The heat number of the topic. A larger number means a higher position in the sample. |
| `band_list[].rank / realpos` | Position of the topic in the list. `rank` starts at `0` and `realpos` starts at `1`. |
| `band_list[].category / m_category` | The topic category label, for example `艺人` (artist) or `剧集` (TV series). |
| `band_list[].subject_querys` | Related subjects for the topic. Each key is a subject name, with `subject_trend` as the related trend text and `subject_type` as the subject type such as `综艺`, `剧集` or `event`. |
| `band_list[].icon_desc / icon_desc_color` | Badge label and badge color for the topic, such as `热` (hot) in orange. Only some entries have them. |
| `band_list[].is_hot / topic_flag / flag` | Numeric flags attached to the topic. The response does not explain their exact meaning. |

### Notes

- Send an empty JSON object `{}`. The API has no request parameters and no pagination.
- `rank` is zero-based and `realpos` is one-based, so the first topic has `rank` `0` and `realpos` `1`.
- Text values are in Chinese. Pass `word` to [Weibo Topic Search](/apis/weibo/web-v2/topic-search) or [Weibo Real-Time Search](/apis/weibo/web-v2/realtime-search) to find posts about a topic.
- For other Weibo rankings, see [Weibo Social Ranking](/apis/weibo/web-v2/social-ranking).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/entertainment-ranking.json`](../../../../catalog/models/weibo/web-v2/entertainment-ranking.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/entertainment-ranking
