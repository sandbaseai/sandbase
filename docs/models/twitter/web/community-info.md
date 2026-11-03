# Twitter Community info API: pricing, parameters and code examples

`twitter/web/community-info` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get community info on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/community-info", "community_id": "1493290339532222469"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/community-info', {'community_id': '1493290339532222469'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/community-info", {
  "community_id": "1493290339532222469"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/community-info", sandbase.Params{
	"community_id": "1493290339532222469",
})
```

Same call via the path form: `POST /v1/api/twitter/web/community-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `community_id` | string | yes | Community ID  |

## Details

Returns the profile of one Twitter community: its name, description, member count, banner images and rules. It needs a `community_id`.

### Use cases

- Show a community's name, description and member count in a dashboard.
- Track the growth of a community by saving `member_count` over time.
- Check a community's rules before posting or moderating.
- Flag communities marked as NSFW with `is_nsfw` before showing them to users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/community-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"community_id": "1493290339532222469"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `community_id` | string | Yes | Community ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "created_at": 1644863135598,
  "custom_banner_media": "https://pbs.twimg.com/media/FECS7TfVcAcCrj2.jpg",
  "default_banner_media": "https://pbs.twimg.com/media/FECS7TfVcAcCrj2.jpg",
  "description": "XRP community",
  "id": "1493290339532222469",
  "is_nsfw": false,
  "last_cursor": "",
  "member_count": 123243,
  "name": "XRP",
  "primary_topic": null,
  "rules": [
    {
      "description": "You should be respectful towards others.",
      "name": "Be Respectful"
    }
  ],
  "status": "failed"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Community ID. It matches the `community_id` you sent. |
| `name` | Display name of the community. |
| `description` | Short text that describes the community. |
| `member_count` | Number of members in the community. |
| `created_at` | Creation time of the community as a number. The value looks like a Unix time in milliseconds. |
| `is_nsfw` | `true` if the community is marked as NSFW, otherwise `false`. |
| `custom_banner_media / default_banner_media` | URLs of the community banner images. |
| `rules[].name / rules[].description` | Title and full text of each community rule. |
| `primary_topic` | Main topic of the community. It is `null` when none is set. |
| `status` | Status string in the response. The sample shows `failed`, so check this field in your own code. |

### Notes

- Find a `community_id` with [Twitter Search communities](/apis/twitter/web/search-communities).
- Call [Twitter Community members](/apis/twitter/web/community-members) to list the people in a community.
- Call [Twitter Community timeline](/apis/twitter/web/community-timeline) to read its posts.
- `last_cursor` is an empty string in this response.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/web/community-info.json`](../../../../catalog/models/twitter/web/community-info.json) · Store page: https://www.sandbase.ai/model/twitter/web/community-info
