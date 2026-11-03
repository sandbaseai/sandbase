# Douyin Xingtu Author Location Info API: pricing, parameters and code examples

`douyin/xingtu-v2/author-local-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns location details for a Douyin Xingtu creator using their author ID, with optional filters for time range and platform settings.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-local-info", "o_author_id": "7146074596666507300"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-local-info', {'o_author_id': '7146074596666507300'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-local-info", {
  "o_author_id": "7146074596666507300"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-local-info", sandbase.Params{
	"o_author_id": "7146074596666507300",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-local-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `time_range` | integer |  | Time range in days, default 30  |
| `o_author_id` | string | yes | Creator/author ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Returns location details for a Douyin Xingtu creator, including the city and province where the creator lives and whether the creator counts as a local author. It needs the creator's Xingtu author ID in `o_author_id`.

### Use cases

- Check which city and province a creator is based in before you plan a regional campaign.
- Filter a shortlist of creators to those flagged as local authors for a city-targeted promotion.
- Compare the `credit_score` of several creators before you book them.
- Add resident city and province columns to an internal creator database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-local-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7146074596666507300"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator/author ID |
| `platform_channel` | integer | No | Platform channel, default 1 |
| `platform_source` | integer | No | Platform source, default 1 |
| `time_range` | integer | No | Time range in days, default 30 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "city_resident": "深圳",
  "content_level": "0",
  "credit_score": "100",
  "is_local_author": "1",
  "province_resident": "广东",
  "settled_level": "0"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `city_resident` | City where the creator lives. The sample value is `深圳` (Shenzhen). |
| `province_resident` | Province where the creator lives. The sample value is `广东` (Guangdong). |
| `is_local_author` | Flag for whether the creator is a local author. The sample value `1` suggests yes, but the response does not define the flag. |
| `credit_score` | Creator credit score returned as a string. The sample value is `100`. |
| `content_level / settled_level` | Level values for the creator's content and settlement status. Both are `0` in the sample, and the response does not explain the scale. |
| `base_resp.status_code` | Status code of the call. `0` means the request succeeded. |
| `base_resp.status_message` | Status text for the call. It is an empty string in the sample. |

### Notes

- All values in the sample response are strings, including `credit_score` and `is_local_author`. Convert them yourself if you need numbers.
- Only `o_author_id` is required. `time_range`, `platform_source` and `platform_channel` are optional.
- To get the profile of the same creator, call [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info) with the same `o_author_id`.
- If you only have a Douyin ID, look up the author ID first with [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-local-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-local-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-local-info
