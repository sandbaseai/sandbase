# Similarweb API: 25 endpoints with pricing and code examples

Call 25 Similarweb endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`similarweb/ad-networks`](../models/similarweb/ad-networks.md) | Get the ad networks behind a website's display-ad traffic, with each network's traffic share and change over the selected months. | about $0.225 per call |
| [`similarweb/audience-interest`](../models/similarweb/audience-interest.md) | Get the other websites a site's audience also visits, with affinity and audience overlap scores. | about $0.375 per call |
| [`similarweb/audience-overlap`](../models/similarweb/audience-overlap.md) | Compare the audiences of up to 5 websites: unique visitors per site, overlapping visitors and the combined audience. | about $0.15 per call |
| [`similarweb/deduplicated-audience`](../models/similarweb/deduplicated-audience.md) | Get a website's deduplicated monthly audience across desktop and mobile web, with each platform's share. | about $0.525 per call |
| [`similarweb/demographics`](../models/similarweb/demographics.md) | Get the age and gender breakdown of a website's visitors for the selected period. | $0.6 per call |
| [`similarweb/keywords-overview`](../models/similarweb/keywords-overview.md) | Get search metrics for keywords: clicks, volume, CPC, competition, intent and SERP features such as AI Overviews. | about $1.275 per call |
| [`similarweb/marketing-channel-sources-legacy`](../models/similarweb/marketing-channel-sources-legacy.md) | Get a website's visits by marketing channel (direct, search, social, referrals, mail, display) month by month. | about $0.525 per call |
| [`similarweb/popular-pages`](../models/similarweb/popular-pages.md) | Get a website's most visited pages with each page's traffic share and change. | about $0.225 per call |
| [`similarweb/ppc-spend`](../models/similarweb/ppc-spend.md) | Get a website's estimated monthly paid-search (PPC) ad spend in USD. | about $0.075 per call |
| [`similarweb/ranking`](../models/similarweb/ranking.md) | Get a website's global, country and category traffic rank month by month. | about $0.15 per call |
| [`similarweb/referrals`](../models/similarweb/referrals.md) | Get the websites a site's referral traffic comes from, with visits, share and change for each referrer. | about $0.3 per call |
| [`similarweb/search-keyword-competitors`](../models/similarweb/search-keyword-competitors.md) | Get the websites that compete with a domain for the same search keywords, with a competition score and shared-keyword ratio. | about $0.075 per call |
| [`similarweb/search-landing-pages`](../models/similarweb/search-landing-pages.md) | Get the landing pages that receive a website's search traffic, with clicks, keyword counts and desktop/mobile split. | about $0.15 per call |
| [`similarweb/search-serp-players-aggregated`](../models/similarweb/search-serp-players-aggregated.md) | Get the websites that win clicks on search results for given keywords, with clicks, top URL and SERP features, aggregated over the period. | about $0.15 per call |
| [`similarweb/search-serp-players-timeseries`](../models/similarweb/search-serp-players-timeseries.md) | Get month-by-month clicks for the websites that appear on search results for given keywords. | about $0.075 per call |
| [`similarweb/search-website-keywords`](../models/similarweb/search-website-keywords.md) | Get the search keywords a website's search traffic comes from, with clicks, position, competition and search intent. | about $0.15 per call |
| [`similarweb/similar-sites`](../models/similarweb/similar-sites.md) | Get websites similar to a domain, with affinity score, category and global rank. The date range must span exactly 3 months. | about $0.375 per call |
| [`similarweb/subdomains`](../models/similarweb/subdomains.md) | Get a website's subdomains with each subdomain's share of traffic. | about $0.15 per call |
| [`similarweb/technologies`](../models/similarweb/technologies.md) | Get the technologies a website uses (analytics, advertising, CMS and more), with category and first-seen date. | $0.75 per call |
| [`similarweb/top-sites-ranking`](../models/similarweb/top-sites-ranking.md) | Get the top-ranked websites worldwide or in a category, ordered by traffic rank. | about $0.075 per call |
| [`similarweb/traffic-by-demographics-aggregated`](../models/similarweb/traffic-by-demographics-aggregated.md) | Get the traffic share of one visitor age group on a website for the selected period. | about $0.45 per call |
| [`similarweb/traffic-engagement`](../models/similarweb/traffic-engagement.md) | Get a website's traffic and engagement metrics month by month: visits, page views, visit duration, bounce rate and more. | about $0.075 per call |
| [`similarweb/website-top-geographies`](../models/similarweb/website-top-geographies.md) | Get the countries a website's traffic comes from, with share and visits for each country. | about $0.225 per call |
| [`similarweb/website-traffic-snapshot`](../models/similarweb/website-traffic-snapshot.md) | Get a one-month snapshot of a website's traffic: visits, visit duration, pages per visit and bounce rate. | $0.3 per call |
| [`similarweb/website-traffic-trend`](../models/similarweb/website-traffic-trend.md) | Get a website's monthly traffic trend for chosen metrics over a date range. | $0.45 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/ad-networks", "domain": "cnn.com", "end_date": "2026-09", "limit": 1, "start_date": "2026-09"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
