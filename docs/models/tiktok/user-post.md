# TikTok User Published Posts

`tiktok/user-post` · api · TikTok

Get posts published by a TikTok user identified by secUid, with cursor pagination and latest or popular sorting. Use it to browse a creator's posting history or continue through their public post feed.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/user-post", "secUid": "MS4wLjABAAAA9BGtvm-UVpvkJWKC9MQO2MwFhXOz2Cp0Euox91YwY-F9EQWLz8gRnVG8sQw6LkMk"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/user-post', {'secUid': 'MS4wLjABAAAA9BGtvm-UVpvkJWKC9MQO2MwFhXOz2Cp0Euox91YwY-F9EQWLz8gRnVG8sQw6LkMk'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/user-post", {
  "secUid": "MS4wLjABAAAA9BGtvm-UVpvkJWKC9MQO2MwFhXOz2Cp0Euox91YwY-F9EQWLz8gRnVG8sQw6LkMk"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/user-post", sandbase.Params{
	"secUid": "MS4wLjABAAAA9BGtvm-UVpvkJWKC9MQO2MwFhXOz2Cp0Euox91YwY-F9EQWLz8gRnVG8sQw6LkMk",
})
```

Same call via the path form: `POST /v1/api/tiktok/user-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sorting criteria for the user's posts. one of: `LATEST`, `MOST_POPULAR`; default `"LATEST"` |
| `cursor` | string |  | Pagination cursor. Use '0' for the first page, then use the max_cursor value returned in the previous response. default `"0"` |
| `secUid` | string | yes | The opaque security ID returned for the TikTok user.  |

## Details

Get posts published by a TikTok user identified by secUid, with cursor pagination and latest or popular sorting. Use it to browse a creator's posting history or continue through their public post feed.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/user-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAA9BGtvm-UVpvkJWKC9MQO2MwFhXOz2Cp0Euox91YwY-F9EQWLz8gRnVG8sQw6LkMk"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | The opaque security ID returned for the TikTok user. |
| `cursor` | string | No | Pagination cursor. Use '0' for the first page, then use the max_cursor value returned in the previous response. |
| `sort` | string | No | Sorting criteria for the user's posts. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/tiktok/user-post.json`](../../../catalog/models/tiktok/user-post.json) · Store page: https://www.sandbase.ai/model/tiktok/user-post
