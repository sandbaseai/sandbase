# Xigua User Post List

`xigua/app-v2/user-post-list` · api · Xigua

Returns a list of posts from a specific Xigua user account. Supports paginated results using timestamp cursor tokens.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/user-post-list", "user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/user-post-list', {'user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/user-post-list", {
  "user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/user-post-list", sandbase.Params{
	"user_id": "example",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/user-post-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User id  |
| `max_behot_time` | string |  | Maximum behavior time, default empty, pass empty for the first request, pass the max_behot_time returned by the previous request for subsequent requests  |

## Details

Fetch published posts for a specific Xigua user by passing their `user_id`. Supports pagination across multiple pages using the `max_behot_time` parameter.

### Use cases

- Retrieve the video submission history of a specific Xigua creator.
- Monitor new video uploads from monitored Xigua accounts.
- Aggregate profile content timelines for performance tracking.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/user-post-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "<user_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User id |
| `max_behot_time` | string | No | Maximum behavior time, default empty, pass empty for the first request, pass the max_behot_time returned by the previous request for subsequent requests |

### Notes

- Leave `max_behot_time` empty on the first request, then provide the value returned from the previous call for subsequent pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xigua Single Video Information](/model/xigua/app-v2/one-video): Returns lightweight single video data and associated related video information from Xigua for a specific post by its unique item ID.
- [Xigua Video Play URL](/model/xigua/app-v2/one-video-play-url): Returns the direct playback URL for a specific Xigua video using its unique item identifier.
- [Xigua Video Search](/model/xigua/app-v2/search-video): Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.

---
Machine-readable: [`catalog/models/xigua/app-v2/user-post-list.json`](../../../../catalog/models/xigua/app-v2/user-post-list.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/user-post-list
