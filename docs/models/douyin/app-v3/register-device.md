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

Registers a new virtual Android device for the Douyin app and returns its identifiers, cookies, and device profile. The only input is an optional `proxy` string, so you can call it with an empty body.

### Use cases

- Get a fresh `device_id` and `install_id` to use as device identity in other Douyin app requests.
- Reuse the returned `cookies_str` and `ua` values when you build your own Douyin app request headers.
- Read the device model, OS version, and app version fields to check which client profile a registration produced.
- Send the registration call through your own HTTP proxy by setting `proxy`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/register-device" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `proxy` | string | No | Proxy, with http:// or https://, only supports http proxies. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BootTime": 1793690965,
  "MbTime": 1793490965,
  "cdid": "a69bd3a0-98be-4018-9383-7dda0e1f8756",
  "channel": "xiaomi_64_1775",
  "cookies": {
    "d_ticket": "8d9975f2ccb6f29206a89352df737eec",
    "install_id": "903174056578794",
    "multi_sids": "112279642953059:48214153003562833010815191492641",
    "odin_tt": "272ff86df62fd1cd7d9ce430623df2abd52e948f630430c6f4070361861114a1353e8fe78055d2c5…",
    "passport_csrf_token": "9c3a245c…",
    "passport_csrf_token_default": "9c3a245c…",
    "store-region": "cn-js",
    "store-region-src": "did",
    "ttreq": "1$716928618b7ac1feef97b977801bcb2de5bd1df3"
  },
  "cookies_str": "install_…",
  "device_brand": "samsung",
  "device_id": "903174057197274",
  "device_manufacturer": "samsung",
  "device_model": "平 的 A52",
  "device_platform": "android",
  "device_type": "SM-A5260"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `device_id / iid / cdid / openudid / uuid` | Identifiers for the registered device. `iid` has the same value as `install_id` in the cookies, and `cdid` is a UUID-style string. |
| `cookies` | Object of cookie values set during registration, such as `install_id`, `d_ticket`, `odin_tt`, `passport_csrf_token`, and `store-region`. |
| `cookies_str` | The cookies joined into a single cookie-header style string, shown as `name=value` pairs separated by semicolons. |
| `ua` | User-agent string for the registered Android device and the Douyin app build. |
| `device_brand / device_manufacturer / device_model / device_type` | Hardware details of the device, such as brand, manufacturer, display model, and model code. |
| `os_version / os_api / device_platform / host_abi` | Operating system details of the device: the OS version, its API level, the platform name, and the CPU architecture. |
| `resolution / dpi` | Screen size as a `WIDTHxHEIGHT` string and the screen density value. |
| `version_name / version_code / update_version_code / manifest_version_code` | Douyin app version values attached to the registered device. |
| `server_time / first_launch_timestamp / BootTime / MbTime` | Time values returned with the device. `server_time` looks like Unix seconds, and `first_launch_timestamp` looks like Unix milliseconds. |
| `x_tt_dt / mc / rom / rom_version / channel` | Extra device values returned by the registration: a token string, a MAC-style address, ROM build details, and the install channel name. |

### Notes

- `proxy` is optional. Include `http://` or `https://` in the value. Only HTTP proxies work.
- Send an empty JSON object `{}` to register a device with no proxy.
- `mssdk_token` and `lanusk` come back as empty strings in this response.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/register-device.json`](../../../../catalog/models/douyin/app-v3/register-device.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/register-device
