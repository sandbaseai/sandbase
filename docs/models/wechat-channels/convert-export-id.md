# WeChat Channels Export Id Conversion API: pricing, parameters and code examples

`wechat-channels/convert-export-id` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Convert an encrypted WeChat Channels export ID from search results into a usable video object identity. Use it to prepare the identifier required by video lookup endpoints.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/convert-export-id", "exportId": "export/UzFfAgtgekIEAQAAAAAA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/convert-export-id', {'exportId': 'export/UzFfAgtgekIEAQAAAAAA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/convert-export-id", {
  "exportId": "export/UzFfAgtgekIEAQAAAAAA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/convert-export-id", sandbase.Params{
	"exportId": "export/UzFfAgtgekIEAQAAAAAA",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/convert-export-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `exportId` | string | yes | Encrypted WeChat Channels exportId returned by video search results.  |

## Details

Convert an encrypted WeChat Channels export ID from search results into a usable video object identity. Use it to prepare the identifier required by video lookup endpoints.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/convert-export-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"exportId": "export/UzFfAgtgekIEAQAAAAAA"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `exportId` | string | Yes | Encrypted WeChat Channels exportId returned by video search results. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/convert-export-id.json`](../../../catalog/models/wechat-channels/convert-export-id.json) · Store page: https://www.sandbase.ai/model/wechat-channels/convert-export-id
