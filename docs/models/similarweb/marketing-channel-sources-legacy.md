# Similarweb Marketing Channel Sources

`similarweb/marketing-channel-sources-legacy` · api · Similarweb

Get a website's visits by marketing channel (direct, search, social, referrals, mail, display) month by month.

## Pricing

- Depends on parameters (`params.end_date`, `params.start_date`).

Formula: `0.525 * Math.max(1.0, (params.start_date != nil && params.end_date != nil ? ((int(split(params.end_date, "-")[0]) - int(split(params.start_date, "-")[0])) * 12 + int(split(params.end_date, "-")[1]) - int(split(params.start_date, "-")[1]) + 1) * 1.0 : 12.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/marketing-channel-sources-legacy", "domain": "cnn.com", "end_date": "2026-09", "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/marketing-channel-sources-legacy', {'domain': 'cnn.com', 'end_date': '2026-09', 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/marketing-channel-sources-legacy", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/marketing-channel-sources-legacy", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/marketing-channel-sources-legacy` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | domain  |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `desktop`, `mobile_web`, `total` |
| `granularity` | string |  | granularity one of: `monthly`; default `"monthly"` |
| `main_domain_only` | boolean |  | main_domain_only default `true` |

## Details

Get a website's visits by marketing channel (direct, search, social, referrals, mail, display) month by month.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/marketing-channel-sources-legacy" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "granularity": "monthly"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | end_date |
| `granularity` | string | No | granularity |
| `main_domain_only` | boolean | No | main_domain_only |
| `start_date` | string | Yes | start_date |
| `web_source` | string | No | web_source |

### Pricing

$0.525 per month between start_date and end_date (12 months if omitted). Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/marketing-channel-sources-legacy.json`](../../../catalog/models/similarweb/marketing-channel-sources-legacy.json) · Store page: https://www.sandbase.ai/model/similarweb/marketing-channel-sources-legacy
