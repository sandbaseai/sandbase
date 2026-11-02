# TikTok Creator Account Violations API: pricing, parameters and code examples

`tiktok/creator/account-violation-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the violation history and enforcement actions for a TikTok Shop creator account. Supports chronological pagination across historical violation records.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/account-violation-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/account-violation-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/account-violation-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/account-violation-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/creator/account-violation-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Integer, page number (default is `1`)  |
| `proxy` |  |  | Optional HTTP proxy address, can be omitted if not needed  |

## Details

Look up past compliance violations and enforcement records for a TikTok Shop creator account using `page` for pagination.

### Use cases

- Monitor creator account health and track policy compliance.
- Review past enforcement actions across historical records.
- Audit account risk factors across multiple paginated entries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/account-violation-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Integer, page number (default is `1`) |
| `proxy` | string | No | Optional HTTP proxy address, can be omitted if not needed |

### Notes

- Supports pagination via the `page` parameter, which defaults to `1`.
- Accepts an optional HTTP proxy address via `proxy`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Creator Account Health Status](/model/tiktok/creator/account-health-status): Returns the health status of a TikTok Shop creator account.
- [TikTok Creator Account Insights Overview](/model/tiktok/creator/account-insights-overview): Retrieves performance metrics for a TikTok Shop creator account, including revenue, exposure, clicks, and orders for the specified month.
- [TikTok Creator Account Info](/model/tiktok/creator/creator-account-info): Returns basic profile details for a TikTok Shop creator account, including username, avatar URLs, account ID, region, partner bindings, and permissions.

---
Machine-readable: [`catalog/models/tiktok/creator/account-violation-list.json`](../../../../catalog/models/tiktok/creator/account-violation-list.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/account-violation-list
