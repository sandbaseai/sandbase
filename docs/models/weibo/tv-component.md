# Weibo TV Video Details API: pricing, parameters and code examples

`weibo/tv-component` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get Weibo TV video details for a colon-delimited object ID (OID). Use it to look up a known TV video for content review, cataloging, or downstream processing.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/tv-component", "oid": "1022:2309405359416706203708"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/tv-component', {'oid': '1022:2309405359416706203708'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/tv-component", {
  "oid": "1022:2309405359416706203708"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/tv-component", sandbase.Params{
	"oid": "1022:2309405359416706203708",
})
```

Same call via the path form: `POST /v1/api/weibo/tv-component` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `oid` | string | yes | Weibo video/object ID.  |

## Details

This API takes a Weibo object ID (`oid`) for a TV video and returns the video's play component data. The `oid` is colon-delimited, for example `1022:2309405359416706203708`.

### Use cases

- Check whether a known Weibo TV video ID returns play information before you add it to a catalog.
- Run a quick lookup on a stored `oid` during content review.
- Pass a video `oid` into a pipeline that reads the play component data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/tv-component" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oid": "1022:2309405359416706203708"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oid` | string | Yes | Weibo video/object ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": "100000",
  "data": {
    "Component_Play_Playinfo": null
  },
  "msg": "succ"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code` | Status code of the response. The sample shows `100000`. |
| `msg` | Status message. The sample shows `succ`. |
| `data` | Container for the result of the lookup. |
| `data.Component_Play_Playinfo` | Play information for the video. It is `null` in the sample response, so no play details came back for this `oid`. |

### Notes

- The `oid` has two parts separated by a colon. The example is `1022:2309405359416706203708`.
- A `code` of `100000` with `msg` set to `succ` can still return `data.Component_Play_Playinfo` as `null`. Check that field before you use the result.
- If you need video data for a different ID, try [Weibo Video Detail](/apis/weibo/app/video-detail).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/weibo/tv-component.json`](../../../catalog/models/weibo/tv-component.json) · Store page: https://www.sandbase.ai/model/weibo/tv-component
