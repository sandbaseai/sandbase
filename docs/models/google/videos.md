# Google Videos API: pricing, parameters and code examples

`google/videos` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Search Google for video results (YouTube and others) with title, link, thumbnail, and source.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/videos", "query": "lofi hip hop"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/videos', {'query': 'lofi hip hop'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/videos", {
  "query": "lofi hip hop"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/videos", sandbase.Params{
	"query": "lofi hip hop",
})
```

Same call via the path form: `POST /v1/api/google/videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Two-letter country code for result localization (e.g. us, gb, de). default `"us"` |
| `hl` | string |  | Two-letter interface and results language code (e.g. en, es, de). default `"en"` |
| `query` | string | yes | The video search query.  |
| `location` | string |  | Fine-grained location for result localization, given as a canonical Google location string (e.g. 'New York, United States', 'London, United Kingdom'). More specific than the country-level gl.  |
| `timeframe` | string |  | Restrict results to a recent time window: 1h, 1d, 7d, 1y, or all. Default all (no time restriction). one of: `1h`, `1d`, `7d`, `1y`, `all` |
| `autocorrect` | boolean |  | Toggle Google spelling autocorrect (default true). Set false to search the exact query without correction.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `source`, and it is served only by a source that returns every one…  |

## Details

Returns Google video search results for a text query. Each result has a title, link, position, snippet, and thumbnail image. The only required input is `query`.

### Use cases

- Find YouTube videos that rank on Google for a keyword.
- Track which videos appear first for a topic in a given country or language.
- Collect video links and titles to build a content list for a topic.
- Check how results change when you set `timeframe` to `7d` or `1y`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"gl": "us", "hl": "en", "query": "lofi hip hop"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The video search query. |
| `autocorrect` | boolean | No | Toggle Google spelling autocorrect (default true). Set false to search the exact query without correction. |
| `gl` | string | No | Two-letter country code for result localization (e.g. us, gb, de). |
| `hl` | string | No | Two-letter interface and results language code (e.g. en, es, de). |
| `location` | string | No | Fine-grained location for result localization, given as a canonical Google location string (e.g. 'New York, United States', 'London, United Kingdom'). More specific than the country-level gl. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `source`, and it is served only by a source that returns every one of  |
| `timeframe` | string | No | Restrict results to a recent time window: 1h, 1d, 7d, 1y, or all. Default all (no time restriction). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "query": "lofi hip hop",
    "results": [
      {
        "image": "",
        "link": "https://www.youtube.com/watch?v=rFZHOHl-L8A",
        "position": 1,
        "snippet": "Spooky season is officially upon us 2026 Halloween playlist available now: https…",
        "title": "lofi hip hop radio beats to relax/study to"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.query` | The search query that Google ran. It can differ from your input if autocorrect changed it. |
| `data.results[].position` | Rank of the video in the result list, starting at 1. |
| `data.results[].title` | Title of the video result. |
| `data.results[].link` | URL of the video page, such as a YouTube watch link. |
| `data.results[].snippet` | Text shown under the result. It can include the description start, the site name, the channel name, and a date. |
| `data.results[].image` | Thumbnail of the video. It is either an empty string or an inline base64 `data:image/jpeg` value. |
| `found` | `true` when the search returned results. |

### Notes

- The `source` field is not in this response. Pass `requireFields: ["source"]` if you need it. This can change the price.
- The site and channel name appear inside `snippet`, after the description text.
- Use `gl`, `hl`, and `location` to localize results. Use `location` for city-level targeting.
- For image results on the same query, call [Google Images](/apis/google/images).

### Pricing

Billed at the actual cost of each call, about $0.00085 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/videos.json`](../../../catalog/models/google/videos.json) · Store page: https://www.sandbase.ai/model/google/videos
