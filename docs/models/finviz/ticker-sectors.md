# Finviz Ticker Sectors and Performance API: pricing, parameters and code examples

`finviz/ticker-sectors` · data API · Finviz · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** async

Get the sector, industry and multi-period performance of a list of US tickers from Finviz.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "finviz/ticker-sectors", "tickers": "AAPL,MSFT"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('finviz/ticker-sectors', {'tickers': 'AAPL,MSFT'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("finviz/ticker-sectors", {
  "tickers": "AAPL,MSFT"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "finviz/ticker-sectors", sandbase.Params{
	"tickers": "AAPL,MSFT",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/finviz/ticker-sectors` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tickers` | string | yes | Comma-separated list of US-listed ticker symbols (1-100). Class-share symbols use dot notation (e.g. BRK.B, PBR.A).  |

## Details

Get the sector, industry and multi-period performance of a list of US tickers from Finviz.

---
Machine-readable: [`catalog/models/finviz/ticker-sectors.json`](../../../catalog/models/finviz/ticker-sectors.json) · Store page: https://www.sandbase.ai/model/finviz/ticker-sectors
