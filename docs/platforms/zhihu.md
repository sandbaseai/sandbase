# Zhihu API: 51 endpoints with pricing and code examples

Call 51 Zhihu endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`zhihu/answer-list`](../models/zhihu/answer-list.md) | Get answers for a Zhihu question with sorting and pagination controls. Use it to browse responses to a known question and continue through… | $0.013889 per call (free daily quota) |
| [`zhihu/search`](../models/zhihu/search.md) | Search Zhihu by keyword with optional result-type, sort, time-interval, topic-display, and offset controls. Use it to find relevant… | $0.027778 per call |
| [`zhihu/user-articles`](../models/zhihu/user-articles.md) | Get articles published by a Zhihu user with offset pagination and publish-time or upvote sorting. Use it to browse a creator's articles in… | $0.013889 per call (free daily quota) |
| [`zhihu/user-follow-collections`](../models/zhihu/user-follow-collections.md) | Get Zhihu collections followed by a user, with offset pagination. Use it to browse the collections associated with a known account's… | $0.013889 per call (free daily quota) |
| [`zhihu/user-follow-columns`](../models/zhihu/user-follow-columns.md) | Get Zhihu columns followed by a user, with offset pagination. Use it to browse the columns associated with a known account's follow… | $0.013889 per call (free daily quota) |
| [`zhihu/user-follow-topics`](../models/zhihu/user-follow-topics.md) | Get Zhihu topics followed by a user, with offset pagination. Use it to browse the topics associated with a known account's follow activity. | $0.013889 per call (free daily quota) |
| [`zhihu/user-followees`](../models/zhihu/user-followees.md) | Get accounts followed by a Zhihu user, with offset pagination. Use it to explore the outgoing connections of a known account. | $0.013889 per call (free daily quota) |
| [`zhihu/user-followers`](../models/zhihu/user-followers.md) | Get accounts that follow a Zhihu user, with offset pagination. Use it to explore the audience connections of a known account. | $0.013889 per call (free daily quota) |
| [`zhihu/user-included-articles`](../models/zhihu/user-included-articles.md) | Get the included-article records exposed for a Zhihu user, with offset pagination. Use it to browse that account's included-article list. | $0.013889 per call (free daily quota) |
| [`zhihu/user-info`](../models/zhihu/user-info.md) | Get the public profile for a Zhihu user identified by URL token. Use it to inspect an account found through Zhihu content or relationship… | $0.013889 per call (free daily quota) |
| [`zhihu/web/ai-search-stream`](../models/zhihu/web/ai-search-stream.md) | Returns streaming AI search results from Zhihu based on a query prompt. Supports conversational multi-turn sessions and chat modes. | $0.0075 per call (free daily quota) |
| [`zhihu/web/answer-detail`](../models/zhihu/web/answer-detail.md) | Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links. | $0.0015 per call (free daily quota) |
| [`zhihu/web/article-search-v3`](../models/zhihu/web/article-search-v3.md) | Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and… | $0.0015 per call (free daily quota) |
| [`zhihu/web/column-article-detail`](../models/zhihu/web/column-article-detail.md) | Returns detailed information and metadata for a specific Zhihu column article, including author profile details, using a provided article… | $0.0015 per call (free daily quota) |
| [`zhihu/web/column-articles`](../models/zhihu/web/column-articles.md) | Returns articles from a specific Zhihu column, including titles, content snippets, vote counts, and author profile details. | $0.0015 per call (free daily quota) |
| [`zhihu/web/column-comment-config`](../models/zhihu/web/column-comment-config.md) | Returns comment settings and options for a Zhihu column article based on the provided article identifier. | $0.0015 per call (free daily quota) |
| [`zhihu/web/column-recommend`](../models/zhihu/web/column-recommend.md) | Returns recommended similar columns and articles for a specified Zhihu article ID, with support for pagination limits and offsets. | $0.0015 per call (free daily quota) |
| [`zhihu/web/column-relationship`](../models/zhihu/web/column-relationship.md) | Returns interaction details and relationship metadata for a Zhihu column article, including endorsement reaction text and navigation… | $0.0015 per call (free daily quota) |
| [`zhihu/web/column-search-v3`](../models/zhihu/web/column-search-v3.md) | Searches Zhihu columns matching a specified query term. Returns matching column profiles, follower counts, article totals, and snippet… | $0.0015 per call (free daily quota) |
| [`zhihu/web/comment-v5`](../models/zhihu/web/comment-v5.md) | Get the comments on a Zhihu answer: comment text, author, time, like and reply counts, with sorting and pagination. | $0.0015 per call (free daily quota) |
| [`zhihu/web/ebook-search-v3`](../models/zhihu/web/ebook-search-v3.md) | Searches Zhihu for ebooks matching a query term. Returns publication details including commodity IDs, SKU IDs, and direct product links. | $0.0015 per call (free daily quota) |
| [`zhihu/web/hot-list`](../models/zhihu/web/hot-list.md) | Get the Zhihu hot list: trending questions with title, excerpt, heat, answer and follower counts, and links. | $0.0015 per call (free daily quota) |
| [`zhihu/web/hot-recommend`](../models/zhihu/web/hot-recommend.md) | Returns hot recommendation items and content snippets from Zhihu Web. Supports pagination through offset and page_number alongside an… | $0.0015 per call (free daily quota) |
| [`zhihu/web/pin-comments`](../models/zhihu/web/pin-comments.md) | Returns comments for a Zhihu pin, including author details, like counts, and reply counts. Supports sorting by score or newest timestamp. | $0.0015 per call (free daily quota) |
| [`zhihu/web/pin-detail`](../models/zhihu/web/pin-detail.md) | Retrieves the full content and details of a single Zhihu pin using its unique pin identifier. Returns parsed text blocks, links, and… | $0.0015 per call (free daily quota) |
| [`zhihu/web/preset-search`](../models/zhihu/web/preset-search.md) | Retrieves preset search recommendations and default placeholder queries from Zhihu Web. Returns trending search terms without requiring… | $0.0015 per call (free daily quota) |
| [`zhihu/web/question-answers`](../models/zhihu/web/question-answers.md) | Returns a list of answers for a specified Zhihu question. Supports pagination through cursor or offset parameters and sorting by time or… | $0.0015 per call (free daily quota) |
| [`zhihu/web/question-detail`](../models/zhihu/web/question-detail.md) | Retrieves question information on Zhihu using a question ID. Returns the question title, answer counts, comment counts, follower counts,… | $0.0015 per call (free daily quota) |
| [`zhihu/web/recommend-followees`](../models/zhihu/web/recommend-followees.md) | Returns a list of recommended users to follow on Zhihu. Access personalized author and contributor suggestions directly from Zhihu web. | $0.0015 per call (free daily quota) |
| [`zhihu/web/salt-search-v3`](../models/zhihu/web/salt-search-v3.md) | Returns Zhihu Salt column and chapter search results matching a specified keyword. Supports pagination with offset and limit parameters. | $0.0015 per call (free daily quota) |
| [`zhihu/web/scholar-search-v3`](../models/zhihu/web/scholar-search-v3.md) | Search Zhihu Scholar papers matching specified keywords and filters. Returns paper details including IDs, titles, highlight snippets, and… | $0.0015 per call (free daily quota) |
| [`zhihu/web/search-recommend`](../models/zhihu/web/search-recommend.md) | Returns recommended search queries and trending suggestions from Zhihu Web. Helps discover popular topics and keywords without providing… | $0.0015 per call (free daily quota) |
| [`zhihu/web/search-suggest`](../models/zhihu/web/search-suggest.md) | Returns search query suggestions and related topics from Zhihu based on a specified search keyword. | $0.0015 per call (free daily quota) |
| [`zhihu/web/sub-comment-v5`](../models/zhihu/web/sub-comment-v5.md) | Returns replies to a specific Zhihu comment. Supports pagination through limit and offset parameters alongside custom sorting options. | $0.0015 per call (free daily quota) |
| [`zhihu/web/topic-search-v3`](../models/zhihu/web/topic-search-v3.md) | Searches Zhihu topics by keyword and returns matching topic profiles, follower metrics, and highlighted text matches with pagination… | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-answers`](../models/zhihu/web/user-answers.md) | Returns answers posted by a specific Zhihu user based on their user token. Supports pagination and sorting results by creation date or… | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-articles`](../models/zhihu/web/user-articles.md) | Retrieves articles posted by a specific Zhihu author using their user identifier. Supports sorting by post date or upvotes alongside… | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-collections`](../models/zhihu/web/user-collections.md) | Returns collections curated by a specific Zhihu user using their user URL token. Supports pagination controls via limit and offset… | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-follow-collections`](../models/zhihu/web/user-follow-collections.md) | Returns collections followed by a specific Zhihu user using their account identifier. Supports pagination to browse through full… | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-follow-columns`](../models/zhihu/web/user-follow-columns.md) | Returns the list of columns followed by a specific Zhihu user. Supports pagination controls via limit and offset parameters. | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-follow-questions`](../models/zhihu/web/user-follow-questions.md) | Returns a list of questions followed by a specified Zhihu user. Supports pagination controls through page size and offset parameters. | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-follow-topics`](../models/zhihu/web/user-follow-topics.md) | Returns the list of topics followed by a specific Zhihu user. Filter and paginate results using user token, limit, and offset values. | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-followees`](../models/zhihu/web/user-followees.md) | Returns the list of accounts that a specific Zhihu user follows. Supports pagination through limit and offset parameters. | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-followers`](../models/zhihu/web/user-followers.md) | Retrieves a paginated list of followers for a specified Zhihu user profile. Supports offset and limit parameters for browsing through… | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-included-articles`](../models/zhihu/web/user-included-articles.md) | Returns articles included or featured by a specific Zhihu user. Filter results using pagination parameters alongside the target user… | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-info`](../models/zhihu/web/user-info.md) | Retrieves public profile metrics and details for a Zhihu user. Returns article counts, answer counts, follower totals, and user account… | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-pins`](../models/zhihu/web/user-pins.md) | Returns a list of pins or moments posted by a specific Zhihu user. Supports pagination controls using offset and limit parameters. | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-search-v3`](../models/zhihu/web/user-search-v3.md) | Search for Zhihu user profiles by query terms. Returns matching accounts along with follower numbers, article counts, and answer statistics. | $0.0015 per call (free daily quota) |
| [`zhihu/web/user-segments`](../models/zhihu/web/user-segments.md) | Returns highlighted text segments and line comments for a specified Zhihu member. Supports filtering by content type along with offset… | $0.0015 per call (free daily quota) |
| [`zhihu/web/video-list`](../models/zhihu/web/video-list.md) | Retrieves a paginated list of videos from the Zhihu web platform. Supports pagination controls through page size and offset index… | $0.0015 per call (free daily quota) |
| [`zhihu/web/video-search-v3`](../models/zhihu/web/video-search-v3.md) | Returns Zhihu video search results matching a specified keyword. Supports pagination using offset and limit parameters, and accepts a… | $0.0015 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/answer-list", "questionId": "19550225"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
