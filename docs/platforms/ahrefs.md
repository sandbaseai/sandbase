# Ahrefs API: 38 endpoints with pricing and code examples

Call 38 Ahrefs endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`ahrefs/batch-analysis-batch-analysis`](../models/ahrefs/batch-analysis-batch-analysis.md) | Get Domain Rating, backlinks, and traffic metrics for up to 100 targets at once. | about $0.013545 per call |
| [`ahrefs/domain-rating`](../models/ahrefs/domain-rating.md) | Return the Ahrefs Domain Rating (0-100 authority score) and Ahrefs Rank for a target domain on a given date. 4xx/5xx are not charged. | $0.08 per call |
| [`ahrefs/keywords-explorer-matching-terms`](../models/ahrefs/keywords-explorer-matching-terms.md) | Find keyword ideas containing seed terms, with volume and difficulty. | about $0.01419 per call |
| [`ahrefs/keywords-explorer-overview`](../models/ahrefs/keywords-explorer-overview.md) | Get volume, difficulty, traffic potential, intent, and CPC for up to 100 keywords. | about $0.02709 per call |
| [`ahrefs/keywords-explorer-related-terms`](../models/ahrefs/keywords-explorer-related-terms.md) | Find keywords related to seed terms, with volume and difficulty. | about $0.01419 per call |
| [`ahrefs/keywords-explorer-search-suggestions`](../models/ahrefs/keywords-explorer-search-suggestions.md) | Get autocomplete-style keyword suggestions for seeds, with volume and CPC. | about $0.00774 per call |
| [`ahrefs/keywords-explorer-volume-by-country`](../models/ahrefs/keywords-explorer-volume-by-country.md) | Split a keyword's search volume across countries. | about $0.007095 per call |
| [`ahrefs/keywords-explorer-volume-history`](../models/ahrefs/keywords-explorer-volume-history.md) | Track a keyword's monthly search volume over time in one country. | about $0.00129 per call |
| [`ahrefs/metrics`](../models/ahrefs/metrics.md) | Return core Site Explorer metrics for a target domain on a given date: organic and paid keyword counts, top-3 keyword count, organic… | $0.08 per call |
| [`ahrefs/serp-overview-serp-overview`](../models/ahrefs/serp-overview-serp-overview.md) | Get the top organic results for a keyword with ratings, backlinks, and traffic. | about $0.0129 per call |
| [`ahrefs/site-explorer-ai-responses-count`](../models/ahrefs/site-explorer-ai-responses-count.md) | Count how often eight AI assistants cite a target in generated answers. | about $0.087075 per call |
| [`ahrefs/site-explorer-all-backlinks`](../models/ahrefs/site-explorer-all-backlinks.md) | List a target's backlinks with anchors, source ratings, and link attributes. | about $0.00645 per call |
| [`ahrefs/site-explorer-anchors`](../models/ahrefs/site-explorer-anchors.md) | Break down a target's backlinks by anchor text with referring-domain counts. | about $0.005805 per call |
| [`ahrefs/site-explorer-backlinks-stats`](../models/ahrefs/site-explorer-backlinks-stats.md) | Get a target's live and all-time backlink and referring-domain totals. | about $0.00774 per call |
| [`ahrefs/site-explorer-broken-backlinks`](../models/ahrefs/site-explorer-broken-backlinks.md) | List backlinks pointing at a target's broken (non-200) pages. | about $0.005805 per call |
| [`ahrefs/site-explorer-crawled-pages`](../models/ahrefs/site-explorer-crawled-pages.md) | List a target's pages known to the crawler with URL Rating and HTTP codes. | about $0.00645 per call |
| [`ahrefs/site-explorer-domain-rating`](../models/ahrefs/site-explorer-domain-rating.md) | Get a target's Domain Rating (0-100 link authority) and its global rank. | about $0.00129 per call |
| [`ahrefs/site-explorer-domain-rating-history`](../models/ahrefs/site-explorer-domain-rating-history.md) | Track a target's Domain Rating over time, one row per date bucket. | about $0.00129 per call |
| [`ahrefs/site-explorer-keywords-history`](../models/ahrefs/site-explorer-keywords-history.md) | Track a target's ranking keyword counts by position bucket over time. | about $0.00387 per call |
| [`ahrefs/site-explorer-linked-anchors-external`](../models/ahrefs/site-explorer-linked-anchors-external.md) | Break down a target's outbound external links by anchor text. | about $0.003225 per call |
| [`ahrefs/site-explorer-linked-anchors-internal`](../models/ahrefs/site-explorer-linked-anchors-internal.md) | Break down a target's internal links by anchor text. | about $0.00258 per call |
| [`ahrefs/site-explorer-linkeddomains`](../models/ahrefs/site-explorer-linkeddomains.md) | List domains a target links out to, with link and page counts. | about $0.00258 per call |
| [`ahrefs/site-explorer-metrics`](../models/ahrefs/site-explorer-metrics.md) | Get a target's organic and paid keywords, traffic, and cost estimates. | about $0.02838 per call |
| [`ahrefs/site-explorer-metrics-by-country`](../models/ahrefs/site-explorer-metrics-by-country.md) | Split a target's organic and paid keywords and traffic by country. | about $0.014835 per call |
| [`ahrefs/site-explorer-metrics-history`](../models/ahrefs/site-explorer-metrics-history.md) | Track a target's organic and paid traffic estimates over time. | about $0.013545 per call |
| [`ahrefs/site-explorer-organic-competitors`](../models/ahrefs/site-explorer-organic-competitors.md) | Find domains competing with a target in organic search, with keyword overlap. | about $0.00903 per call |
| [`ahrefs/site-explorer-organic-keywords`](../models/ahrefs/site-explorer-organic-keywords.md) | List keywords a target ranks for with position, volume, and traffic estimates. | about $0.01548 per call |
| [`ahrefs/site-explorer-outlinks-stats`](../models/ahrefs/site-explorer-outlinks-stats.md) | Get a target's outbound link totals: external, internal, and dofollow counts. | about $0.00258 per call |
| [`ahrefs/site-explorer-pages-by-backlinks`](../models/ahrefs/site-explorer-pages-by-backlinks.md) | List a target's pages ordered by backlink and referring-domain counts. | about $0.00516 per call |
| [`ahrefs/site-explorer-pages-by-internal-links`](../models/ahrefs/site-explorer-pages-by-internal-links.md) | List a target's pages ordered by incoming internal link counts. | about $0.001935 per call |
| [`ahrefs/site-explorer-pages-by-traffic`](../models/ahrefs/site-explorer-pages-by-traffic.md) | Bucket a target's pages into organic-traffic ranges with totals per range. | about $0.03612 per call |
| [`ahrefs/site-explorer-pages-history`](../models/ahrefs/site-explorer-pages-history.md) | Track how many of a target's pages rank in organic search over time. | about $0.00129 per call |
| [`ahrefs/site-explorer-paid-pages`](../models/ahrefs/site-explorer-paid-pages.md) | List a target's paid-search landing pages with traffic and ad counts. | about $0.008385 per call |
| [`ahrefs/site-explorer-refdomains`](../models/ahrefs/site-explorer-refdomains.md) | List domains linking to a target with Domain Rating and link counts. | about $0.00387 per call |
| [`ahrefs/site-explorer-refdomains-history`](../models/ahrefs/site-explorer-refdomains-history.md) | Track a target's referring-domain count over time. | about $0.00387 per call |
| [`ahrefs/site-explorer-top-pages`](../models/ahrefs/site-explorer-top-pages.md) | List a target's pages by estimated organic traffic and top keyword. | about $0.014835 per call |
| [`ahrefs/site-explorer-total-search-volume-history`](../models/ahrefs/site-explorer-total-search-volume-history.md) | Track total search volume of keywords a target ranks for over time. | about $0.007095 per call |
| [`ahrefs/site-explorer-url-rating-history`](../models/ahrefs/site-explorer-url-rating-history.md) | Track a target URL's rating over time, one row per date bucket. | about $0.00129 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/batch-analysis-batch-analysis", "targets": [{"url": "ahrefs.com"}]}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
