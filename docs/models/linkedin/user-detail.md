# LinkedIn User Profile API: pricing, parameters and code examples

`linkedin/user-detail` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get a LinkedIn profile by username, including documented core profile fields such as name and headline. Use it to inspect a person's professional background or before requesting published posts.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/user-detail", "username": "williamhgates"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/user-detail', {'username': 'williamhgates'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/user-detail", {
  "username": "williamhgates"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/user-detail", sandbase.Params{
	"username": "williamhgates",
})
```

Same call via the path form: `POST /v1/api/linkedin/user-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | LinkedIn username from the profile URL, for example jack from linkedin.com/in/jack.  |

## Details

This API returns a public LinkedIn profile for one person. It needs the LinkedIn `username` from the profile URL, for example `williamhgates` from linkedin.com/in/williamhgates. The response includes name, position, location, work history, education, follower count, and recent posts and activity.

### Use cases

- Check a person's current role and employer before a sales or partnership outreach.
- Build a career timeline from the `experience` and `education` lists.
- Rank influencers by `followers` and the `influencer` flag.
- Find related people to research next using `similar_profiles`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/user-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "williamhgates"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | LinkedIn username from the profile URL, for example jack from linkedin.com/in/jack. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "about": "Chair of the Gates Foundation. Founder of Breakthrough Energy. Co-founder of Mic…",
  "activity": [
    {
      "id": "7522801130767224832",
      "img": "https://media.licdn.com/dms/image/sync/v2/D4E27AQFkOX_Yu-a3fA/articleshare-shrin…",
      "interaction": "Bill Gates shared this",
      "link": "https://www.linkedin.com/posts/williamhgates_world-bank-says-small-ai-could-tran…",
      "title": "Useful advice for farmers, in their own language, on a phone they already have i…"
    }
  ],
  "avatar": "https://media.licdn.com/dms/image/v2/D5603AQF-RYZP55jmXA/profile-displayphoto-sh…",
  "banner_image": "https://media.licdn.com/dms/image/v2/D5616AQEjhPbTCeblYg/profile-displaybackgrou…",
  "bio_links": [
    {
      "link": "https://gatesnot.es/sourcecode-li",
      "title": "Blog"
    }
  ],
  "city": "Seattle, Washington, United States",
  "connections": 8,
  "country_code": "US",
  "current_company": {
    "company_id": "gates-foundation",
    "name": "Gates Foundation",
    "title": "Co-chair"
  },
  "current_company_company_id": "gates-foundation",
  "current_company_name": "Gates Foundation",
  "default_avatar": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `name / first_name / last_name` | The person's full name and its parts. |
| `position` | The headline text shown under the person's name. |
| `about` | The free-text summary section of the profile. |
| `city / country_code` | Location of the person as a readable place and a country code. |
| `followers / connections` | Counts of followers and connections shown on the profile. Check `influencer` for the platform's influencer flag. |
| `current_company.name / current_company.title / current_company.company_id` | The current employer, the person's title there, and the company's LinkedIn ID. |
| `experience[].company / experience[].title / experience[].start_date / experience[].end_date` | Each job entry with the company, role and dates. An `end_date` of `Present` marks a current role. |
| `education[].title / education[].start_year / education[].end_year` | Each school with the years attended, when listed. |
| `posts[].title / posts[].link / posts[].created_at / posts[].interaction` | Recent published articles with link, date, and a text summary of engagement. |
| `activity[].title / activity[].link / activity[].interaction` | Recent activity such as shared posts, with the post text and link. |

### Notes

- Take `username` from the part of the profile URL after `linkedin.com/in/`. The response echoes it in `linkedin_id` and `id`.
- `linkedin_num_id` holds the numeric profile ID. Post IDs in `posts[].id` and `activity[].id` are long numeric strings.
- `similar_profiles[].url` gives the profile URL of related people. Use the last part of the URL as `username` in a new call.
- For a longer list of posts, call [LinkedIn Profile Posts (full)](/apis/linkedin/profile-posts-full) or [LinkedIn Profile Posts (basic)](/apis/linkedin/profile-posts-thin).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/user-detail.json`](../../../catalog/models/linkedin/user-detail.json) · Store page: https://www.sandbase.ai/model/linkedin/user-detail
