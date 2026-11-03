# Zhihu Search Suggestions API: pricing, parameters and code examples

`zhihu/web/search-suggest` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns search query suggestions and related topics from Zhihu based on a specified search keyword.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/search-suggest", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/search-suggest', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/search-suggest", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/search-suggest", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/search-suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search Keywords  |

## Details

Returns a list of Zhihu search suggestions for a keyword. It needs one input, `keyword`, and returns the suggested queries with an ID, a tab type and an optional label and icon for each.

### Use cases

- Fill a search box with Zhihu autocomplete suggestions as a user types.
- Collect the long-tail queries people use around a brand or topic such as `OpenAI`.
- Spot trending phrasing around a keyword to plan content titles.
- Seed a keyword list, then run each suggestion through a Zhihu search API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/search-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attached_info": "OioSIDQ5NDM5NGJhY2Y1MDIwNTQ4NDIzNDczMDA4ZDBhMDM0agZPcGVuQUk=",
  "input_hash_id": "494394bacf5020548423473008d0a034",
  "suggest": [
    {
      "attached_info": "OioSIDQ5NDM5NGJhY2Y1MDIwNTQ4NDIzNDczMDA4ZDBhMDM0agZPcGVuQUnyAksKIDQ5NDM5NGJhY2Y1…",
      "height": 14,
      "icon_url": "https://picx.zhimg.com/80/v2-14647b51c955b4cd339e3f2150d45b9a_1440w.png",
      "id": -2962146858830793432,
      "label": "activity_topic",
      "query": "OpenAI",
      "raw_id": "-2962146858830793432",
      "tab_type": "general",
      "target_url": "",
      "width": 26
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `suggest[]` | List of suggestion entries for the keyword, in the order returned. |
| `suggest[].query` | The suggested search phrase as plain text. |
| `suggest[].id / suggest[].raw_id` | Identifier of the suggestion. `raw_id` is the same number as a string, which is safer for tools that lose precision on large integers. |
| `suggest[].label` | Type tag for the suggestion. A value such as `activity_topic` marks a topic entry. It is an empty string on plain query suggestions. |
| `suggest[].tab_type` | Search tab the suggestion belongs to. The sample entries all return `general`. |
| `suggest[].icon_url / suggest[].width / suggest[].height` | Icon image for the suggestion with its size. Plain query suggestions return an empty `icon_url` and `0` for both sizes. |
| `suggest[].target_url` | Link target for the suggestion. It is an empty string in the sample. |
| `suggest[].attached_info` | Opaque token attached to each suggestion. Pass it unchanged if you need to refer back to it. |
| `input_hash_id` | Hash string that identifies the input keyword. |

### Notes

- `keyword` is the only parameter and it is required. Send the text the user has typed so far.
- Large `id` values can exceed the safe integer range in some languages. Use `raw_id` when you need an exact value.
- To search content for a suggested phrase, pass it to [Zhihu Article Search](/apis/zhihu/web/article-search-v3) or [Zhihu Topic Search (V3)](/apis/zhihu/web/topic-search-v3).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/search-suggest.json`](../../../../catalog/models/zhihu/web/search-suggest.json) · Store page: https://www.sandbase.ai/model/zhihu/web/search-suggest
