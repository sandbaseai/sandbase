# Douyin Xingtu KOL Search (V2)

`douyin/xingtu/search-kol-v2` · api · Douyin

Searches Douyin Xingtu creators by keyword, content tags, and follower count ranges. Returns creator identifiers, task rate tiers, and qualification levels.

## Pricing

- **$0.03 per call** (USD)

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

Query Douyin Xingtu creator profiles by specifying a `keyword` alongside optional content tags and follower thresholds.

### Use cases

- Discover Douyin creators matching specific niche topics or keywords.
- Filter potential influencer partnerships by audience size brackets.
- Evaluate creator task tier assignments and performance levels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/search-kol-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `contentTag` | string | No | Content tag (optional), for example tag-1 or tag_level_two-7. |
| `followerRange` | string | No | Follower range (optional), for example 10-100 means 100,000 to 1,000,000 followers. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "authors": [
    {
      "star_id": "6669294384883695629",
      "attribute_datas": {
        "assign_cpm_suggest_price": "105",
        "assign_task_price_list": "[97500,150000,172000]",
        "author_ecom_level": "L0",
        "author_level_game": "Lv1",
        "author_level_other": "Lv1",
        "author_status": "1"
      }
    }
  ]
}
```

### Notes

- Format `followerRange` as min-max values in tens of thousands, such as 10-100 for 100,000 to 1,000,000 followers.
- Supply `contentTag` values using category identifiers like tag-1 or tag_level_two-7.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/model/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/model/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/model/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/search-kol-v2.json`](../../../../catalog/models/douyin/xingtu/search-kol-v2.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/search-kol-v2
