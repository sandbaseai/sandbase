# Reddit Post Transcript API: pricing, parameters and code examples

`reddit/post-transcript` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Extract the spoken transcript from a Reddit video post by URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/post-transcript", "url": "https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/post-transcript', {'url': 'https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/post-transcript", {
  "url": "https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/post-transcript", sandbase.Params{
	"url": "https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/",
})
```

Same call via the path form: `POST /v1/api/reddit/post-transcript` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Reddit post URL or direct v.redd.it video URL to transcribe.  |
| `language` | string |  | Optional two-letter language code (defaults to en).  |

## Details

This API returns the spoken transcript of a Reddit video post as plain text. It needs the post URL or a direct `v.redd.it` video URL, and it accepts an optional two-letter `language` code.

### Use cases

- Search the spoken content of Reddit clips for names, quotes or topics.
- Add text captions or summaries to videos from a subreddit you track.
- Feed video speech into a sentiment or topic analysis alongside the post's comments.
- Archive the words of a video post as text before the post is removed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/post-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Reddit post URL or direct v.redd.it video URL to transcribe. |
| `language` | string | No | Optional two-letter language code (defaults to en). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "language": "en",
    "postId": "1oiu9xm",
    "transcript": "stop on third down and now Barnhart I hanging spiraling punts touch back Barnhar…",
    "transcriptNotAvailable": false,
    "url": "https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.transcript` | The spoken text of the video as one string. Use it as the main output of the call. |
| `data.transcriptNotAvailable` | A boolean flag. When `true`, the post has no transcript to return, so check it before you read `data.transcript`. |
| `data.language` | The two-letter language code of the transcript, for example `en`. |
| `data.postId` | The Reddit post ID taken from the URL, for example `1oiu9xm`. Use it to match the transcript to other post data. |
| `data.url` | The post URL that the transcript belongs to. |
| `found` | A boolean that shows whether the lookup found the post. It is `true` when a result came back. |

### Notes

- Copy the `url` from the address bar of a Reddit video post, or pass a direct `v.redd.it` link.
- Leave `language` out to use the default `en`. Set it to another two-letter code to change the transcript language.
- To get the title, score and author of the same post, call [Reddit Post](/apis/reddit/post) or [Reddit Post Details](/apis/reddit/app/post-details).
- To read the discussion under the video, call [Reddit Post Comments](/apis/reddit/post-comments).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/reddit/post-transcript.json`](../../../catalog/models/reddit/post-transcript.json) · Store page: https://www.sandbase.ai/model/reddit/post-transcript
