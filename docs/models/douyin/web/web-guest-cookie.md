# Douyin Web Guest Cookie API: pricing, parameters and code examples

`douyin/web/web-guest-cookie` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a guest cookie for Douyin Web based on a specified browser user agent string. This cookie helps establish identity for browsing web endpoints.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/web-guest-cookie", "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/web-guest-cookie', {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/web-guest-cookie", {
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/web-guest-cookie", sandbase.Params{
	"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
})
```

Same call via the path form: `POST /v1/api/douyin/web/web-guest-cookie` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_agent` | string | yes | User browser agent  |

## Details

Retrieve a guest session cookie for Douyin Web by supplying a valid browser `user_agent`.

### Use cases

- Obtain guest credentials for crawling Douyin Web data.
- Maintain session identity when querying public user and mix videos.
- Prevent duplicate responses across public web data requests.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/web-guest-cookie" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_agent": "<user_agent>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_agent` | string | Yes | User browser agent |

### Notes

- Requires `user_agent` containing a valid browser agent string.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/web-guest-cookie.json`](../../../../catalog/models/douyin/web/web-guest-cookie.json) · Store page: https://www.sandbase.ai/model/douyin/web/web-guest-cookie
