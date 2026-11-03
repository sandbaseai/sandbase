# Douyin Xingtu KOL Search (V2) API: pricing, parameters and code examples

`douyin/xingtu/search-kol-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Searches Douyin Xingtu creators by keyword, content tags, and follower count ranges. Returns creator identifiers, task rate tiers, and qualification levels.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/search-kol-v2", "keyword": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/search-kol-v2', {'keyword': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/search-kol-v2", {
  "keyword": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/search-kol-v2", sandbase.Params{
	"keyword": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/search-kol-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Keyword  |
| `contentTag` | string |  | Content tag (optional), for example tag-1 or tag_level_two-7.  |
| `followerRange` | string |  | Follower range (optional), for example 10-100 means 100,000 to 1,000,000 followers.  |

## Details

Searches Douyin Xingtu creators by `keyword`, with optional `contentTag` and `followerRange` filters. Returns a page of creators with their `star_id`, recent videos, price settings and task price lists.

### Use cases

- Build a shortlist of Douyin creators who cover a topic such as artificial intelligence.
- Compare task prices across creators before you plan a paid campaign.
- Narrow a creator search to a follower bracket with `followerRange`.
- Collect `star_id` values to feed into other Xingtu creator APIs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/search-kol-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `contentTag` | string | No | Content tag (optional), for example tag-1 or tag_level_two-7. |
| `followerRange` | string | No | Follower range (optional), for example 10-100 means 100,000 to 1,000,000 followers. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "authors": [
    {
      "attribute_datas": {
        "assign_cpm_suggest_price": "105",
        "assign_task_price_list": "[97500,97500,150000,150000,150000,172000]",
        "author_avatar_frame_icon": "20",
        "author_ecom_level": "L0",
        "author_level_game": "Lv1",
        "author_level_other": "Lv1",
        "author_status": "1",
        "author_thin_mid_word_association_index": "{\"年轻人\":0.09050000000000001,\"高电压架构\":0.002}"
      },
      "extra_data": {
        "content_query_from_word": "",
        "content_query_score": 0,
        "debug_info": "",
        "demander_behavior": {
          "added_author_list": false,
          "cooperated": false,
          "viewd_author_page": false
        },
        "recall_from": [
          "1_0"
        ],
        "recall_return_infos": {},
        "recommend_types": []
      },
      "items": [
        {
          "item_id": "7639730469419945279",
          "video_tag": 3,
          "vv": 10219804
        }
      ],
      "star_id": "6669294384883695629",
      "task_infos": [
        {
          "online_status": 1,
          "platform_source": 1,
          "price_infos": [
            {
              "end_time": "2145916800",
              "platform_source": 1,
              "price": 150000,
              "price_extra_info": {},
              "start_time": "1774972800",
              "task_category": 1,
              "video_type": 71,
              "video_type_status": 1
            }
          ],
          "task_category": 1,
          "task_status": 1
        }
      ]
    }
  ],
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "extra_data": {
    "intent_score": 0.14355403184890747,
    "is_cpm_project_search": false,
    "is_intent_consistent": false,
    "search_author_count": 0,
    "search_item_count": 0,
    "search_session_id": "77038448…",
    "speaker_live_base_dis": []
  },
  "pagination": {
    "has_more": true,
    "limit": 20,
    "page": 1,
    "total_count": 100
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `authors[].star_id` | The Xingtu creator ID. Use it as the input for other Xingtu creator APIs. |
| `authors[].attribute_datas.assign_task_price_list` | A JSON string holding a list of task prices for the creator. Parse it before use. |
| `authors[].attribute_datas.assign_cpm_suggest_price` | A suggested CPM price for the creator, returned as a string. |
| `authors[].attribute_datas.author_ecom_level / author_level_game / author_level_other` | Level labels for the creator, such as `L0` or `Lv1`. They cover e-commerce, game and other categories. |
| `authors[].attribute_datas.author_thin_mid_word_association_index` | A JSON string that maps topic words to numeric association scores. It can be empty (`{}`). |
| `authors[].items[].item_id / vv` | The ID of a recent video from the creator, and its `vv` value (view count). |
| `authors[].task_infos[].price_infos[].price` | The price for one video type under this task. The `video_type` field gives the type code. |
| `authors[].task_infos[].price_infos[].start_time / end_time` | Unix timestamps in seconds that mark when the price is valid. |
| `authors[].task_infos[].online_status / task_status` | Status codes for the creator's task. The response does not name what each code value means. |
| `pagination.page / limit / total_count / has_more` | Current page number, page size, total match count and whether more pages exist. |

### Notes

- Set `followerRange` in units of 10,000 followers. For example, `10-100` means 100,000 to 1,000,000 followers.
- Pass `contentTag` as a tag ID such as `tag-1` or `tag_level_two-7`.
- The response reports `pagination.has_more`, `page` and `limit` (20 per page here). The request schema lists no paging parameter.
- Pass a `star_id` to [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1) or [Douyin XingTu KOL Price](/apis/douyin/xingtu/kol-service-price-v1) for more detail on one creator.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/apis/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/search-kol-v2.json`](../../../../catalog/models/douyin/xingtu/search-kol-v2.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/search-kol-v2
