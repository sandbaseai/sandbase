# Facebook API: 28 endpoints with pricing and code examples

Call 28 Facebook endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`facebook/ad-details`](../models/facebook/ad-details.md) | Look up a single Meta Ad Library ad by ID or URL and get the advertiser, creative text, call-to-action, platforms, and run dates as clean… | about $0.0012 per call |
| [`facebook/ad-details-full`](../models/facebook/ad-details-full.md) | Pull one Meta Ad Library ad with its creative: every carousel variant, image and video URL, headline, body, and call to action. | about $0.00462 per call |
| [`facebook/ad-transcript`](../models/facebook/ad-transcript.md) | Get the spoken-word transcript of a Meta Ad Library video ad by ad ID or URL. | about $0.0012 per call |
| [`facebook/ads-search`](../models/facebook/ads-search.md) | Search the Meta Ad Library by keyword and get matching ads (advertiser, creative text, CTA, platforms, and run dates) with cursor… | about $0.0011 per call |
| [`facebook/company-ads`](../models/facebook/company-ads.md) | List the Meta Ad Library ads a company is running by page ID or company name (creative text, format, platforms, and run dates) with cursor… | about $0.0011 per call |
| [`facebook/event-details`](../models/facebook/event-details.md) | Fetch full details for a single Facebook event by ID or URL (name, schedule, venue, hosts, and attendance) as normalized JSON. | about $0.0012 per call |
| [`facebook/events`](../models/facebook/events.md) | List public Facebook events for a city or place by its events-page URL (event name, date, venue, and attendance) as normalized JSON. | about $0.0012 per call |
| [`facebook/events-search`](../models/facebook/events-search.md) | Search public Facebook events by keyword and get structured event records (name, schedule, venue, pricing, and attendance) as normalized… | about $0.0012 per call |
| [`facebook/followers`](../models/facebook/followers.md) | List the public followers (or accounts followed) of any Facebook page or profile URL as normalized JSON records. | about $0.12 per call |
| [`facebook/group-posts`](../models/facebook/group-posts.md) | Fetch recent posts from any public Facebook group by URL: text, author, reactions, and comment counts. | about $0.0012 per call |
| [`facebook/marketplace`](../models/facebook/marketplace.md) | Search Facebook Marketplace listings by keyword near a location, filter by price, condition, delivery, recency, and availability, and get… | about $0.0012 per call |
| [`facebook/marketplace-item`](../models/facebook/marketplace-item.md) | Fetch full details for a single Facebook Marketplace listing by ID or URL (title, price, location, photos, and attributes) as normalized… | about $0.0012 per call |
| [`facebook/marketplace-location-search`](../models/facebook/marketplace-location-search.md) | Resolve a place name to Facebook Marketplace locations with coordinates and metadata as normalized JSON. | about $0.0012 per call |
| [`facebook/page-contact`](../models/facebook/page-contact.md) | Look up a Facebook Page's public contact details (email, phone, website, and address) by page URL or ID. | about $0.0012 per call |
| [`facebook/page-lookup`](../models/facebook/page-lookup.md) | Look up Facebook Pages and profiles by name with Facebook's own quick search. A name lookup that returns basic identity fields only: name,… | about $0.00975 per call |
| [`facebook/photos`](../models/facebook/photos.md) | Fetch recent photos posted by any public Facebook page or profile (image URLs, captions, and dimensions) as normalized JSON. | about $0.0012 per call |
| [`facebook/post`](../models/facebook/post.md) | Fetch a single Facebook post by URL with its text and engagement counts (likes, comments, shares, views). | about $0.0012 per call |
| [`facebook/post-comments`](../models/facebook/post-comments.md) | Get comments for a Facebook post ID with cursor pagination. Use it to review discussion associated with a known public post or continue… | $0.028571 per call |
| [`facebook/post-transcript`](../models/facebook/post-transcript.md) | Get the spoken-word transcript of any public Facebook video post by URL as normalized JSON. | about $0.0012 per call |
| [`facebook/profile`](../models/facebook/profile.md) | Fetch a Facebook page's public profile (likes, followers, category, about) by URL or handle. | about $0.0012 per call |
| [`facebook/profile-events`](../models/facebook/profile-events.md) | List upcoming and past events hosted by any public Facebook page by URL (name, schedule, venue, and host) as normalized JSON. | about $0.0012 per call |
| [`facebook/profile-id`](../models/facebook/profile-id.md) | Resolve the numeric Facebook profile ID behind a profile path such as "zuck", for use with endpoints that need a profile ID. | $0.028571 per call |
| [`facebook/profile-posts`](../models/facebook/profile-posts.md) | Get public posts for a Facebook profile ID with cursor pagination. Use it to browse a known profile's public posting history or continue… | $0.028571 per call |
| [`facebook/profile-reels`](../models/facebook/profile-reels.md) | List a Facebook page's reels by URL with cursor pagination (caption, view count, permalink, thumbnail). | about $0.0012 per call |
| [`facebook/search-companies`](../models/facebook/search-companies.md) | Search the Meta Ad Library for advertisers by keyword and get matching pages: page ID, category, verification, follower counts, and linked… | about $0.0011 per call |
| [`facebook/search-pages`](../models/facebook/search-pages.md) | Search Facebook Pages by keyword, optionally narrowed to a location, and get structured page profiles (name, category, followers, contact… | about $0.123 per call |
| [`facebook/search-post`](../models/facebook/search-post.md) | Search public Facebook posts by keyword with optional inclusive date-range filters and cursor pagination. Use it to find topic-related… | $0.028571 per call |
| [`facebook/search-posts`](../models/facebook/search-posts.md) | Search public Facebook posts by keyword, optionally filtered by location, and get structured post records (text, author, engagement). | about $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/ad-details"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
