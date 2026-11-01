# Douyin Video ID Extractor

`douyin/web/aweme-id` · api · Douyin

Extracts the internal video ID from a given Douyin video web URL. Useful for parsing links before calling downstream video detail endpoints.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/aweme-id", "url": "https://static.sandbase.ai/examples/8199cdcf-9adb-4073-a093-e4e83b70e1d0/input/0598f8d8-d74b-4fae-997a-faec7227135f.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/aweme-id', {'url': 'https://static.sandbase.ai/examples/8199cdcf-9adb-4073-a093-e4e83b70e1d0/input/0598f8d8-d74b-4fae-997a-faec7227135f.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/aweme-id", {
  "url": "https://static.sandbase.ai/examples/8199cdcf-9adb-4073-a093-e4e83b70e1d0/input/0598f8d8-d74b-4fae-997a-faec7227135f.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/aweme-id", sandbase.Params{
	"url": "https://static.sandbase.ai/examples/8199cdcf-9adb-4073-a093-e4e83b70e1d0/input/0598f8d8-d74b-4fae-997a-faec7227135f.bin",
})
```

Same call via the path form: `POST /v1/api/douyin/web/aweme-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Url  |

## Details

Parse a Douyin video link provided in `url` to extract its underlying video ID.

### Use cases

- Extract video IDs from shared Douyin web links.
- Normalize video URLs before querying metadata endpoints.
- Resolve raw post links captured from social feeds.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/aweme-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.douyin.com/video/7512756548356492544"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | — |

### Notes

- Requires a valid Douyin video URL in the `url` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/aweme-id.json`](../../../../catalog/models/douyin/web/aweme-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/aweme-id
