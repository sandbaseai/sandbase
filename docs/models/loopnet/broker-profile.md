# LoopNet Broker Profile

`loopnet/broker-profile` · api · LoopNet

Get broker profile and contact information including phone numbers, company name, and professional designations. The profile_url can be a full URL or relative path obtainable from search_brokers results or.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "loopnet/broker-profile", "profile_url": "/commercial-real-estate-brokers/profile/glenn-frankel/jlvz546b"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('loopnet/broker-profile', {'profile_url': '/commercial-real-estate-brokers/profile/glenn-frankel/jlvz546b'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("loopnet/broker-profile", {
  "profile_url": "/commercial-real-estate-brokers/profile/glenn-frankel/jlvz546b"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "loopnet/broker-profile", sandbase.Params{
	"profile_url": "/commercial-real-estate-brokers/profile/glenn-frankel/jlvz546b",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/loopnet/broker-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `profile_url` | string | yes | Full URL or relative path to the broker profile (e.g., '/commercial-real-estate-brokers/profile/glenn-frankel/jlvz546b'). Obtainable from search_brokers results or get_listing_detail broker_links.  |

## Details

Get broker profile and contact information including phone numbers, company name, and professional designations. The profile_url can be a full URL or relative path obtainable from search_brokers results or.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/loopnet/broker-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"profile_url": "/commercial-real-estate-brokers/profile/glenn-frankel/jlvz546b"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `profile_url` | string | Yes | Full URL or relative path to the broker profile (e.g., '/commercial-real-estate-brokers/profile/glenn-frankel/jlvz546b'). Obtainable from search_brokers results or get_listing_detail broker_links. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/loopnet/broker-profile.json`](../../../catalog/models/loopnet/broker-profile.json) · Store page: https://www.sandbase.ai/model/loopnet/broker-profile
