# LinkedIn API: 38 endpoints with pricing and code examples

Call 38 LinkedIn endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`linkedin/ad`](../models/linkedin/ad.md) | Look up a single LinkedIn Ad Library ad by URL and get the advertiser, headline, creative text, format, CTA, targeting, run dates, and… | about $0.0012 per call |
| [`linkedin/ads`](../models/linkedin/ads.md) | Search the LinkedIn Ad Library by search URL and list the matching ads (advertiser, creative text, format). | about $0.0331 per call |
| [`linkedin/ads-search`](../models/linkedin/ads-search.md) | Search the LinkedIn Ad Library by company or keyword and list matching ads (advertiser, headline, creative text, format, CTA, and run… | about $0.0012 per call |
| [`linkedin/article`](../models/linkedin/article.md) | Read a public LinkedIn article or newsletter issue by URL, including its full body text, author, publication time, and engagement counts. | about $0.00569 per call |
| [`linkedin/comment-reactions`](../models/linkedin/comment-reactions.md) | List who reacted to a comment on a LinkedIn post - reactor name, profile URL, job title, and reaction type, 100 per page. | about $0.0026 per call |
| [`linkedin/comment-replies`](../models/linkedin/comment-replies.md) | List up to the 10 newest replies to a comment on a LinkedIn post - reply text, replier name/URL/job title, timestamps, and likes. | about $0.0026 per call |
| [`linkedin/company`](../models/linkedin/company.md) | Fetch a full LinkedIn company page by URL: name, description, industry, employee count and range, follower count, founded year,… | about $0.0011 per call |
| [`linkedin/company-employees`](../models/linkedin/company-employees.md) | List the employees of a LinkedIn company by name or company URL, with optional job-title filtering. | about $0.006 per call |
| [`linkedin/company-posts`](../models/linkedin/company-posts.md) | List a LinkedIn company page's recent posts by URL: full text, canonical link, publish date, author, engagement counts with a per-reaction… | about $0.0029 per call |
| [`linkedin/company-posts-thin`](../models/linkedin/company-posts-thin.md) | Post text and link only. No engagement counts, author details, media, or reaction breakdown - for those use linkedin.company_posts. | about $0.0012 per call |
| [`linkedin/company-thin`](../models/linkedin/company-thin.md) | Basic company: name, description, employee count, industry, logo, website, tagline. No follower count, founded year, office locations, or… | about $0.001 per call |
| [`linkedin/group`](../models/linkedin/group.md) | Fetch one LinkedIn group by URL or id: name, description, rules, member count, logo and cover image, creation date, visibility and join… | about $0.0013 per call |
| [`linkedin/group-posts`](../models/linkedin/group-posts.md) | List the posts in a LinkedIn group by group URL, newest first: full text, canonical link, publish date, author, engagement counts with a… | about $0.0026 per call |
| [`linkedin/jobs`](../models/linkedin/jobs.md) | Search LinkedIn job listings by title and location - full records with description, salary, applicant count, seniority, company details,… | about $0.0195 per call |
| [`linkedin/jobs-thin`](../models/linkedin/jobs-thin.md) | Cheap job index: title, company, location, posted date, URL. No description, salary, applicant counts, or seniority - for those use… | about $0.00066 per call |
| [`linkedin/post`](../models/linkedin/post.md) | Fetch a single LinkedIn post or article by URL (title, text, author, like and comment counts, publish date). | about $0.0008 per call |
| [`linkedin/post-comments`](../models/linkedin/post-comments.md) | List comments on a LinkedIn post - full text, commenter name/URL/job title, timestamps, and engagement. | about $0.0029 per call |
| [`linkedin/post-reactions`](../models/linkedin/post-reactions.md) | List who reacted to a LinkedIn post - reactor name, profile URL, job title, and reaction type. Lead-gen grade. | about $0.0029 per call |
| [`linkedin/post-transcript`](../models/linkedin/post-transcript.md) | Get the spoken transcript of a LinkedIn video post by URL. | about $0.0012 per call |
| [`linkedin/profile-comments`](../models/linkedin/profile-comments.md) | List the comments a LinkedIn member has left on other people's posts - the comment text, its permalink and timestamp, plus the post it was… | about $0.0029 per call |
| [`linkedin/profile-posts-full`](../models/linkedin/profile-posts-full.md) | Fetch recent public LinkedIn profile posts with enriched author, engagement, article, newsletter, media, annotation, repost, and social… | about $0.005 per call |
| [`linkedin/profile-posts-thin`](../models/linkedin/profile-posts-thin.md) | Fetch recent public LinkedIn profile posts with portable identity, author, engagement, article, image, video, and repost fields. | about $0.005 per call |
| [`linkedin/profile-reactions`](../models/linkedin/profile-reactions.md) | List the posts a LinkedIn member has reacted to - the reaction, its timestamp, and the full post it was made on with author and engagement. | about $0.0029 per call |
| [`linkedin/search-companies`](../models/linkedin/search-companies.md) | Search LinkedIn companies by keyword with optional location filtering, returning normalized company records. | about $0.005 per call |
| [`linkedin/search-groups`](../models/linkedin/search-groups.md) | Search LinkedIn groups by keyword, 10 per page: group name, URL, member count, summary, and logo. | about $0.0013 per call |
| [`linkedin/search-leads`](../models/linkedin/search-leads.md) | LinkedIn lead search with Sales Navigator's search and filters: one call returns a page of up to 25 people matching a keyword and Sales… | about $0.07 per call |
| [`linkedin/search-posts`](../models/linkedin/search-posts.md) | Search public LinkedIn posts by keyword (text, link, publish date). Results come from search-engine matches over public LinkedIn posts and… | about $0.0012 per call |
| [`linkedin/search-posts-full`](../models/linkedin/search-posts-full.md) | Search public LinkedIn posts with rich author, engagement, attachment, and poll details. | about $0.004 per call |
| [`linkedin/search-profiles`](../models/linkedin/search-profiles.md) | Search LinkedIn profiles by keyword with optional location and job-title filters. Each match returns a full profile record: name,… | about $0.198 per call |
| [`linkedin/search-profiles-thin`](../models/linkedin/search-profiles-thin.md) | Cheap people search: name/handle, headline, VANITY profile URL, location. No full profile or email - for full profiles per hit use… | about $0.036 per call |
| [`linkedin/user-detail`](../models/linkedin/user-detail.md) | Get a LinkedIn profile by username, including documented core profile fields such as name and headline. Use it to inspect a person's… | $0.028571 per call |
| [`linkedin/web-v2/company-posts`](../models/linkedin/web-v2/company-posts.md) | Returns posts from a LinkedIn organization page using the company URL. Supports ordering by top or recent posts and offset or token… | $0.05 per call |
| [`linkedin/web-v2/company-profile`](../models/linkedin/web-v2/company-profile.md) | Returns LinkedIn company profile details, including affiliated organizations, using a direct company page URL. | $0.008 per call (free daily quota) |
| [`linkedin/web-v2/job-detail`](../models/linkedin/web-v2/job-detail.md) | Returns detailed information for a specific LinkedIn job posting via its URL. Allows optional inclusion of required skills and hiring team… | $0.05 per call |
| [`linkedin/web-v2/post-comments`](../models/linkedin/web-v2/post-comments.md) | Returns comments for a specific LinkedIn post using its activity URN. Supports filtering by share URN, sorting by relevance or recency,… | $0.05 per call |
| [`linkedin/web-v2/post-detail`](../models/linkedin/web-v2/post-detail.md) | Returns content and metadata for a LinkedIn post or article using its web address. Works with both standard post and pulse article links. | $0.008 per call (free daily quota) |
| [`linkedin/web-v2/user-posts`](../models/linkedin/web-v2/user-posts.md) | Retrieves a member's posts, commented posts, or reacted posts using their profile URL. Supports filtering by activity type and paginating… | $0.05 per call |
| [`linkedin/web-v2/user-profile`](../models/linkedin/web-v2/user-profile.md) | Retrieves public profile details for a LinkedIn member. Input the full profile link to look up member information. | $0.008 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/ad", "url": "https://www.linkedin.com/ad-library/detail/1487405616"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
