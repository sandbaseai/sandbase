# Baidu Homepage Summary API: pricing, parameters and code examples

`baidu/homepage-summary` · data API · Baidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetch the main home/board overview page summary with cloud trending topics and top items for all categories (realtime, novel, movie, teleplay). Each card contains a preview of that board's top items. The cloud array contains trending keywords with hotScores.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "baidu/homepage-summary"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('baidu/homepage-summary', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("baidu/homepage-summary", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "baidu/homepage-summary", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/baidu/homepage-summary` with the body above minus `model`.

## Details

Fetch the main home/board overview page summary with cloud trending topics and top items for all categories (realtime, novel, movie, teleplay). Each card contains a preview of that board's top items. The cloud array contains trending keywords with hotScores.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "baidu/homepage-summary"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/baidu/homepage-summary.json`](../../../catalog/models/baidu/homepage-summary.json) · Store page: https://www.sandbase.ai/model/baidu/homepage-summary
