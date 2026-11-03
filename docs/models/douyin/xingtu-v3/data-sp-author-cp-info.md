# Douyin Xingtu Cost Performance Analysis API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-cp-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) cost-performance information for a specified creator and content channel. Use it to compare creator efficiency during campaign budgeting.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-cp-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-cp-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-cp-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-cp-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-cp-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns Xingtu cost-performance estimates for one Douyin creator on one content channel. You pass the creator's `oAuthorId` and, optionally, a `platform` value such as `SHORT_VIDEO`.

### Use cases

- Compare the expected video views of several creators before you set a campaign budget.
- Check expected cost metrics for a creator's short video channel against their live streaming channel.
- Screen a list of creator IDs and drop those with no cost-performance data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-cp-info" \
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
  "expect_cpe": {},
  "expect_cpm": {},
  "expect_vv": {
    "value": 13169552
  },
  "hot_item": {}
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_resp.status_code` | Status code of the call. `0` means the request succeeded. |
| `base_resp.status_message` | Status text. It is an empty string when the call succeeds. |
| `expect_vv.value` | Expected view count (`vv`) for this creator on the chosen channel. The sample value is `13169552`. |
| `expect_cpm` | Expected cost per thousand views (CPM) for the creator. It comes back as an empty object when no value exists for the channel. |
| `expect_cpe` | Expected cost per engagement (CPE) for the creator. It comes back as an empty object when no value exists for the channel. |
| `hot_item` | Hot content item for the creator. It comes back as an empty object when none exists. |

### Notes

- `platform` accepts `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT` and `SHORT_DRAMA`. The default is `SHORT_VIDEO`.
- Some objects, such as `expect_cpm` and `expect_cpe`, can be empty for a creator or channel. Try another `platform` value if you need them.
- Find a creator's `oAuthorId` with [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- For more creator metrics, call [Douyin Xingtu Creator Channel Metrics](/apis/douyin/xingtu-v3/author-author-platform-channel-info-v2) or [Douyin Xingtu Spread Metrics](/apis/douyin/xingtu-v3/data-sp-author-spread-info).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-cp-info.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-cp-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-cp-info
