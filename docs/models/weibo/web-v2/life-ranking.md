# Weibo Life Ranking API: pricing, parameters and code examples

`weibo/web-v2/life-ranking` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Weibo life ranking data across categories such as food, travel, health, and fashion. Retrieves trending lifestyle lists directly from the platform.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/life-ranking"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/life-ranking', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/life-ranking", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/life-ranking", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/life-ranking` with the body above minus `model`.

## Details

Returns a list of trending Weibo topics from the life ranking. Each entry has a topic phrase, a category label, and a heat number. The request takes no input parameters, so send an empty JSON object.

### Use cases

- Track which topics are rising in the Weibo life ranking right now.
- Compare `hot_num` values to see which topics draw the most attention.
- Collect topic phrases and categories to study what people discuss on Weibo.
- Flag newly listed topics by checking the `is_new` field.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/life-ranking" \
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
      "category": "情感",
      "emoticon": "",
      "flag": 1,
      "hot_num": 683477,
      "icon": "https://simg.s.weibo.com/moter/flags/1_0.png",
      "icon_desc": "新",
      "icon_desc_color": "#ff3852",
      "icon_height": 24,
      "icon_url": "https://simg.s.weibo.com/moter/flags/1_0.png",
      "icon_width": 24,
      "is_new": 1,
      "loc_page": 3
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `band_list[]` | One ranked topic in the life ranking. |
| `band_list[].word / band_list[].note / band_list[].word_scheme` | The topic phrase as shown on Weibo. In the sample, all three hold the same text. |
| `band_list[].category / band_list[].m_category` | The category label of the topic, for example `情感` (relationships and feelings). |
| `band_list[].hot_num / band_list[].num` | The heat number of the topic. Both fields hold the same value in the sample. |
| `band_list[].rank` | Position in the list. The first item has `rank` 0. |
| `band_list[].realpos` | Position in the list, counted from 1. |
| `band_list[].is_new / band_list[].icon_desc` | `is_new` is 1 when the topic is marked new. `icon_desc` holds the badge text, such as `新`. Both appear only on some items. |
| `band_list[].icon_url` | URL of the badge image shown next to the topic. It appears only on items with a badge. |
| `band_list[].subject_querys` | Related events linked to the topic, keyed by event name. Each entry has `subject_trend` and `subject_type`. It is an empty object when there are none. |

### Notes

- The request has no parameters. Send `{}` as the body.
- `rank` starts at 0 and `realpos` starts at 1. Both give the order of the list.
- Badge fields such as `icon`, `icon_desc` and `icon_width` are missing on items without a badge.
- For other ranking lists, try [Weibo Social Ranking](/apis/weibo/web-v2/social-ranking) or [Weibo Entertainment Ranking](/apis/weibo/web-v2/entertainment-ranking).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/life-ranking.json`](../../../../catalog/models/weibo/web-v2/life-ranking.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/life-ranking
