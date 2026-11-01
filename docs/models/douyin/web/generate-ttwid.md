# Douyin Web TTWID Generator

`douyin/web/generate-ttwid` · api · Douyin

Returns a Douyin web ttwid cookie value required for web session authentication. Accepts an optional custom user agent string.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/generate-ttwid"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/generate-ttwid', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/generate-ttwid", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/generate-ttwid", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/web/generate-ttwid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_agent` | string |  | User Agent  |

## Details

Retrieve a Douyin web ttwid cookie for automated platform queries. You can optionally specify a `user_agent` to match your client environment.

### Use cases

- Obtain valid session identifiers for Douyin web scraping workflows.
- Configure web headers with a matching ttwid cookie and user agent.
- Refresh expired browser session cookies before making platform calls.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/generate-ttwid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_agent` | string | No | — |

### Notes

- Set `user_agent` to match the client headers used in subsequent web requests.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/generate-ttwid.json`](../../../../catalog/models/douyin/web/generate-ttwid.json) · Store page: https://www.sandbase.ai/model/douyin/web/generate-ttwid
