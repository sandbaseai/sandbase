# Douyin Author Video Distribution API: pricing, parameters and code examples

`douyin/xingtu-v2/author-video-distribution` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call · **Modes:** sync

Get Author Video Distribution on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.002 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-video-distribution", "o_author_id": "7112600044674482187"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-video-distribution', {'o_author_id': '7112600044674482187'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-video-distribution", {
  "o_author_id": "7112600044674482187"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-video-distribution", sandbase.Params{
	"o_author_id": "7112600044674482187",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-video-distribution` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, 1 for Douyin default `1` |
| `platform_channel` | integer |  | Platform channel, 1 for short video default `1` |

## Details

This API returns the content category breakdown of one Douyin creator's short videos, as listed on Xingtu. It needs the creator ID in `o_author_id`. Each row shows a category name, a video count, and that category's share of the total.

### Use cases

- Check whether a creator's videos match the category of your product before you plan a campaign.
- Compare the main content categories of several creators to build a shortlist for a brand.
- Spot creators whose output is spread across many categories versus those who focus on one.
- Add a category mix column to an internal creator database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-video-distribution" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7112600044674482187", "platform_source": 1, "platform_channel": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `platform_channel` | integer | No | Platform channel, 1 for short video |
| `platform_source` | integer | No | Platform source, 1 for Douyin |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "video_content_distribution": [
    {
      "cnt": 4,
      "id": "0",
      "name": "生活家居",
      "proportion": 0.6667
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `video_content_distribution[]` | One entry per content category found in the creator's videos. The list is sorted from the largest share to the smallest in the sample. |
| `video_content_distribution[].name` | Category name in Chinese, for example `生活家居` (home and living) or `时尚` (fashion). |
| `video_content_distribution[].cnt` | Number of the creator's videos counted in this category. |
| `video_content_distribution[].proportion` | Share of the counted videos that fall in this category, as a decimal. For example `0.6667` means about two thirds. |
| `video_content_distribution[].id` | Category ID. It is `"0"` for every row in this response, so use `name` to tell categories apart. |
| `base_resp.status_code / base_resp.status_message` | Status of the request. `0` with an empty message means it succeeded. |

### Notes

- The `proportion` values add up to about `1`, and the `cnt` values add up to the number of videos counted.
- Keep `platform_source` at `1` for Douyin and `platform_channel` at `1` for short video.
- If you only have a Douyin ID or UID, call [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id) or [Douyin Xingtu Author ID by UID](/apis/douyin/xingtu-v2/xingtu-kolid-by-uid) first to get the creator ID.
- For creator profile details, call [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info).

### Pricing

$0.002 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-video-distribution.json`](../../../../catalog/models/douyin/xingtu-v2/author-video-distribution.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-video-distribution
