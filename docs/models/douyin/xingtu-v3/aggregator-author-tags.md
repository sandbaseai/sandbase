# Douyin Xingtu Creator Tags API: pricing, parameters and code examples

`douyin/xingtu-v3/aggregator-author-tags` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) tags for a specified creator. Use it to classify creators and compare their fit for campaign briefs.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-tags", "starAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-tags', {'starAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-tags", {
  "starAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-tags", sandbase.Params{
	"starAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `starAuthorId` | string | yes | Creator's unique Xingtu ID.  |

## Details

This API returns the tag data Douyin Creator Marketplace (Xingtu) holds for one creator. It needs the creator's Xingtu ID in `starAuthorId`. In the sample response, the tag detail holds only an `is_curated` flag.

### Use cases

- Check the `is_curated` flag for a creator before adding them to a campaign shortlist.
- Filter a list of Xingtu creator IDs by their curated status.
- Confirm that a call succeeded by reading the status code before you pass the creator to other Xingtu lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"starAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `starAuthorId` | string | Yes | Creator's unique Xingtu ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "author_tags_detail": {
    "is_curated": "0"
  },
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `author_tags_detail` | Object that holds the tag data for the creator. |
| `author_tags_detail.is_curated` | Curated flag for the creator. The sample value is the string `0`. The response does not explain what each value means, so treat it as a raw flag. |
| `base_resp.status_code` | Status code of the request. `0` appears in the sample response for a successful call. |
| `base_resp.status_message` | Status text for the request. It is an empty string in the sample response. |

### Notes

- Get `starAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square). The ID is a numeric string, for example `6870161898013196295`.
- Send the ID as a string in the JSON body, not as a number.
- For profile details of the same creator, call [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-tags.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-tags.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-tags
