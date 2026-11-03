# Instagram Media Transcript API: pricing, parameters and code examples

`instagram/media-transcript` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Get the spoken-audio transcript text for an Instagram post or reel by URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/media-transcript", "url": "https://www.instagram.com/reel/DHsD6HGqJhp/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/media-transcript', {'url': 'https://www.instagram.com/reel/DHsD6HGqJhp/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/media-transcript", {
  "url": "https://www.instagram.com/reel/DHsD6HGqJhp/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/media-transcript", sandbase.Params{
	"url": "https://www.instagram.com/reel/DHsD6HGqJhp/",
})
```

Same call via the path form: `POST /v1/api/instagram/media-transcript` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Instagram post or reel URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `durationSeconds`, and it is served only by a source that returns…  |

## Details

This API returns the spoken-audio transcript of an Instagram post or reel. You send the post or reel URL in `url`. The response lists the transcript text with the post's media ID and shortcode.

### Use cases

- Pull the spoken words from a competitor's reel to review its script and hooks.
- Index reel transcripts so you can search a set of videos by what the creator says.
- Feed transcript text into a summarizer or translation tool without watching the video.
- Check whether a reel mentions a brand or product name in its audio.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/media-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/reel/DHsD6HGqJhp/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Instagram post or reel URL. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `durationSeconds`, and it is served only by a source that returns ever |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "transcripts": [
      {
        "durationSeconds": null,
        "id": "3597267389859272809",
        "shortcode": "DHsD6HGqJhp",
        "text": "Let's fry up the perfect bun sale. Beautiful. Everybody, shh. The perfect bun sa…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the lookup matched a post. A lookup that finds nothing returns `found: false`. |
| `data.transcripts[]` | List of transcripts for the post. The sample call returned one item. |
| `data.transcripts[].text` | The transcript of the spoken audio in the post or reel. |
| `data.transcripts[].shortcode` | The short code from the Instagram URL, such as `DHsD6HGqJhp`. |
| `data.transcripts[].id` | The numeric Instagram media ID of the post, returned as a string. |
| `data.transcripts[].durationSeconds` | The length of the video. It is `null` in the sample response. Set `requireFields` to `durationSeconds` to ask for a source that returns it. |

### Notes

- Copy the `url` from the Instagram post or reel page, for example `https://www.instagram.com/reel/DHsD6HGqJhp/`.
- `durationSeconds` can be `null` with the default routing. Pass `requireFields: ["durationSeconds"]` to be served only by a source that returns it. This can raise the price.
- To convert between `id` and `shortcode`, use [Instagram Shortcode to Media ID](/apis/instagram/v1/shortcode-to-media-id) or [Instagram Media ID to Shortcode (V1)](/apis/instagram/v1/media-id-to-shortcode).
- For captions, counts and other post data, call [Instagram Post Details](/apis/instagram/post-detail).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/media-transcript.json`](../../../catalog/models/instagram/media-transcript.json) · Store page: https://www.sandbase.ai/model/instagram/media-transcript
