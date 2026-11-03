# Xiaohongshu Keyword Note Search API: pricing, parameters and code examples

`xiaohongshu/search-note` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Search Xiaohongshu (RedNote) notes by keyword with page-based pagination, sorting and note-type filters. The V2 noteTime filter may return notes outside the selected time range.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/search-note", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/search-note', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/search-note", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/search-note", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/search-note` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. Start at 1, then increment page while keeping the keyword and filters unchanged. default `1` |
| `sort` | string |  | Sort order for the result set. one of: `general`, `popularity_descending`, `time_descending`, `comment_descending`, `collect_descending`; default `"general"` |
| `keyword` | string | yes | Search keyword.  |
| `noteTime` | string |  | Note publish time filter. Results may include notes published outside the selected time range. one of: `ONE_DAY`, `ONE_WEEK`, `HALF_YEAR` |
| `noteType` | string |  | Note type filter. one of: `_0`, `_1`, `_2`; default `"_0"` |

## Details

Returns a page of Xiaohongshu (RedNote) notes that match a search keyword. Each item carries engagement counts and a publish date tag. The only required input is `keyword`.

### Use cases

- Track which notes rank for a food keyword such as `美食` and how many saves and comments they have.
- Sort results by `popularity_descending` or `collect_descending` to find the most saved notes on a topic.
- Collect note IDs from search results, then pull full note details or comments for content research.
- Check the `query_intent` flags to see how the platform reads a search term.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/search-note" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `noteTime` | string | No | Note publish time filter. Results may include notes published outside the selected time range. |
| `noteType` | string | No | Note type filter. |
| `page` | integer | No | Page number for pagination. Start at 1, then increment page while keeping the keyword and filters unchanged. |
| `sort` | string | No | Sort order for the result set. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ai_mode_enable": false,
  "can_cut": false,
  "cur_cut_number": 0,
  "dqa_authorized_user_by_shared": false,
  "extra_info": {
    "atmosphere_v3_enable": "0"
  },
  "is_broad_query": true,
  "items": [
    {
      "mix_track_id": "NOTE__6ab3ef24000000001800736f__2h3wq0ok0fiwx58b9zpt7__美食",
      "model_type": "note",
      "new_help_style": false,
      "note": {
        "advanced_widgets_groups": {
          "groups": [
            {
              "fetch_types": [
                "guos_test"
              ],
              "mode": 1
            }
          ]
        },
        "click_score": 0.018783261999487877,
        "collected": false,
        "collected_count": 16088,
        "comments_count": 140,
        "corner_tag_info": [
          {
            "icon": "",
            "location": -1,
            "style": 0,
            "text": "RAhtMWDRZPq2iZ25x+orCX1alSUCEVI1eumvzosCK6L+dOYtbzjL4CMGmwv9jddH5SqVbyfSraRcvdSX…",
            "text_en": "",
            "type": "ubt_sig_token"
          }
        ],
        "cover_image_index": 0,
        "debug_info_str": ""
      }
    }
  ],
  "query_debug_info": {
    "is_forbidden": false
  },
  "query_intent": {
    "goodsIntent": 3,
    "low_supply_intent": false,
    "search_ask_intent": true
  },
  "query_type": 0,
  "request_dqa": 0,
  "request_dqa_instant": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | One search result. Page through this list to read the notes for the keyword. |
| `items[].model_type` | Type of result card. The value `note` marks a note. |
| `items[].mix_track_id` | Tracking string for the result. It contains the note ID after `NOTE__`, followed by the search request token and the keyword. |
| `items[].note.collected_count` | Number of times users saved the note. |
| `items[].note.comments_count` | Number of comments on the note. |
| `items[].note.collected` | Whether the note is saved by the requesting account. It is `false` in this response. |
| `items[].note.corner_tag_info[].text` | Tag text. For the entry with `type` set to `publish_time`, this is the publish date in `MM-DD` form, such as `09-24`. |
| `items[].note.at_user_list[]` | Users mentioned in the note, with `nickname` and `user_id`. Present only on some notes. |
| `search_request_id` | ID of this search request. |
| `query_intent` | Flags describing the search intent, such as `goodsIntent` and `search_ask_intent`. |

### Notes

- Send `page` starting at 1 and increase it by 1 while keeping `keyword`, `sort`, `noteType` and `noteTime` the same.
- The `noteTime` filter can return notes published outside the chosen range, so check the `publish_time` tag in each item.
- The note ID is the 24-character hex string inside `mix_track_id`, between `NOTE__` and the next `__`. Pass it to [Xiaohongshu Note Details](/apis/xiaohongshu/note-detail) or [Xiaohongshu Note Comments](/apis/xiaohongshu/note-comment).
- For a similar search with a different response layout, see [Xiaohongshu (RED) Note Search](/apis/xiaohongshu/app-v2/search-notes).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/search-note.json`](../../../catalog/models/xiaohongshu/search-note.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/search-note
