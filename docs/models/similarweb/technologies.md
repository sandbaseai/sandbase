# Similarweb Website Technologies API: pricing, parameters and code examples

`similarweb/technologies` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.75 per call · **Modes:** sync

Get the technologies a website uses (analytics, advertising, CMS and more), with category and first-seen date.

## Pricing

- **$0.75 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/technologies", "domain": "cnn.com", "end_date": "2026-09", "granularity": "monthly", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/technologies', {'domain': 'cnn.com', 'end_date': '2026-09', 'granularity': 'monthly', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/technologies", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "granularity": "monthly",
  "limit": 1,
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/technologies", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"granularity": "monthly",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/technologies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `domain` | string | yes | domain  |
| `format` | string |  | format one of: `json` |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `total` |
| `granularity` | string | yes | granularity one of: `monthly` |
| `main_domain_only` | boolean |  | main_domain_only  |

## Details

Get the technologies a website uses (analytics, advertising, CMS and more), with category and first-seen date.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/technologies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "granularity": "monthly", "limit": 1}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | end_date |
| `format` | string | No | format |
| `granularity` | string | Yes | granularity |
| `limit` | integer | Yes | limit |
| `main_domain_only` | boolean | No | main_domain_only |
| `start_date` | string | Yes | start_date |
| `web_source` | string | No | web_source |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/technologies.json`](../../../catalog/models/similarweb/technologies.json) · Store page: https://www.sandbase.ai/model/similarweb/technologies
