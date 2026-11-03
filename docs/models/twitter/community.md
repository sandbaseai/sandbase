# X (Twitter) Twitter Community API: pricing, parameters and code examples

`twitter/community` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0001 per call · **Modes:** sync

Fetch a Twitter/X community's public details (name, description, member count, join policy) by URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0001**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/community", "url": "https://x.com/i/communities/1926186499399139650"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/community', {'url': 'https://x.com/i/communities/1926186499399139650'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/community", {
  "url": "https://x.com/i/communities/1926186499399139650"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/community", sandbase.Params{
	"url": "https://x.com/i/communities/1926186499399139650",
})
```

Same call via the path form: `POST /v1/api/twitter/community` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Community URL (e.g. https://x.com/i/communities/1926186499399139650).  |

## Details

Returns the public details of one X (Twitter) community: name, description, member count, join policy, creator handle and rules. It needs the community URL as the `url` parameter.

### Use cases

- Check the size and join policy of a community before you decide to join or promote in it.
- Track `memberCount` for a list of communities to see which ones grow.
- Read the rules of a community before you plan posts for it.
- Find the creator of a community and start outreach from their handle.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/community" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://x.com/i/communities/1926186499399139650"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Community URL (e.g. https://x.com/i/communities/1926186499399139650). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "createdUtc": 1748073622,
    "creatorHandle": "carsonrmccann",
    "description": "This community is for creators and builders who are growing to their first 1,000…",
    "id": "1926186499399139650",
    "joinPolicy": "Open",
    "memberCount": 5626,
    "name": "The First Thousand",
    "nsfw": false,
    "rules": [
      {
        "name": "No Empty Platitudes"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name` | Display name of the community. |
| `data.description` | Text the community uses to describe its purpose. |
| `data.memberCount` | Number of members in the community. |
| `data.joinPolicy` | How people can join. The sample value is `Open`. |
| `data.creatorHandle` | X handle of the user who created the community. |
| `data.createdUtc` | Creation time as a Unix timestamp in seconds (UTC). |
| `data.rules[].name` | Title of each community rule, in the order returned. |
| `data.nsfw` | `true` if the community is marked as adult content, otherwise `false`. |
| `data.id` | Numeric community ID as a string. It matches the ID at the end of the input URL. |
| `found` | `true` when the community was found. A lookup that finds nothing returns `false`. |

### Notes

- Copy the URL from the community page. It has the form `https://x.com/i/communities/<id>`.
- To see what members post, call [X (Twitter) Twitter Community Tweets](/apis/twitter/community-tweets).
- To list the people who run the community, call [X (Twitter) Community Moderators](/apis/twitter/community-moderators).
- To find communities by keyword instead of by URL, use [X / Twitter Community Search](/apis/twitter/search-communities).

### Pricing

Billed at the actual cost of each call, about $0.0001 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/community.json`](../../../catalog/models/twitter/community.json) · Store page: https://www.sandbase.ai/model/twitter/community
