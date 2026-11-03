# TikTok Web Stream Search API: pricing, parameters and code examples

`tiktok/web/search-live` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches active TikTok web broadcasts matching a specified keyword. Returns stream details with pagination controls via count and offset parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/search-live", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/search-live', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/search-live", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/search-live", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/search-live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page default `20` |
| `offset` | integer |  | Page offset, 0 for the first request, need to provide for the second paging. default `0` |
| `keyword` | string | yes | Search keyword  |
| `search_id` | string |  | Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request. default `""` |

## Details

This API searches live TikTok broadcasts that match a keyword. It needs one input, `keyword`, and returns a list of live rooms plus paging values.

### Use cases

- Find live rooms on TikTok that mention a brand or product name such as `openai`.
- Collect room titles and viewer counts for a topic to see which streams are active.
- Check which matching rooms sell goods or run battles by reading the room flags.
- Build a paged list of live results for a keyword by passing the paging values back in.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/search-live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `count` | integer | No | Number per page |
| `offset` | integer | No | Page offset, 0 for the first request, need to provide for the second paging. |
| `search_id` | string | No | Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "backtrace": "",
  "cookie": "tt_chain…",
  "cursor": 20,
  "data": [
    {
      "live_info": {
        "raw_data": "{\"id\":7703772241024142094,\"id_str\":\"7703772241024142094\",\"status\":2,\"owner_user_…",
        "room_info": {
          "has_commerce_goods": false,
          "is_battle": false
        }
      }
    }
  ],
  "extra": {
    "api_debug_info": null,
    "fatal_item_ids": [],
    "logid": "202611030744286B42605440E85F01DADD",
    "now": 1793691869000,
    "search_request_id": ""
  },
  "has_more": 0,
  "log_pb": {
    "impr_id": "202611030744286B42605440E85F01DADD"
  },
  "status_code": 0,
  "tt_chain_token": "R2aMeDVd…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].live_info.raw_data` | A JSON string with the full room record. It includes the room `id`, `id_str`, `status`, `owner_user_id`, `title` and `user_count`. Parse the string to read these values. |
| `data[].live_info.room_info.has_commerce_goods` | `true` if the room has commerce goods attached, `false` if not. |
| `data[].live_info.room_info.is_battle` | `true` if the room is in a battle, `false` if not. |
| `cursor` | Position value for the next page. The sample shows `20` for a request with the default `count`. |
| `has_more` | Paging flag. `0` in the sample, which means no further page was signaled. |
| `extra.search_request_id` | Search request ID for the call. It was an empty string in this sample. |
| `extra.now` | Timestamp attached to the response, shown as a 13-digit number. |
| `extra.logid / log_pb.impr_id` | Request log ID and impression ID. They carry the same value in the sample. |
| `status_code` | `0` in the sample, which marks a successful call. |
| `tt_chain_token` | Token string that also appears inside the `cookie` field. |

### Notes

- Set `count` to control how many rooms come back per page. The default is `20`.
- For the next page, send the `cursor` value as `offset` and add the `search_id` the schema asks for. Check `has_more` first.
- Room data sits inside the `raw_data` string, so parse it as JSON to read the room `id_str`.
- To check whether a room is still live, call [TikTok Stream Status Check](/apis/tiktok/web/check-live-alive). For more room detail, call [TikTok Stream Room Information](/apis/tiktok/web/live-data).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/search-live.json`](../../../../catalog/models/tiktok/web/search-live.json) · Store page: https://www.sandbase.ai/model/tiktok/web/search-live
