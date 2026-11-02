# Xiaohongshu User Notes API: pricing, parameters and code examples

`xiaohongshu/user-note-list` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get a user's published public Xiaohongshu (RedNote) notes by user ID or supported profile URL, with lastCursor pagination. This endpoint does not create, upload or publish notes.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/user-note-list", "userId": "64b898310000000014037b21"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/user-note-list', {'userId': '64b898310000000014037b21'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/user-note-list", {
  "userId": "64b898310000000014037b21"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/user-note-list", sandbase.Params{
	"userId": "64b898310000000014037b21",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/user-note-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | A Xiaohongshu user ID or a profile URL containing /user/profile/.  |
| `lastCursor` | string |  | Omit on the first request. For the next page, pass the last note's cursor value from the previous response.  |

## Details

Get a user's published public Xiaohongshu (RedNote) notes by user ID or supported profile URL, with lastCursor pagination. This endpoint does not create, upload or publish notes.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/user-note-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "64b898310000000014037b21"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | A Xiaohongshu user ID or a profile URL containing /user/profile/. |
| `lastCursor` | string | No | Omit on the first request. For the next page, pass the last note's cursor value from the previous response. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/user-note-list.json`](../../../catalog/models/xiaohongshu/user-note-list.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/user-note-list
