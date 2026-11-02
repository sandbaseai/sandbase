# Douyin App Device Registration API: pricing, parameters and code examples

`douyin/app-v3/register-device` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Registers a device in the Douyin app and returns device parameters such as device ID and version metadata, with an optional HTTP proxy setting.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/register-device"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/register-device', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/register-device", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/register-device", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/register-device` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `proxy` | string |  | Proxy, with http:// or https://, only supports http proxies.  |

## Details

This endpoint registers a device on Douyin and returns device profile details. You can optionally route the request through `proxy`.

### Use cases

- Generate valid Douyin device identifiers for downstream requests.
- Obtain device hardware and version details for automated testing.
- Route device registration calls via a custom HTTP proxy.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/register-device" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `proxy` | string | No | Proxy, with http:// or https://, only supports http proxies. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "BootTime": 1791290193,
  "MbTime": 1791090193,
  "device_id": "516136130850216",
  "device_type": "EVR-AL00",
  "first_launch_timestamp": 1791280340878,
  "server_time": 1791290341,
  "update_version_code": 28309900,
  "version_name": "28.3.0"
}
```

### Notes

- The `proxy` parameter accepts http:// or https:// formats but only supports HTTP proxies.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/register-device.json`](../../../../catalog/models/douyin/app-v3/register-device.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/register-device
