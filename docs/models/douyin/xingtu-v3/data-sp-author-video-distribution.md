# Douyin Xingtu Video Distribution API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-video-distribution` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) video-distribution data for a specified creator and content channel. Use it to analyze how the creator's videos are distributed during campaign research.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-video-distribution", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-video-distribution', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-video-distribution", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-video-distribution", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-video-distribution` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns a breakdown of a Douyin Xingtu creator's videos by content category. Each row gives a category name, a video count, and the share of the creator's videos in that category. It needs the creator's `oAuthorId` and optionally a content channel in `platform`.

### Use cases

- Check whether a creator's videos focus on one topic, such as current affairs, before you pitch a brand campaign.
- Compare the content mix of several candidate creators to find the best fit for a product category.
- Spot creators who cover a secondary category like variety shows or TV dramas that matches a campaign theme.
- Add a content category breakdown to a creator report or internal dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-video-distribution" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `platform` | string | No | Platform type. |

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
      "cnt": 354,
      "id": "0",
      "name": "社会时政",
      "proportion": 0.8571
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `video_content_distribution` | List of content categories for the creator's videos. Each item is one category. |
| `video_content_distribution[].name` | Category name, in Chinese. Examples in the response are `社会时政`, `综艺` and `电视剧`. |
| `video_content_distribution[].cnt` | Number of videos counted in this category. |
| `video_content_distribution[].proportion` | Share of the creator's videos in this category, as a decimal. A value of `0.8571` means about 85.7%. |
| `video_content_distribution[].id` | Category ID. The sample response returns `0` for every item, so use `name` to tell categories apart. |
| `base_resp.status_code / base_resp.status_message` | Request status. `0` with an empty message means the call succeeded. |

### Notes

- `oAuthorId` is the creator's unique Xingtu ID, a numeric string such as `6870161898013196295`.
- `platform` accepts `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT` or `SHORT_DRAMA`. The default is `SHORT_VIDEO`.
- To find a creator's ID first, call [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- For the creator's audience instead of content mix, call [Douyin Xingtu Audience Distribution](/apis/douyin/xingtu-v3/data-sp-author-audience-distribution).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-video-distribution.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-video-distribution.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-video-distribution
