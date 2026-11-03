# DataForSEO YouTube Subtitles API: pricing, parameters and code examples

`dataforseo/v3/serp/youtube/video_subtitles/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.006 per call (free daily quota) · **Modes:** sync

Fetch the subtitle track of a YouTube video with timestamps. Subtitles of a YouTube video by video_id and language.

## Pricing

- **$0.006 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/youtube/video_subtitles/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/youtube/video_subtitles/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/youtube/video_subtitles/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/youtube/video_subtitles/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/youtube/video_subtitles/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string |  | YouTube video ID.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the subtitle track of a YouTube video as a list of timed text lines. You send a `video_id` and optionally a `language_code` and `location_code`.

### Use cases

- Build a searchable transcript of a video from its subtitle lines.
- Create caption files or quote clips by using the start and end time of each line.
- Feed video text into summarization or topic analysis without downloading the video.
- Check whether a video has subtitles in a given language.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/youtube/video_subtitles/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |
| `video_id` | string | No | YouTube video ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "serp",
        "device": "desktop",
        "function": "live",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "youtube",
        "se_type": "video_subtitles"
      },
      "id": "11030829-1614-0139-0000-776382922759",
      "path": [
        "v3"
      ],
      "result": [
        {
          "category": null,
          "check_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
          "datetime": "2026-11-03 08:29:44 +00:00",
          "item_types": [
            "youtube_subtitles"
          ],
          "items": [
            {
              "duration_time": 1.68,
              "end_time": 3.04,
              "rank_absolute": 1,
              "rank_group": 1,
              "start_time": 1.36,
              "text": "[♪♪♪]",
              "type": "youtube_subtitles"
            }
          ],
          "items_count": 61,
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "10.4056 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "10.4905 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].text` | The subtitle text for one line. A line can contain a newline character and music symbols or bracketed sound cues such as `[♪♪♪]`. |
| `tasks[].result[].items[].start_time / end_time` | When the line appears and disappears. The values look like seconds from the start of the video. |
| `tasks[].result[].items[].duration_time` | How long the line stays on screen. It equals `end_time` minus `start_time`. |
| `tasks[].result[].items[].rank_absolute / rank_group` | Position of the line in the subtitle list, starting at 1. |
| `tasks[].result[].items_count` | Number of subtitle lines in the result. |
| `tasks[].result[].check_url` | The YouTube watch URL for the video that was checked. |
| `tasks[].result[].language_code` | Language code of the returned subtitles. |
| `tasks[].result[].datetime` | Time the result was produced, with a UTC offset. |
| `tasks[].status_code / status_message` | Status of the task. `20000` with `Ok.` means the call succeeded. |

### Notes

- Take `video_id` from the `v` parameter of a YouTube watch URL, for example `dQw4w9WgXcQ` from `https://www.youtube.com/watch?v=dQw4w9WgXcQ`.
- Read the lines from `tasks[].result[].items[]` and sort by `start_time` or `rank_absolute` to keep them in order.
- The request echoes `language_code` and `location_code` in `tasks[].data` and in the result.

### Pricing

$0.006 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/youtube/video_subtitles/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/youtube/video_subtitles/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/youtube/video_subtitles/live/advanced
