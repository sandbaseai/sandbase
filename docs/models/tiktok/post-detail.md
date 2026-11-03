# TikTok Post Details API: pricing, parameters and code examples

`tiktok/post-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get details for a TikTok post identified by its post ID. Use it to look up a known TikTok video before content review, reporting, or related engagement analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/post-detail", "postId": "6701927684605233153"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/post-detail', {'postId': '6701927684605233153'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/post-detail", {
  "postId": "6701927684605233153"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/post-detail", sandbase.Params{
	"postId": "6701927684605233153",
})
```

Same call via the path form: `POST /v1/api/tiktok/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `postId` | string | yes | The unique ID of the TikTok post.  |

## Details

Returns the platform's original data structure for a TikTok post, looked up by its post ID. It needs one input, `postId`. The sample response for `6701927684605233153` holds only status and request metadata, with no video fields.

### Use cases

- Check whether a known TikTok post ID returns data before you add it to a content review queue.
- Record the request IDs for a post lookup so you can trace the call later in a report.
- Test a list of saved post IDs and flag the ones whose `extra.fatal_item_ids` list is not empty.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"postId": "6701927684605233153"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `postId` | string | Yes | The unique ID of the TikTok post. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611030744081E2411327AEFB402ED07",
    "now": 1793691849000
  },
  "log_pb": {
    "impr_id": "202611030744081E2411327AEFB402ED07"
  },
  "statusCode": 10204,
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `status_code` | Status code of the lookup. It is `0` in the sample response. |
| `status_msg` | Status message text. It is an empty string in the sample response. |
| `statusCode` | A second status code in camelCase. The sample shows `10204`. The response does not explain this value. |
| `extra.fatal_item_ids` | List of item IDs the platform flagged with a fatal error. It is empty in the sample. |
| `extra.logid` | Identifier for this request on the platform side. It has the same value as `log_pb.impr_id` in the sample. |
| `extra.now` | A 13-digit number that fits a Unix timestamp in milliseconds. It most likely marks the time of the response. |
| `log_pb.impr_id` | Impression ID for this request. Use it together with `extra.logid` when you log or compare calls. |

### Notes

- `postId` is a numeric string, for example `6701927684605233153`.
- The sample response has no video fields such as description, author or counts. If you need full video data, try [TikTok Video Details](/apis/tiktok/app-v3/one-video) or [TikTok Video Details (V3)](/apis/tiktok/app-v3/one-video-v3).
- Check both `status_code` and `statusCode` in your code. The two fields can differ, as they do in the sample (`0` and `10204`).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tiktok/post-detail.json`](../../../catalog/models/tiktok/post-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/post-detail
