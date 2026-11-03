# Douyin Xingtu Audience Touchpoint Distribution API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-touch-distribution` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) audience-touchpoint distribution data for a specified creator and content channel. Use it to compare audience-contact patterns during campaign research.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-touch-distribution", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-touch-distribution', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-touch-distribution", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-touch-distribution", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-touch-distribution` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

This API returns a nested breakdown of content categories that reach a Douyin Xingtu creator's audience, grouped by source type and split into three category levels. It needs the creator's `oAuthorId` and optionally a content channel in `platform`.

### Use cases

- Compare which content categories reach the audience of two creators before you pick one for a campaign.
- Check how much of a creator's reach comes from Xingtu orders versus personal posts.
- Find the sub-categories, such as music or cars, that drive the most contacts for a creator.
- Build a category chart for a creator report from the three category levels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-touch-distribution" \
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
  "video_touch": [
    {
      "distribution_data": {
        "cnt": -1799409204,
        "id": "0",
        "name": "个人"
      },
      "second_distribution": [
        {
          "distribution_data": {
            "cnt": 276457,
            "id": "0",
            "name": "随拍"
          },
          "three_distribution": [
            {
              "distribution_data": {
                "cnt": 276457,
                "id": "0",
                "name": "生活随拍"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `video_touch[]` | Top-level groups of the creator's touchpoint data. The sample shows two groups, named `个人` (personal) and `星图` (Xingtu). |
| `video_touch[].distribution_data.name` | Name of the top-level group. |
| `video_touch[].distribution_data.cnt` | Count for the top-level group. The sample shows a negative value for `个人`, so check for odd values before you use it. |
| `video_touch[].second_distribution[].distribution_data.name / video_touch[].second_distribution[].distribution_data.cnt` | Name and count for each second-level category in the group, such as `音乐` (music) or `汽车` (cars). |
| `video_touch[].second_distribution[].three_distribution[].distribution_data.name / video_touch[].second_distribution[].three_distribution[].distribution_data.cnt` | Name and count for each third-level sub-category under a second-level category, such as `音乐演唱` under `音乐`. |
| `video_touch[].second_distribution[].distribution_data.id / video_touch[].second_distribution[].three_distribution[].distribution_data.id` | Identifier of the category node. The sample returns the string `"0"` for every node. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message means the request succeeded. |

### Notes

- Get `oAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square) or from [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info).
- `platform` accepts `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT` and `SHORT_DRAMA`. The default is `SHORT_VIDEO`, and the sample response uses the `video_touch` key.
- Category names are returned in Chinese. The `cnt` values are plain numbers, and the response does not state their unit.
- For the creator's audience profile, call [Douyin Xingtu Audience Distribution](/apis/douyin/xingtu-v3/data-sp-author-audience-distribution).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-touch-distribution.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-touch-distribution.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-touch-distribution
