# TikTok Web StrData Encryption

`tiktok/web/encrypt-str-data` · api · TikTok

Encrypts raw fingerprint string data for TikTok web requests. Takes a stringified JSON fingerprint payload via the data parameter and returns the encrypted string.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/encrypt-str-data", "data": "{\"behavior\":{\"beResize\":[],\"beMotion\":[{\"ts\":1701069187299,\"x\":null,\"y\":null,\"z\":null},{\"ts\":1701069202902,\"x\":null,\"y\":null,\"z\":null}],\"bePaste\":[],\"beMouse\":[],\"beKeyboard\":[],\"beScroll\":[],\"beTouch\":[],\"beWheel\":[],\"windowState\":[{\"ts\":1701069186257,\"v\":1},{\"ts\":1701069186257,\"v\":1},{\"ts\":1701069186388,\"v\":2},{\"ts\":1701069186388,\"v\":2},{\"ts\":1701069186402,\"v\":1},{\"ts\":1701069186402,\"v\":1},{\"ts\":1701069200309,\"v\":2},{\"ts\":1701069200309,\"v\":2},{\"ts\":1701069201865,\"v\":1},{\"ts\":1701069201865,\"v\":1}],\"isTrusted\":1},\"wID\":{\"sdkVersion\":\"4.4.6\",\"scmVersion\":\"1.0.0.96\",\"msgType\":2,\"timestamp\":\"1701069221819\",\"aid\":368462,\"aidList\":[1988,368462],\"privacyMode\":516},\"custom\":{},\"window\":{\"location\":\"https://www.tiktok.com/@funnykittensttk/video/7293517029737352454?is_from_webapp=1&web_id=7260049563725497899\"},\"msgMeta\":{\"msgType\":2,\"msgSrcProp\":2,\"msgProtocol\":1,\"aid\":368462,\"aidList\":[1988,368462]}}"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/encrypt-str-data', {'data': '{"behavior":{"beResize":[],"beMotion":[{"ts":1701069187299,"x":null,"y":null,"z":null},{"ts":1701069202902,"x":null,"y":null,"z":null}],"bePaste":[],"beMouse":[],"beKeyboard":[],"beScroll":[],"beTouch":[],"beWheel":[],"windowState":[{"ts":1701069186257,"v":1},{"ts":1701069186257,"v":1},{"ts":1701069186388,"v":2},{"ts":1701069186388,"v":2},{"ts":1701069186402,"v":1},{"ts":1701069186402,"v":1},{"ts":1701069200309,"v":2},{"ts":1701069200309,"v":2},{"ts":1701069201865,"v":1},{"ts":1701069201865,"v":1}],"isTrusted":1},"wID":{"sdkVersion":"4.4.6","scmVersion":"1.0.0.96","msgType":2,"timestamp":"1701069221819","aid":368462,"aidList":[1988,368462],"privacyMode":516},"custom":{},"window":{"location":"https://www.tiktok.com/@funnykittensttk/video/7293517029737352454?is_from_webapp=1&web_id=7260049563725497899"},"msgMeta":{"msgType":2,"msgSrcProp":2,"msgProtocol":1,"aid":368462,"aidList":[1988,368462]}}'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/encrypt-str-data", {
  "data": "{\"behavior\":{\"beResize\":[],\"beMotion\":[{\"ts\":1701069187299,\"x\":null,\"y\":null,\"z\":null},{\"ts\":1701069202902,\"x\":null,\"y\":null,\"z\":null}],\"bePaste\":[],\"beMouse\":[],\"beKeyboard\":[],\"beScroll\":[],\"beTouch\":[],\"beWheel\":[],\"windowState\":[{\"ts\":1701069186257,\"v\":1},{\"ts\":1701069186257,\"v\":1},{\"ts\":1701069186388,\"v\":2},{\"ts\":1701069186388,\"v\":2},{\"ts\":1701069186402,\"v\":1},{\"ts\":1701069186402,\"v\":1},{\"ts\":1701069200309,\"v\":2},{\"ts\":1701069200309,\"v\":2},{\"ts\":1701069201865,\"v\":1},{\"ts\":1701069201865,\"v\":1}],\"isTrusted\":1},\"wID\":{\"sdkVersion\":\"4.4.6\",\"scmVersion\":\"1.0.0.96\",\"msgType\":2,\"timestamp\":\"1701069221819\",\"aid\":368462,\"aidList\":[1988,368462],\"privacyMode\":516},\"custom\":{},\"window\":{\"location\":\"https://www.tiktok.com/@funnykittensttk/video/7293517029737352454?is_from_webapp=1&web_id=7260049563725497899\"},\"msgMeta\":{\"msgType\":2,\"msgSrcProp\":2,\"msgProtocol\":1,\"aid\":368462,\"aidList\":[1988,368462]}}"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/encrypt-str-data", sandbase.Params{
	"data": "{\"behavior\":{\"beResize\":[],\"beMotion\":[{\"ts\":1701069187299,\"x\":null,\"y\":null,\"z\":null},{\"ts\":1701069202902,\"x\":null,\"y\":null,\"z\":null}],\"bePaste\":[],\"beMouse\":[],\"beKeyboard\":[],\"beScroll\":[],\"beTouch\":[],\"beWheel\":[],\"windowState\":[{\"ts\":1701069186257,\"v\":1},{\"ts\":1701069186257,\"v\":1},{\"ts\":1701069186388,\"v\":2},{\"ts\":1701069186388,\"v\":2},{\"ts\":1701069186402,\"v\":1},{\"ts\":1701069186402,\"v\":1},{\"ts\":1701069200309,\"v\":2},{\"ts\":1701069200309,\"v\":2},{\"ts\":1701069201865,\"v\":1},{\"ts\":1701069201865,\"v\":1}],\"isTrusted\":1},\"wID\":{\"sdkVersion\":\"4.4.6\",\"scmVersion\":\"1.0.0.96\",\"msgType\":2,\"timestamp\":\"1701069221819\",\"aid\":368462,\"aidList\":[1988,368462],\"privacyMode\":516},\"custom\":{},\"window\":{\"location\":\"https://www.tiktok.com/@funnykittensttk/video/7293517029737352454?is_from_webapp=1&web_id=7260049563725497899\"},\"msgMeta\":{\"msgType\":2,\"msgSrcProp\":2,\"msgProtocol\":1,\"aid\":368462,\"aidList\":[1988,368462]}}",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/encrypt-str-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `data` | string | yes | Raw fingerprint data string (please convert JSON format to string before requesting)  |

## Details

Encrypt raw fingerprint data for TikTok web interactions. Pass the stringified JSON payload in the `data` parameter to receive the encrypted result.

### Use cases

- Encrypting client fingerprint payloads for TikTok web automation.
- Preparing formatted request parameters for web endpoint calls.
- Generating encrypted device or browser string data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/encrypt-str-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"data": "7218694761253735723"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | string | Yes | Raw fingerprint data string (please convert JSON format to string before requesting) |

### Notes

- Convert JSON format to a string before passing it into `data`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/encrypt-str-data.json`](../../../../catalog/models/tiktok/web/encrypt-str-data.json) · Store page: https://www.sandbase.ai/model/tiktok/web/encrypt-str-data
