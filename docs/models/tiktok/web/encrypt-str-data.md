# TikTok Web StrData Encryption API: pricing, parameters and code examples

`tiktok/web/encrypt-str-data` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Encrypts raw fingerprint string data for TikTok web requests. Takes a stringified JSON fingerprint payload via the data parameter and returns the encrypted string.

## Pricing

- **$0.001 per call** (USD)
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

This API encrypts a raw fingerprint string for TikTok web requests. It needs one input, `data`, which is a JSON fingerprint payload converted to a string. It returns the encrypted string and its length.

### Use cases

- Encrypt a browser fingerprint payload before you send it in a TikTok web request.
- Build the encrypted `StrData` value for a device registration call.
- Check the encrypted output of a fingerprint you made with the fingerprint generator.
- Script repeatable TikTok web request flows that need an encrypted string parameter.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/encrypt-str-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"data": "7218694761253735723"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | string | Yes | Raw fingerprint data string (please convert JSON format to string before requesting) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "encrypted": "3k6yTlt/uIlvc2Z8k7tNo1LbfxcqSpploVv0153cLn4MP1c7816ZeE9VkzuszWHfLjZn/xtBgiNrF8jx…",
  "length": 96
}
```

### Response fields

| Field | Meaning |
|---|---|
| `encrypted` | The encrypted version of the string you sent in `data`. It looks like a Base64-style text value that ends in `==`. |
| `length` | The character count of the `encrypted` string. In the sample response it is `96`. |

### Notes

- Convert your JSON fingerprint to a string before you pass it in `data`. The API takes one string, not a nested object.
- To get a fingerprint payload to encrypt, call [TikTok Web Browser Fingerprint](/apis/tiktok/web/generate-fingerprint).
- To turn an encrypted string back into readable data, call [TikTok Web String Data Decryption](/apis/tiktok/web/decrypt-str-data).
- Use the encrypted value in [TikTok Web Device Registration](/apis/tiktok/web/device-register) if that call needs it.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/encrypt-str-data.json`](../../../../catalog/models/tiktok/web/encrypt-str-data.json) · Store page: https://www.sandbase.ai/model/tiktok/web/encrypt-str-data
