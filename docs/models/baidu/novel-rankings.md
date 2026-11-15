# Baidu Novel Rankings API: pricing, parameters and code examples

`baidu/novel-rankings` · data API · Baidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetch the hot novel rankings from the Baidu Top board. Returns all novels currently ranked with their scores, along with available genre filter tags that can be used with get_novel_rankings_by_genre or get_board_by_tab.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "baidu/novel-rankings"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('baidu/novel-rankings', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("baidu/novel-rankings", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "baidu/novel-rankings", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/baidu/novel-rankings` with the body above minus `model`.

## Details

Fetch the hot novel rankings from the Baidu Top board. Returns all novels currently ranked with their scores, along with available genre filter tags that can be used with get_novel_rankings_by_genre or get_board_by_tab.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "baidu/novel-rankings"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/baidu/novel-rankings.json`](../../../catalog/models/baidu/novel-rankings.json) · Store page: https://www.sandbase.ai/model/baidu/novel-rankings
