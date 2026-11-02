# Bilibili Video Captions API: pricing, parameters and code examples

`bilibili/video-caption` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get caption data for a Bilibili video segment identified by BVID, AID, and CID. Use it to obtain subtitles for transcript extraction, accessibility review, or language-focused content analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/video-caption", "bvid": "BV1GJ411x7h7", "aid": "80433022", "cid": "137649199"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/video-caption', {'bvid': 'BV1GJ411x7h7', 'aid': '80433022', 'cid': '137649199'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/video-caption", {
  "bvid": "BV1GJ411x7h7",
  "aid": "80433022",
  "cid": "137649199"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/video-caption", sandbase.Params{
	"bvid": "BV1GJ411x7h7",
	"aid": "80433022",
	"cid": "137649199",
})
```

Same call via the path form: `POST /v1/api/bilibili/video-caption` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aid` | string | yes | Bilibili AID.  |
| `cid` | string | yes | Bilibili CID.  |
| `bvid` | string | yes | Bilibili Video ID (BVID).  |

## Details

Get caption data for a Bilibili video segment identified by BVID, AID, and CID. Use it to obtain subtitles for transcript extraction, accessibility review, or language-focused content analysis.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/video-caption" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bvid": "BV1GJ411x7h7", "aid": "80433022", "cid": "137649199"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bvid` | string | Yes | Bilibili Video ID (BVID). |
| `aid` | string | Yes | Bilibili AID. |
| `cid` | string | Yes | Bilibili CID. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/bilibili/video-caption.json`](../../../catalog/models/bilibili/video-caption.json) · Store page: https://www.sandbase.ai/model/bilibili/video-caption
