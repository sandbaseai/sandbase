# Waveinflu Email Lookup

`waveinflu/email-lookup` · api · Waveinflu

Looks up the contact email for one Instagram, TikTok, or YouTube creator from a profile URL.

## Pricing

- **$0.001991 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "waveinflu/email-lookup"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('waveinflu/email-lookup', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("waveinflu/email-lookup", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "waveinflu/email-lookup", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/waveinflu/email-lookup` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `profile_url` | string |  | Instagram, TikTok, or YouTube creator profile URL.  |

## Details

Looks up the contact email for one Instagram, TikTok, or YouTube creator from a profile URL.

The response is the official Waveinflu API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/waveinflu/email-lookup" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"profile_url": "https://www.instagram.com/nike/"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `profile_url` | string | No | Instagram, TikTok, or YouTube creator profile URL. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/waveinflu/email-lookup.json`](../../../catalog/models/waveinflu/email-lookup.json) · Store page: https://www.sandbase.ai/model/waveinflu/email-lookup
