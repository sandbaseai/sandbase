# Zhihu AI Search Stream API: pricing, parameters and code examples

`zhihu/web/ai-search-stream` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Returns streaming AI search results from Zhihu based on a query prompt. Supports conversational multi-turn sessions and chat modes.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/ai-search-stream", "message_content": "test"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/ai-search-stream', {'message_content': 'test'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/ai-search-stream", {
  "message_content": "test"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/ai-search-stream", sandbase.Params{
	"message_content": "test",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/ai-search-stream` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `chat_mode` | string |  | Chat mode, default FAST  |
| `session_id` | string |  | Session ID for multi-turn  |
| `message_content` | string | yes | Search Content  |

## Details

Returns the AI answer to a query from Zhihu AI search as a list of stream events. Each event carries a small piece of the answer text. The only required input is `message_content`, the question or prompt to search.

### Use cases

- Collect a full AI-written answer to a question by joining the `summary` pieces from all `Answer` events.
- Continue a conversation by sending the `session_id` from a first call with a follow-up `message_content`.
- Measure how fast the answer starts using the `ttft` timing values in `system_meta`.
- Log the `trace_id` of each call to match a response to a specific search.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/ai-search-stream" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"message_content": "<message_content>"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `message_content` | string | Yes | Search Content |
| `chat_mode` | string | No | Chat mode, default FAST |
| `session_id` | string | No | Session ID for multi-turn |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "events": [
    {
      "data": {
        "ai_attached_info": "ogN8EhM3NzAzODQ5MDI0OTU1MDMyODE3GJgBIhM3NzAzODQ5MDI0OTU1MDE3MDg2KhM3NzAzODQ5MDI0…",
        "message_id": "7703849024955017086",
        "parent_message_id": "7703849024955032817",
        "session_id": "37616450…"
      },
      "event": "Init",
      "system_meta": {
        "flush_time": 1793692127112,
        "flush_time_format": "15:48:47.112",
        "trace_id": "4361b701-b2b3-4560-95b0-4fb71bf30c68"
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `events[]` | List of stream events in the order they were sent. Each item has an `event` name, a `data` object and a `system_meta` object. |
| `events[].event` | Type of the event. The sample shows `Init` first, followed by `Answer` events. |
| `events[].data.session_id` | ID of the chat session, sent in the `Init` event. Pass it as `session_id` in a later call for a multi-turn chat. |
| `events[].data.message_id / events[].data.parent_message_id` | ID of the new message and the ID of the message before it in the session. |
| `events[].data.summary` | A piece of answer text in an `Answer` event. Join the pieces in order to get the full answer. |
| `events[].data.delta` | Set to `true` when `summary` holds only the new text for this event, not the whole answer so far. |
| `events[].data.cite_dict / events[].data.digital_cite_dict` | Citation maps for the answer text. Both are empty in the sample events. |
| `events[].system_meta.ttft / events[].system_meta.answer_ttft / events[].system_meta.aisp_ttft` | Time to first token values, present on the first `Answer` event. The response does not state their unit. |
| `events[].system_meta.flush_time / events[].system_meta.flush_time_format` | Time the event was sent, as a number and as a `HH:MM:SS.mmm` string. |
| `events[].system_meta.trace_id` | Trace ID shared by all events in the same response. |

### Notes

- Concatenate `events[].data.summary` from the `Answer` events in order to build the full answer text, since each event has `delta` set to `true`.
- To keep a conversation going, read `events[].data.session_id` from the `Init` event and send it as `session_id` in the next call.
- `chat_mode` is optional and defaults to `FAST`.
- To read the full content behind a topic, use [Zhihu Article Search](/apis/zhihu/web/article-search-v3) to find articles and answers on the same query.

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…
- [Zhihu Column Article Detail](/apis/zhihu/web/column-article-detail): Returns detailed information and metadata for a specific Zhihu column article, including author profile details, using a provided article ID.

---
Machine-readable: [`catalog/models/zhihu/web/ai-search-stream.json`](../../../../catalog/models/zhihu/web/ai-search-stream.json) · Store page: https://www.sandbase.ai/model/zhihu/web/ai-search-stream
