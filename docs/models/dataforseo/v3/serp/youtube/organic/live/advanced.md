# DataForSEO YouTube Search Results API: pricing, parameters and code examples

`dataforseo/v3/serp/youtube/organic/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

YouTube search results for a keyword: videos, channels and playlists with titles, views, durations and upload dates.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/youtube/organic/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/youtube/organic/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/youtube/organic/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/youtube/organic/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/youtube/organic/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the YouTube search results page for a keyword, as a list of ranked items. Each item carries the channel that published it. You send a `keyword`, plus an optional `location_code` and `language_code`.

### Use cases

- Check which channels and videos rank on YouTube for a target keyword in a given country.
- Track the rank of a competitor channel across a list of search terms.
- Collect channel names, IDs and URLs for a niche to build an outreach list.
- Compare results for the same keyword across different `location_code` and `language_code` values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/youtube/organic/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "coffee", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

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
        "keyword": "coffee",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "youtube"
      },
      "id": "11030829-1614-0139-0000-8c15c5d6ecc7",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.youtube.com/results?search_query=coffee",
          "datetime": "2026-11-03 08:29:37 +00:00",
          "item_types": [
            "youtube_video"
          ],
          "items": [
            {
              "badges": null,
              "block_name": null,
              "block_rank": 2,
              "channel_id": "UCI4_-vEalUX3qB7DSQLbgUw",
              "channel_logo": "https://yt3.ggpht.com/ytc/AIdro_kGbzuHsf8CGdiFeKVM3TKi9r4JmymtqTsx0WMjsLQvZuItYd…",
              "channel_name": "LsLs",
              "channel_url": "https://www.youtube.com/@LsLs-r5h",
              "description": "We poured through the coffee aisle so you don't get shortchanged at the register…"
            }
          ],
          "items_count": 26,
          "keyword": "coffee",
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "6.5972 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "6.6636 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].check_url` | The YouTube search URL that matches the query, so you can open the same results in a browser. |
| `tasks[].result[].datetime` | Time the results were collected, in the format `2026-11-03 08:29:37 +00:00`. |
| `tasks[].result[].item_types` | List of item types found in the results. In this response it holds `youtube_video`. |
| `tasks[].result[].items_count` | Number of items in the result for this keyword. |
| `tasks[].result[].items[].block_rank` | Rank of the item's block on the results page, starting at 1. |
| `tasks[].result[].items[].channel_id` | YouTube ID of the channel that published the item. |
| `tasks[].result[].items[].channel_name / tasks[].result[].items[].channel_url` | Display name of the channel and the link to its YouTube page. |
| `tasks[].result[].items[].channel_logo` | URL of the channel's logo image. |
| `tasks[].result[].items[].description` | Text snippet from the item. It is `null` when none is shown. |
| `tasks[].data.device / tasks[].data.os` | Device and operating system used for the search. In this response they are `desktop` and `windows`. |

### Notes

- Use the `location_code` value `2840` for the United States and `en` for `language_code`.
- The response keeps the original task structure, so read results from `tasks[].result[]`, and the ranked entries from `items[]` inside each result.
- Some fields, such as `badges`, `block_name` and `description`, can be `null`.
- Each task has an `id` such as `11030829-1614-0139-0000-8c15c5d6ecc7`, and `tasks_error` shows how many tasks failed.

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/youtube/organic/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/youtube/organic/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/youtube/organic/live/advanced
