# Douyin Xingtu Creator Side Base Info API: pricing, parameters and code examples

`douyin/xingtu-v3/aggregator-author-side-base-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get the Douyin Creator Marketplace (Xingtu) side-card baseline information for a specified creator. Use it to review a creator's marketplace overview during shortlisting.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-side-base-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-side-base-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-side-base-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-side-base-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-side-base-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns a short baseline summary for one creator in the Douyin Creator Marketplace (Xingtu). The request needs the creator's ID in `oAuthorId`. The response in this example holds a 30-day follower growth rate and a status block.

### Use cases

- Compare the 30-day follower growth of several shortlisted creators before you request deeper reports.
- Flag creators whose follower base has stalled or shrunk recently.
- Add a quick growth figure to a creator screening sheet.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-side-base-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "fans_growth_rate_30d": "0.004290767299658834"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `fans_growth_rate_30d` | Follower growth rate for the creator over the last 30 days. It arrives as a decimal string, for example `0.00429...`. The key name does not show whether this is a fraction or a percent, so check against a known creator before you display it. |
| `base_resp.status_code` | Result code of the call. `0` in the sample response. |
| `base_resp.status_message` | Text message that goes with the status code. It is an empty string in the sample response. |

### Notes

- Pass the creator's Xingtu author ID as `oAuthorId`, a numeric string such as `6870161898013196295`.
- Parse `fans_growth_rate_30d` as a number, since the API returns it as a string.
- For the daily follower trend behind this figure, call [Douyin Xingtu Follower Growth Trend](/apis/douyin/xingtu-v3/data-sp-author-daily-fans).
- For the creator's profile details, call [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-side-base-info.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-side-base-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-side-base-info
