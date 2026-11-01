# Bilibili Video Danmaku

`bilibili/video-danmu` · api · Bilibili

Get one page of danmaku comments for a Bilibili video segment identified by AID and CID. Use it to review time-synchronized audience reactions or page through danmaku for a known video.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/video-danmu", "aid": "80433022", "cid": "137649199"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/video-danmu', {'aid': '80433022', 'cid': '137649199'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/video-danmu", {
  "aid": "80433022",
  "cid": "137649199"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/video-danmu", sandbase.Params{
	"aid": "80433022",
	"cid": "137649199",
})
```

Same call via the path form: `POST /v1/api/bilibili/video-danmu` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aid` | string | yes | Bilibili Archive ID (AID).  |
| `cid` | string | yes | Bilibili Chat ID (CID).  |
| `page` | string |  | Page number for pagination.  |

## Details

Get one page of danmaku comments for a Bilibili video segment identified by AID and CID. Use it to review time-synchronized audience reactions or page through danmaku for a known video.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/video-danmu" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aid": "80433022", "cid": "137649199"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aid` | string | Yes | Bilibili Archive ID (AID). |
| `cid` | string | Yes | Bilibili Chat ID (CID). |
| `page` | string | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/bilibili/video-danmu.json`](../../../catalog/models/bilibili/video-danmu.json) · Store page: https://www.sandbase.ai/model/bilibili/video-danmu
