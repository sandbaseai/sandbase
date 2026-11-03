# TikTok Web String Data Decryption API: pricing, parameters and code examples

`tiktok/web/decrypt-str-data` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Decrypts encrypted strData captured from TikTok web network traffic. Pass the captured string to reveal the underlying plaintext response payload.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/decrypt-str-data", "encrypted_data": "3BvqYbNXLLOcZehvxZVbjpAu7vq82RoWmFSJHLFwzDwJIZevE0AeilQfP55LridxmdGGjknoksqIsLqlMHMif0IFK/Br7JWqxOHnYuMwVCnttFc0Y4MFvdVWM5FECiEulJC0Dc+eeVsNSrFnAc9K7fazqdglyJgGLSfXIJmgyCvvQ4pg0u5HBVVugLSWs242X42fjoWymaUCLZJQo6vi6WLyuV7l5IC3Mg+lelr5xBQD6Q7hBIFEw8zzxJ1n2DyA4xLbOHTQdKvEtsK7XzyWwjpRnojPTbBl69Zosnuru+lOBIl+tFu/+hCQ1m0jYZwTP4rVE75L3Du6+KZ5v/9TyFYjq7y3y9bGLP4d7yQueJbF90G1yrZ6htElrZ2vqZKDrIqBVbmOZr/nph12k2JKrITtN0R/pMsp0sJ4gesQnXxcD/pLOFAINHk7umgbe6LzJ7+TLUdGuO4M7xiEg/jCqhjgJX1izZ4NPoBDp35zRxj6Y6OrcstlTN/cv5sz663+Nco/mEwhGq2VwrL4gAIAPycndIsb48dPdtngmLqNDNN0ZyVRjgqVIDXXrxigXCkR9CH89Dlrrb7QQqWVgRXz9/k5ihEM43BR3sd3mMU/XgFLN1Aoxf6GzzdxP2QPBI75/ZoHoAmu54v8gTmA3ntCGlEF0zgaFGTdpkGdb+oZgyQM4pw1aAyxmFINXkpD3IKKoGev9kD9gTFnhiQMGCMemhZS7ZYdbuGu0Cb+lQKaL/QTt80FMyGmW8kzVy9xW/ja9BcdEJYRoaufuFRkBFG5ay8x4WHLR6hEapXqQial/cREbLL4sQytpjtmnndFqvT7xN5DhgsLY2Z7451MJhD6NJXKNrMafGZSbItzQWY="}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/decrypt-str-data', {'encrypted_data': '3BvqYbNXLLOcZehvxZVbjpAu7vq82RoWmFSJHLFwzDwJIZevE0AeilQfP55LridxmdGGjknoksqIsLqlMHMif0IFK/Br7JWqxOHnYuMwVCnttFc0Y4MFvdVWM5FECiEulJC0Dc+eeVsNSrFnAc9K7fazqdglyJgGLSfXIJmgyCvvQ4pg0u5HBVVugLSWs242X42fjoWymaUCLZJQo6vi6WLyuV7l5IC3Mg+lelr5xBQD6Q7hBIFEw8zzxJ1n2DyA4xLbOHTQdKvEtsK7XzyWwjpRnojPTbBl69Zosnuru+lOBIl+tFu/+hCQ1m0jYZwTP4rVE75L3Du6+KZ5v/9TyFYjq7y3y9bGLP4d7yQueJbF90G1yrZ6htElrZ2vqZKDrIqBVbmOZr/nph12k2JKrITtN0R/pMsp0sJ4gesQnXxcD/pLOFAINHk7umgbe6LzJ7+TLUdGuO4M7xiEg/jCqhjgJX1izZ4NPoBDp35zRxj6Y6OrcstlTN/cv5sz663+Nco/mEwhGq2VwrL4gAIAPycndIsb48dPdtngmLqNDNN0ZyVRjgqVIDXXrxigXCkR9CH89Dlrrb7QQqWVgRXz9/k5ihEM43BR3sd3mMU/XgFLN1Aoxf6GzzdxP2QPBI75/ZoHoAmu54v8gTmA3ntCGlEF0zgaFGTdpkGdb+oZgyQM4pw1aAyxmFINXkpD3IKKoGev9kD9gTFnhiQMGCMemhZS7ZYdbuGu0Cb+lQKaL/QTt80FMyGmW8kzVy9xW/ja9BcdEJYRoaufuFRkBFG5ay8x4WHLR6hEapXqQial/cREbLL4sQytpjtmnndFqvT7xN5DhgsLY2Z7451MJhD6NJXKNrMafGZSbItzQWY='})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/decrypt-str-data", {
  "encrypted_data": "3BvqYbNXLLOcZehvxZVbjpAu7vq82RoWmFSJHLFwzDwJIZevE0AeilQfP55LridxmdGGjknoksqIsLqlMHMif0IFK/Br7JWqxOHnYuMwVCnttFc0Y4MFvdVWM5FECiEulJC0Dc+eeVsNSrFnAc9K7fazqdglyJgGLSfXIJmgyCvvQ4pg0u5HBVVugLSWs242X42fjoWymaUCLZJQo6vi6WLyuV7l5IC3Mg+lelr5xBQD6Q7hBIFEw8zzxJ1n2DyA4xLbOHTQdKvEtsK7XzyWwjpRnojPTbBl69Zosnuru+lOBIl+tFu/+hCQ1m0jYZwTP4rVE75L3Du6+KZ5v/9TyFYjq7y3y9bGLP4d7yQueJbF90G1yrZ6htElrZ2vqZKDrIqBVbmOZr/nph12k2JKrITtN0R/pMsp0sJ4gesQnXxcD/pLOFAINHk7umgbe6LzJ7+TLUdGuO4M7xiEg/jCqhjgJX1izZ4NPoBDp35zRxj6Y6OrcstlTN/cv5sz663+Nco/mEwhGq2VwrL4gAIAPycndIsb48dPdtngmLqNDNN0ZyVRjgqVIDXXrxigXCkR9CH89Dlrrb7QQqWVgRXz9/k5ihEM43BR3sd3mMU/XgFLN1Aoxf6GzzdxP2QPBI75/ZoHoAmu54v8gTmA3ntCGlEF0zgaFGTdpkGdb+oZgyQM4pw1aAyxmFINXkpD3IKKoGev9kD9gTFnhiQMGCMemhZS7ZYdbuGu0Cb+lQKaL/QTt80FMyGmW8kzVy9xW/ja9BcdEJYRoaufuFRkBFG5ay8x4WHLR6hEapXqQial/cREbLL4sQytpjtmnndFqvT7xN5DhgsLY2Z7451MJhD6NJXKNrMafGZSbItzQWY="
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/decrypt-str-data", sandbase.Params{
	"encrypted_data": "3BvqYbNXLLOcZehvxZVbjpAu7vq82RoWmFSJHLFwzDwJIZevE0AeilQfP55LridxmdGGjknoksqIsLqlMHMif0IFK/Br7JWqxOHnYuMwVCnttFc0Y4MFvdVWM5FECiEulJC0Dc+eeVsNSrFnAc9K7fazqdglyJgGLSfXIJmgyCvvQ4pg0u5HBVVugLSWs242X42fjoWymaUCLZJQo6vi6WLyuV7l5IC3Mg+lelr5xBQD6Q7hBIFEw8zzxJ1n2DyA4xLbOHTQdKvEtsK7XzyWwjpRnojPTbBl69Zosnuru+lOBIl+tFu/+hCQ1m0jYZwTP4rVE75L3Du6+KZ5v/9TyFYjq7y3y9bGLP4d7yQueJbF90G1yrZ6htElrZ2vqZKDrIqBVbmOZr/nph12k2JKrITtN0R/pMsp0sJ4gesQnXxcD/pLOFAINHk7umgbe6LzJ7+TLUdGuO4M7xiEg/jCqhjgJX1izZ4NPoBDp35zRxj6Y6OrcstlTN/cv5sz663+Nco/mEwhGq2VwrL4gAIAPycndIsb48dPdtngmLqNDNN0ZyVRjgqVIDXXrxigXCkR9CH89Dlrrb7QQqWVgRXz9/k5ihEM43BR3sd3mMU/XgFLN1Aoxf6GzzdxP2QPBI75/ZoHoAmu54v8gTmA3ntCGlEF0zgaFGTdpkGdb+oZgyQM4pw1aAyxmFINXkpD3IKKoGev9kD9gTFnhiQMGCMemhZS7ZYdbuGu0Cb+lQKaL/QTt80FMyGmW8kzVy9xW/ja9BcdEJYRoaufuFRkBFG5ay8x4WHLR6hEapXqQial/cREbLL4sQytpjtmnndFqvT7xN5DhgsLY2Z7451MJhD6NJXKNrMafGZSbItzQWY=",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/decrypt-str-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `encrypted_data` | string | yes | Encrypted strData string, obtained from browser packet capture  |

## Details

This API decrypts an encrypted `strData` string captured from TikTok web network traffic. It needs one input, `encrypted_data`, and returns the plaintext as a string along with its length.

### Use cases

- Read the plaintext of a `strData` value you captured in browser developer tools.
- Check which client behavior records, such as motion events, a TikTok web client sent in a request.
- Compare decrypted payloads from different sessions to see how the captured data changes.
- Test a string you built with the encryption API to confirm it decrypts back to your input.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/decrypt-str-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"encrypted_data": "3BvqYbNXLLOcZehvxZVbjpAu7vq82RoWmFSJHLFwzDwJIZevE0AeilQfP55LridxmdGGjknoksqIsLqlMHMif0IFK/Br7JWqxOHnYuMwVCnttFc0Y4MFvdVWM5FECiEulJC0Dc+eeVsNSrFnAc9K7fazqdglyJgGLSfXIJmgyCvvQ4pg0u5HBVVugLSWs242X42fjoWymaUCLZJQo6vi6WLyuV7l5IC3Mg+lelr5xBQD6Q7hBIFEw8zzxJ1n2DyA4xLbOHTQdKvEtsK7XzyWwjpRnojPTbBl69Zosnuru+lOBIl+tFu/+hCQ1m0jYZwTP4rVE75L3Du6+KZ5v/9TyFYjq7y3y9bGLP4d7yQueJbF90G1yrZ6htElrZ2vqZKDrIqBVbmOZr/nph12k2JKrITtN0R/pMsp0sJ4gesQnXxcD/pLOFAINHk7umgbe6LzJ7+TLUdGuO4M7xiEg/jCqhjgJX1izZ4NPoBDp35zRxj6Y6OrcstlTN/cv5sz663+Nco/mEwhGq2VwrL4gAIAPycndIsb48dPdtngmLqNDNN0ZyVRjgqVIDXXrxigXCkR9CH89Dlrrb7QQqWVgRXz9/k5ihEM43BR3sd3mMU/XgFLN1Aoxf6GzzdxP2QPBI75/ZoHoAmu54v8gTmA3ntCGlEF0zgaFGTdpkGdb+oZgyQM4pw1aAyxmFINXkpD3IKKoGev9kD9gTFnhiQMGCMemhZS7ZYdbuGu0Cb+lQKaL/QTt80FMyGmW8kzVy9xW/ja9BcdEJYRoaufuFRkBFG5ay8x4WHLR6hEapXqQial/cREbLL4sQytpjtmnndFqvT7xN5DhgsLY2Z7451MJhD6NJXKNrMafGZSbItzQWY="}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `encrypted_data` | string | Yes | Encrypted strData string, obtained from browser packet capture |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "decrypted": "{\"behavior\":{\"beResize\":[],\"beMotion\":[{\"ts\":1701069187299,\"x\":null,\"y\":null,\"z\"…",
  "length": 905
}
```

### Response fields

| Field | Meaning |
|---|---|
| `decrypted` | The decrypted plaintext. In this example it is a JSON document stored as a string. It starts with a `behavior` object that holds lists of recorded client events, such as `beMotion` entries with a `ts` timestamp. Parse the string again to read these keys. |
| `length` | A number returned with the plaintext. The sample shows `905`. The response does not say whether it counts characters or bytes. |

### Notes

- Capture the `encrypted_data` value from your browser's network panel and pass it unchanged.
- The `decrypted` field is a string. Parse it as JSON before you read nested keys.
- To go the other way, use [TikTok Web StrData Encryption](/apis/tiktok/web/encrypt-str-data).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/decrypt-str-data.json`](../../../../catalog/models/tiktok/web/decrypt-str-data.json) · Store page: https://www.sandbase.ai/model/tiktok/web/decrypt-str-data
