# Douyin Webcast ID Extractor API: pricing, parameters and code examples

`douyin/web/webcast-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Resolves and returns the webcast ID from a Douyin live stream web link. Requires the stream URL as input to retrieve internal webcast identifiers.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/webcast-id", "url": "https://static.sandbase.ai/examples/590a708e-2714-4ede-aaf9-860b25b907ff/input/fd36a8df-fe90-4379-80f3-91bc83b2c4b2.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/webcast-id', {'url': 'https://static.sandbase.ai/examples/590a708e-2714-4ede-aaf9-860b25b907ff/input/fd36a8df-fe90-4379-80f3-91bc83b2c4b2.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/webcast-id", {
  "url": "https://static.sandbase.ai/examples/590a708e-2714-4ede-aaf9-860b25b907ff/input/fd36a8df-fe90-4379-80f3-91bc83b2c4b2.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/webcast-id", sandbase.Params{
	"url": "https://static.sandbase.ai/examples/590a708e-2714-4ede-aaf9-860b25b907ff/input/fd36a8df-fe90-4379-80f3-91bc83b2c4b2.bin",
})
```

Same call via the path form: `POST /v1/api/douyin/web/webcast-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Url  |

## Details

Look up internal webcast identifiers directly from a Douyin stream link by supplying `url`.

### Use cases

- Extract internal webcast identifiers from standard Douyin stream URLs.
- Resolve live stream room parameters for downstream data collection.
- Verify target broadcast IDs from web links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/webcast-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://live.douyin.com/775841227732"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | — |

### Notes

- Provide a valid stream link in `url` such as standard live broadcast web addresses.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/webcast-id.json`](../../../../catalog/models/douyin/web/webcast-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/webcast-id
