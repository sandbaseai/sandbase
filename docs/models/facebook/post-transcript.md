# Facebook Post Transcript API: pricing, parameters and code examples

`facebook/post-transcript` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Get the spoken-word transcript of any public Facebook video post by URL as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/post-transcript", "url": "https://www.facebook.com/reel/2166091230582141/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/post-transcript', {'url': 'https://www.facebook.com/reel/2166091230582141/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/post-transcript", {
  "url": "https://www.facebook.com/reel/2166091230582141/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/post-transcript", sandbase.Params{
	"url": "https://www.facebook.com/reel/2166091230582141/",
})
```

Same call via the path form: `POST /v1/api/facebook/post-transcript` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The Facebook post or video URL.  |

## Details

This API returns the spoken-word transcript of a public Facebook video post or reel. It needs one input, the post or video `url`. The response also includes the video length and the post ID.

### Use cases

- Turn a Facebook reel into text so you can search or quote what the speaker says.
- Check the spoken claims in a video post without watching it.
- Feed reel transcripts into a summary or topic tagging pipeline.
- Add captions or a text version of a Facebook video to a content archive.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/post-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/reel/2166091230582141/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The Facebook post or video URL. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "durationSeconds": 30.067,
    "postId": "1393461115481927",
    "transcript": "How far is too far? There's only one way to find out."
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the API found the post and returned data. A lookup that finds nothing returns `false`. |
| `data.transcript` | The spoken words in the video as plain text. |
| `data.durationSeconds` | The video length in seconds, as a decimal number such as `30.067`. |
| `data.postId` | The numeric ID of the post. |

### Notes

- Pass a full public Facebook post or reel URL in `url`, for example `https://www.facebook.com/reel/2166091230582141/`.
- The `postId` in the response can differ from the number in the reel URL, so store the `url` you sent if you need to match results back to your input.
- To get post details such as text and engagement, call [Facebook Post](/apis/facebook/post). To read replies, call [Facebook Post Comments](/apis/facebook/post-comments).
- To find reel URLs for a page, use [Facebook Profile Reels](/apis/facebook/profile-reels).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/post-transcript.json`](../../../catalog/models/facebook/post-transcript.json) · Store page: https://www.sandbase.ai/model/facebook/post-transcript
