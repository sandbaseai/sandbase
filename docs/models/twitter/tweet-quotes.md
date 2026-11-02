# X (Twitter) Tweet Quotes API: pricing, parameters and code examples

`twitter/tweet-quotes` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.003 per call · **Modes:** sync

Quote tweets of a post by tweet ID, newest first, with optional time range and cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.003**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/tweet-quotes", "tweetId": "1585341984679469056"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/tweet-quotes', {'tweetId': '1585341984679469056'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/tweet-quotes", {
  "tweetId": "1585341984679469056"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/tweet-quotes", sandbase.Params{
	"tweetId": "1585341984679469056",
})
```

Same call via the path form: `POST /v1/api/twitter/tweet-quotes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor for pagination.  |
| `tweetId` | string | yes | The tweet ID to get quotes for.  |
| `sinceTime` | integer |  | On or after a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. range 0–9223372036854776000 |
| `untilTime` | integer |  | Before a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. range 0–9223372036854776000 |
| `includeReplies` | boolean |  | Whether to include replies in the results. Default is True. Provider reference (supplier schema): `{"default":true,"type":"boolean"}`.  |

## Details

Quote tweets of a post by tweet ID, newest first, with optional time range and cursor pagination.

The result is returned in `outputs[0].data` as the official X (Twitter) API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/tweet-quotes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweetId": "1585341984679469056"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Cursor for pagination. |
| `includeReplies` | boolean | No | Whether to include replies in the results. Default is True. Provider reference (supplier schema): `{"default":true,"type":"boolean"}`. |
| `sinceTime` | integer | No | On or after a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. |
| `tweetId` | string | No | The tweet ID to get quotes for. |
| `untilTime` | integer | No | Before a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. |

### Pricing

Billed at the actual cost of each call, about $0.003 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/tweet-quotes.json`](../../../catalog/models/twitter/tweet-quotes.json) · Store page: https://www.sandbase.ai/model/twitter/tweet-quotes
