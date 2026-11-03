# TikTok Web Browser Fingerprint API: pricing, parameters and code examples

`tiktok/web/generate-fingerprint` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns browser fingerprint configurations for web requests. Allows tailoring the profile based on an optional browser type parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-fingerprint"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-fingerprint', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-fingerprint", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-fingerprint", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-fingerprint` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `browser_type` | string |  | Browser Type  |

## Details

Returns a browser fingerprint object for TikTok web requests, with navigator, screen, WebGL, window and TikTok-specific `wID` values. It takes one optional input, `browser_type`. The sample call sent no input and the response echoed `browser_type` as `random`.

### Use cases

- Fill in a browser environment profile when you build TikTok web request flows.
- Compare the navigator, screen and WebGL values across several calls to see how the generated profiles differ.
- Pass the `fingerprint` object to your own test client that needs a full set of browser values.
- Pair the fingerprint with other TikTok web token APIs when you prepare a signed web session.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-fingerprint" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `browser_type` | string | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "browser_type": "random",
  "fingerprint": {
    "canvasIntegrity": {
      "a": 1,
      "b": 1,
      "c": 1,
      "d": [
        "3406898329"
      ],
      "e": 1
    },
    "custom": {},
    "customInit": {
      "ttwid": "75142854…"
    },
    "document": {
      "URL": "https://www.tiktok.com/",
      "all": 13,
      "characterSet": "UTF-8",
      "compatMode": "CSS1Compat",
      "documentMode": "undefined",
      "images": 99,
      "layers": 4
    },
    "mediaQuery": {
      "anyPointer": "fine",
      "dpi": 192,
      "dppx": 2,
      "hover": "hover",
      "maxHeight": 1260,
      "maxWidth": 2834,
      "orientation": "landscape"
    },
    "msgMeta": {
      "aid": 368462,
      "aidList": [
        1988
      ],
      "msgProtocol": 1,
      "msgSrcProp": 2,
      "msgType": 1
    },
    "navigator": {
      "appCodeName": "Mozilla",
      "appMinorVersion": "undefined",
      "appName": "Netscape",
      "appVersion": "5.0 (Macintosh)",
      "bluetooth": 4,
      "buildID": "20181001000000",
      "cookieEnabled": 1,
      "cpuClass": "undefined",
      "credentials": 99,
      "deviceMemory": "8",
      "doNotTrack": "1",
      "hardwareConcurrency": 8
    },
    "plugins": {
      "plugin": [],
      "proto": 1,
      "pv": "0"
    },
    "screen": {
      "availHeight": 1771,
      "availWidth": 2880,
      "clientHeight": 1260,
      "clientWidth": 2834,
      "colorDepth": 30,
      "focus": 2,
      "hidden": 2,
      "innerHeight": 1260,
      "innerWidth": 2834,
      "location": 1,
      "menubar": 1,
      "orientation": "landscape-primary"
    },
    "tokenList": [],
    "wID": {
      "aFP": "3453338562",
      "aid": 368462,
      "aidList": [
        1988
      ],
      "bb": {
        "a": -1,
        "b": 268,
        "c": 1
      },
      "browserType": 2,
      "canvas": "3406898329",
      "dProps": 2,
      "dups": 1,
      "env": "1111111111111111111111111",
      "hl": 3,
      "iframe": 2,
      "iframeInfo": {
        "iFrameNP": {
          "hC": 8,
          "lang": "en-US",
          "platform": "MacIntel",
          "uA": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:135.0) Gecko/20100101 Firefox/1…",
          "wd": "false"
        },
        "iFrameSP": {
          "aH": 1771,
          "aW": 2880,
          "h": 1800,
          "pD": 30,
          "w": 2880
        },
        "propHash": "-29572292501"
      }
    },
    "webgl": {
      "antialias": 1,
      "blueBits": 8,
      "depthBits": 24,
      "greenBits": 8,
      "maxAnisotropy": 16,
      "maxCombinedTextureImageUnits": 80,
      "maxCubeMapTextureSize": 8192,
      "maxFragmentUniformVectors": 4096,
      "maxRenderbufferSize": 16384,
      "maxTextureImageUnits": 16,
      "maxTextureSize": 8192,
      "maxVaryingVectors": 32
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `browser_type` | The browser type used for this profile. It was `random` when no input was sent. |
| `fingerprint.navigator.userAgent` | The user agent string of the generated browser. In the sample it is Firefox 135 on macOS. |
| `fingerprint.navigator.platform / fingerprint.navigator.language / fingerprint.navigator.hardwareConcurrency` | The platform, primary language and CPU thread count that the profile reports. |
| `fingerprint.screen.sizeWidth / fingerprint.screen.sizeHeight` | The reported screen size in pixels. Related fields such as `innerWidth`, `outerWidth` and `availWidth` describe the window and available area. |
| `fingerprint.webgl.renderer / fingerprint.webgl.vendor / fingerprint.webgl.version` | The WebGL graphics renderer, vendor and version strings. |
| `fingerprint.webgl.supportedExtensions[]` | The list of WebGL extension names the profile reports. |
| `fingerprint.customInit.ttwid` | A `ttwid` value included in the profile. |
| `fingerprint.wID.tz / fingerprint.wID.timezone` | The time zone name and numeric time zone value in the profile. |
| `fingerprint.wID.sdkVersion / fingerprint.wID.scmVersion` | The SDK and SCM version strings carried in the `wID` block. |
| `fingerprint.wID.timestamp` | A numeric timestamp string that the profile sets for this fingerprint. |

### Notes

- `browser_type` is optional. Calling with an empty body `{}` returns a profile with `browser_type` set to `random`.
- The response nests all values under `fingerprint`. Many fields inside `wID` are short coded values, so use them as returned.
- To get related identifiers, see [TikTok Web TTWID Identifier](/apis/tiktok/web/generate-ttwid) and [TikTok Web ID](/apis/tiktok/web/generate-webid).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-fingerprint.json`](../../../../catalog/models/tiktok/web/generate-fingerprint.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-fingerprint
