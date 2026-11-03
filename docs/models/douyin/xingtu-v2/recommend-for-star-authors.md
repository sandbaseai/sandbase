# Douyin Xingtu Similar Star Authors API: pricing, parameters and code examples

`douyin/xingtu-v2/recommend-for-star-authors` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended similar Douyin Xingtu creators based on a specified list of author IDs and an optional similarity type.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/recommend-for-star-authors", "author_ids": ["1"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/recommend-for-star-authors', {'author_ids': ['1']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/recommend-for-star-authors", {
  "author_ids": [
    "1"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/recommend-for-star-authors", sandbase.Params{
	"author_ids": []any{"1"},
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/recommend-for-star-authors` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default 1  |
| `author_ids` | array | yes | List of creator/author IDs  |
| `similar_type` | string |  | Similarity type  |

## Details

Returns a list of Douyin Xingtu creators that are similar to the creators you pass in. The input is a list of Xingtu author IDs in `author_ids`. You can add `page` and `similar_type` to control the result.

### Use cases

- Build a shortlist of alternative creators for a campaign when your first-choice creator is unavailable.
- Expand a creator pool by feeding in the IDs of creators that already performed well.
- Compare the link indices of recommended creators to pick candidates in a similar range.
- Collect the city and avatar of each recommended creator to fill a creator review sheet.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/recommend-for-star-authors" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_ids": ["7112600044674482187"]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `author_ids` | array | Yes | List of creator/author IDs |
| `page` | integer | No | Page number, default 1 |
| `similar_type` | string | No | Similarity type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "authors": [
    {
      "attribute_datas": {
        "article_interate_rate": "",
        "auth_type": "",
        "author_avatar_frame_icon": "0",
        "author_status": "1",
        "avatar_uri": "\"https://p11.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_cd706156…",
        "avg_play": "",
        "city": "\"海淀区\"",
        "core_user_id": "\"111549895929\""
      },
      "common_datas": {
        "author_list_sources": [],
        "author_list_status": 0,
        "author_list_tags": [],
        "coverage": 0,
        "industry_link_infos": {
          "0": {
            "link_convert_cnt": "0",
            "link_convert_index": 47.39,
            "link_shopping_cnt": "43837",
            "link_shopping_index": 47.64,
            "link_spread_cnt": "1142446",
            "link_spread_index": 54.52,
            "link_star_cnt": "1142446",
            "link_star_index": 58.57
          }
        },
        "is_collected": false,
        "is_star": true,
        "items": []
      },
      "star_id": "6864453571602055181"
    }
  ],
  "base_resp": {
    "status_code": 0,
    "status_message": "success"
  },
  "pagination": {
    "has_more": false,
    "limit": 12,
    "page": 1,
    "total_count": 12
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `authors[].star_id` | Xingtu ID of the recommended creator. Use it as the author ID in other Xingtu APIs. |
| `authors[].attribute_datas.city` | City of the creator. The value arrives wrapped in extra quote characters. |
| `authors[].attribute_datas.avatar_uri` | Avatar image URL of the creator. The value arrives wrapped in extra quote characters. |
| `authors[].attribute_datas.core_user_id` | Core user ID of the creator, as a quoted string. |
| `authors[].attribute_datas.author_status` | Status code of the creator account. The sample shows `1` for all items. |
| `authors[].common_datas.is_star` | Whether the creator is flagged as a star author. |
| `authors[].common_datas.is_collected` | Whether the creator is marked as collected. The sample shows `false` for all items. |
| `authors[].common_datas.industry_link_infos.0.link_star_index / link_spread_index / link_shopping_index / link_convert_index` | Index scores for the creator under the star, spread, shopping and convert links. Higher numbers mean a higher score. |
| `authors[].common_datas.industry_link_infos.0.link_star_cnt / link_spread_cnt / link_shopping_cnt / link_convert_cnt` | Counts that go with each link index, returned as strings. |
| `pagination.has_more / page / limit / total_count` | Paging state. The sample returns `page` 1, `limit` 12 and `total_count` 12, with `has_more` set to `false`. |

### Notes

- Pass the Xingtu author ID, not the Douyin ID, in `author_ids`. Use [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id) to look it up.
- Increase `page` to get more results while `pagination.has_more` is `true`.
- Pass a `star_id` from the result to [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info) for the full creator profile.
- Many fields in `attribute_datas`, such as `avg_play` and `auth_type`, can come back as empty strings.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/recommend-for-star-authors.json`](../../../../catalog/models/douyin/xingtu-v2/recommend-for-star-authors.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/recommend-for-star-authors
