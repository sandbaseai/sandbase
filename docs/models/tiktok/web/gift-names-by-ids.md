# TikTok Gift Names by IDs API: pricing, parameters and code examples

`tiktok/web/gift-names-by-ids` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.025 per call · **Modes:** sync

Returns gift names for a batch of TikTok gift identifiers. Provide a list of gift IDs to look up their corresponding gift labels.

## Pricing

- **$0.025 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/gift-names-by-ids", "gift_ids": ["10001", "10002", "10003"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/gift-names-by-ids', {'gift_ids': ['10001', '10002', '10003']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/gift-names-by-ids", {
  "gift_ids": [
    "10001",
    "10002",
    "10003"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/gift-names-by-ids", sandbase.Params{
	"gift_ids": []any{"10001", "10002", "10003"},
})
```

Same call via the path form: `POST /v1/api/tiktok/web/gift-names-by-ids` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gift_ids` | array | yes | Gift ID list, recommend 50/call for best value ($0.025), auto-process first 50 if more than 50  |

## Details

Returns the gift name for each TikTok gift ID in a list. You send `gift_ids` as an array of strings and get one result row per ID, plus counts for found and missing IDs.

### Use cases

- Turn raw gift IDs in live stream gift event logs into readable gift names.
- Build a local lookup table of TikTok gift IDs and names.
- Check which gift IDs in a stored dataset have no known name.
- Label gift columns in a report on live stream gifting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/gift-names-by-ids" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"gift_ids": ["10001", "10002", "10003"]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `gift_ids` | array | Yes | Gift ID list, recommend 50/call for best value ($0.025), auto-process first 50 if more than 50 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "found": 3,
  "message": null,
  "not_found": 0,
  "original_count": 3,
  "results": [
    {
      "code": 0,
      "gift_id": "10001",
      "gift_name": "鞭炮"
    }
  ],
  "total": 3,
  "truncated": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[].gift_id` | The gift ID from your request that this row answers. |
| `results[].gift_name` | The name of the gift. The sample values are in Chinese, such as `鞭炮` and `红包`. |
| `results[].code` | Result code for this single lookup. It is `0` on every row in the sample, where all IDs returned a name. |
| `found / not_found` | Number of IDs that returned a name and number of IDs that did not. |
| `original_count / total` | Count of IDs in the request and total count of results. Both are `3` in the sample. |
| `truncated` | Boolean flag. It is `false` in the sample. |
| `message` | Text message about the call. It is `null` in the sample. |

### Notes

- Send each ID as a string, for example `"10001"`. The `gift_ids` list accepts 1 to 1000 items.
- If you send more than 50 IDs, only the first 50 are processed.
- Compare `found`, `not_found` and `truncated` with your request to see whether any IDs were unresolved or skipped.
- To look up one ID, use [TikTok Gift Name by ID](/apis/tiktok/web/gift-name-by-id).

### Pricing

$0.025 per successful call. Failed calls are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/gift-names-by-ids.json`](../../../../catalog/models/tiktok/web/gift-names-by-ids.json) · Store page: https://www.sandbase.ai/model/tiktok/web/gift-names-by-ids
