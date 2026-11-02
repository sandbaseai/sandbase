# X (Twitter) User Mentions API: pricing, parameters and code examples

`twitter/user-mentions` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.003 per call · **Modes:** sync

Recent tweets that mention a user by username, with optional time range and cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.003**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/user-mentions", "userName": "NASA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/user-mentions', {'userName': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/user-mentions", {
  "userName": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/user-mentions", sandbase.Params{
	"userName": "NASA",
})
```

Same call via the path form: `POST /v1/api/twitter/user-mentions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | The cursor to paginate through the results. First page is empty.  |
| `userName` | string | yes | The user screen name to get mentions for.  |
| `sinceTime` | integer |  | On or after a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. range 0–9223372036854776000 |
| `untilTime` | integer |  | Before a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. range 0–9223372036854776000 |

## Details

Recent tweets that mention a user by username, with optional time range and cursor pagination.

The result is returned in `outputs[0].data` as the official X (Twitter) API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/user-mentions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userName": "NASA"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | The cursor to paginate through the results. First page is empty. |
| `sinceTime` | integer | No | On or after a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. |
| `untilTime` | integer | No | Before a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. |
| `userName` | string | No | The user screen name to get mentions for. |

### Pricing

Billed at the actual cost of each call, about $0.003 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/user-mentions.json`](../../../catalog/models/twitter/user-mentions.json) · Store page: https://www.sandbase.ai/model/twitter/user-mentions
