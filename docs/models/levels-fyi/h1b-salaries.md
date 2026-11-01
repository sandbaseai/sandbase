# Levels.fyi H1B Salaries

`levels-fyi/h1b-salaries` · api · Levels.fyi

Retrieve paginated H-1B visa salary records for a given year, sorted by date descending. Each record includes company, job title, wage, location (city/state), and certification status.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "levels-fyi/h1b-salaries"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('levels-fyi/h1b-salaries', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("levels-fyi/h1b-salaries", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "levels-fyi/h1b-salaries", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/levels-fyi/h1b-salaries` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination (starts at 1). range -9007199254740991–9007199254740991 |
| `year` | integer |  | Year of H-1B records. Valid values include 2020 through 2025. range -9007199254740991–9007199254740991 |

## Details

Retrieve paginated H-1B visa salary records for a given year, sorted by date descending. Each record includes company, job title, wage, location (city/state), and certification status.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/levels-fyi/h1b-salaries" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number for pagination (starts at 1). |
| `year` | integer | No | Year of H-1B records. Valid values include 2020 through 2025. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/levels-fyi/h1b-salaries.json`](../../../catalog/models/levels-fyi/h1b-salaries.json) · Store page: https://www.sandbase.ai/model/levels-fyi/h1b-salaries
