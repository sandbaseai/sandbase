# Douyin Xingtu Resource List API: pricing, parameters and code examples

`douyin/xingtu-v2/resource-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns marketing activity resources from Douyin Xingtu. Queries resource details using a specific resource identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/resource-list", "resource_id": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/resource-list', {'resource_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/resource-list", {
  "resource_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/resource-list", sandbase.Params{
	"resource_id": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/resource-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `resource_id` | integer | yes | Resource ID  |

## Details

Returns marketing activity resources from Douyin Xingtu for a given `resource_id`. The `data` list holds one JSON string per resource, such as a case study article with a title, link and cover image.

### Use cases

- Pull the case study articles and campaign write-ups that Xingtu lists under a resource group.
- Collect article links from Xingtu marketing activities to review past campaigns.
- Filter resources by industry code to find examples for a specific sector.
- Save cover images and slogans from Xingtu resources for campaign research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/resource-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"resource_id": 1052}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `resource_id` | integer | Yes | Resource ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "data": [
    "{\"title\":\"2024巨量星图CNY「生意星龙」IP圆满收官，助力众多品牌龙年首战告捷！\",\"create_time\":\"1709350920\",\"nam…"
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_resp.status_code` | Request status code. The value `0` in the sample means the call succeeded. |
| `base_resp.status_message` | Status text for the request. It is an empty string in the sample. |
| `data[]` | One resource per list item. Each item is a string that holds a JSON object, so parse it again after reading the response. Keys seen inside the sample strings include `title`, `name`, `link`, `url`, `cover_url`, `image`, `slogan`, `industries`, `create_time` and `id`. |

### Notes

- Each entry in `data` is a JSON string. Decode it to read inner keys such as `title`, `link`, `cover_url` and `industries`.
- Not every item has every inner key. Check that a key exists before you read it.
- `industries` holds comma-separated numeric codes, for example `1930,1903,1933`. `create_time` and `id` arrive as strings.
- For related activity data, see [Douyin Xingtu IP Activity List](/apis/douyin/xingtu-v2/ip-activity-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/resource-list.json`](../../../../catalog/models/douyin/xingtu-v2/resource-list.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/resource-list
