# LinkedIn Group API: pricing, parameters and code examples

`linkedin/group` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0013 per call · **Modes:** sync

Fetch one LinkedIn group by URL or id: name, description, rules, member count, logo and cover image, creation date, visibility and join settings, and its admins.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0013**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/group"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/group', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/group", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/group", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/linkedin/group` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | LinkedIn group URL (e.g. https://www.linkedin.com/groups/1898033). Send this or groupId.  |
| `groupId` | string |  | Numeric LinkedIn group id (e.g. 1898033), the number in the group URL. Send this or url.  |

## Details

Returns details for one LinkedIn group: name, description, rules, member count, images, visibility settings and a list of admins. Send either the group `url` or the numeric `groupId`.

### Use cases

- Check the size and rules of a LinkedIn group before you decide to join or post in it.
- Find the admins of a group and collect their profile URLs for outreach.
- Track the `memberCount` of competitor or niche groups over time.
- Enrich a list of group URLs with names, descriptions and logos for a research database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/group" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/groups/1898033"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `groupId` | string | No | Numeric LinkedIn group id (e.g. 1898033), the number in the group URL. Send this or url. |
| `url` | string | No | LinkedIn group URL (e.g. https://www.linkedin.com/groups/1898033). Send this or groupId. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "adminCount": 4,
    "admins": [
      {
        "firstName": "Scott",
        "headline": "Human Driven AI Prompts For LinkedIn Content | Co-Founder Of The Expert Content …",
        "id": "ACoAAADiTRQBnmhRYZtBb2XK6jpwgphIRdxlScc",
        "image": "https://media.licdn.com/dms/image/v2/D4E03AQFZ1gz4JjNkcg/profile-displayphoto-sh…",
        "lastName": "Aaron",
        "url": "https://www.linkedin.com/in/scottaaroncoach"
      }
    ],
    "coverImage": "https://media.licdn.com/dms/image/v2/D5607AQH1aNJwDgwX0A/group-heroimage-2560_64…",
    "createdUtc": 1239607151,
    "description": "The Largest LinkedIn Sales Management Group! Companies throw their best salespeo…",
    "id": "1898033",
    "image": "https://media.licdn.com/dms/image/v2/C4E07AQGhdN1m_6ab3A/group-logo_image-shrink…",
    "invitationLevel": "ADMIN",
    "memberCount": 642013,
    "name": "Sales Management Executives",
    "postApprovalEnabled": true,
    "publicVisibility": true
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name` | The group name. |
| `data.description` | The group description text. Long text may be cut. |
| `data.memberCount` | Number of members in the group. |
| `data.createdUtc` | Creation date of the group as a Unix timestamp in seconds (the value `1239607151` is a 10-digit number). |
| `data.publicVisibility / data.postApprovalEnabled` | `publicVisibility` shows whether the group is public. `postApprovalEnabled` shows whether posts need approval before they appear. |
| `data.invitationLevel` | Who can invite others to the group. The sample value is `ADMIN`. |
| `data.rules` | The group rules as plain text, with line breaks. |
| `data.image / data.coverImage` | URLs of the group logo and the cover image. |
| `data.adminCount` | Number of admins the group has. |
| `data.admins[].firstName / data.admins[].lastName / data.admins[].headline / data.admins[].url` | Name, profile headline and LinkedIn profile URL of each admin. The list may hold fewer admins than `adminCount`. |

### Notes

- Copy the group URL from the browser, or use the number in it as `groupId`. For `https://www.linkedin.com/groups/1898033` the id is `1898033`.
- Send `url` or `groupId`, not both. If nothing matches, the call succeeds and returns `found: false`.
- Call [LinkedIn Group Posts](/apis/linkedin/group-posts) to read the posts in a group.
- Use [LinkedIn Group Search](/apis/linkedin/search-groups) to find group ids by keyword.

### Pricing

Billed at the actual cost of each call, about $0.0013 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/group.json`](../../../catalog/models/linkedin/group.json) · Store page: https://www.sandbase.ai/model/linkedin/group
