# Baidu Realtime Hot Search API: pricing, parameters and code examples

`baidu/realtime-hot-search` · data API · Baidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetch the real-time hot search rankings from the Baidu Top board. Returns the current top trending search terms with scores and metadata. Items are ordered by descending hot_score. No filtering is available; the full ranked list is returned in a single page.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "baidu/realtime-hot-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('baidu/realtime-hot-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("baidu/realtime-hot-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "baidu/realtime-hot-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/baidu/realtime-hot-search` with the body above minus `model`.

## Details

Fetch the real-time hot search rankings from the Baidu Top board. Returns the current top trending search terms with scores and metadata. Items are ordered by descending hot_score. No filtering is available; the full ranked list is returned in a single page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "baidu/realtime-hot-search"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/baidu/realtime-hot-search.json`](../../../catalog/models/baidu/realtime-hot-search.json) · Store page: https://www.sandbase.ai/model/baidu/realtime-hot-search
