# X (Twitter) Twitter Tweet Transcript API: pricing, parameters and code examples

`twitter/tweet-transcript` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Extract the spoken transcript from a Twitter/X video tweet by URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/tweet-transcript", "url": "https://x.com/TheoVon/status/1916982720317821050"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/tweet-transcript', {'url': 'https://x.com/TheoVon/status/1916982720317821050'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/tweet-transcript", {
  "url": "https://x.com/TheoVon/status/1916982720317821050"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/tweet-transcript", sandbase.Params{
	"url": "https://x.com/TheoVon/status/1916982720317821050",
})
```

Same call via the path form: `POST /v1/api/twitter/tweet-transcript` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Tweet URL of the video to transcribe (e.g. https://x.com/TheoVon/status/1916982720317821050).  |

## Details

Returns the spoken transcript of a video posted on X (Twitter) as plain text. It needs the `url` of the tweet that contains the video.

### Use cases

- Turn an interview or podcast clip posted on X into searchable text.
- Quote a speaker accurately in an article without replaying the video.
- Feed video tweet speech into a summary or sentiment pipeline.
- Check what was said in a video tweet before you reply or moderate it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/tweet-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://x.com/TheoVon/status/1916982720317821050"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Tweet URL of the video to transcribe (e.g. https://x.com/TheoVon/status/1916982720317821050). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "transcript": "Since you're kind of like a leader in innovation and technology, in our world, y…"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.transcript` | The spoken words from the tweet video as one text string. It includes filler words such as "Um", so the text reads like raw speech. |
| `found` | `true` when the lookup returned a result. A lookup that finds nothing returns `false`. |

### Notes

- Pass the full tweet link in `url`, in the form `https://x.com/<user>/status/<tweet id>`.
- The tweet must contain a video. Use [X (Twitter) Twitter Tweet](/apis/twitter/tweet) to get the tweet's own details, such as its text and author.
- The response has no timestamps or speaker labels, only a single `transcript` string.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/tweet-transcript.json`](../../../catalog/models/twitter/tweet-transcript.json) · Store page: https://www.sandbase.ai/model/twitter/tweet-transcript
