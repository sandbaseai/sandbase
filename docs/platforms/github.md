# GitHub API: 16 endpoints with pricing and code examples

Call 16 GitHub endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`github/issue-comments`](../models/github/issue-comments.md) | List the comments on a GitHub issue or pull request by its URL, oldest first, with each commenter's login, their relationship to the… | about $0.0012 per call |
| [`github/repository`](../models/github/repository.md) | Fetch a GitHub repository's metadata by URL (stars, forks, language, topics, license, and timestamps). | about $0.0012 per call |
| [`github/repository-contributors`](../models/github/repository-contributors.md) | List the people who have committed to a GitHub repository by repository URL, ordered by number of commits, with each contributor's login,… | about $0.0012 per call |
| [`github/repository-forks`](../models/github/repository-forks.md) | List the forks of a GitHub repository by repository URL, with each fork's owner, description, stars, language and last push. Sort by… | about $0.0012 per call |
| [`github/repository-issues`](../models/github/repository-issues.md) | List a GitHub repository's issues and pull requests by repository URL (GitHub lists pull requests as issues), with each one's author,… | about $0.0012 per call |
| [`github/repository-readme`](../models/github/repository-readme.md) | Get a GitHub repository's README by repository URL, as the Markdown text the maintainers wrote, with its file name, path and size. Use it… | about $0.0012 per call |
| [`github/search-issues`](../models/github/search-issues.md) | Search issues and pull requests across GitHub with GitHub's own search syntax (repo:, is:pr, is:issue, author:, label:, opened:...), with… | about $0.0024 per call |
| [`github/trending-developers`](../models/github/trending-developers.md) | List trending GitHub developers (rank, username, name, avatar, and their most popular repository), optionally filtered by programming… | about $0.0012 per call |
| [`github/trending-repositories`](../models/github/trending-repositories.md) | List GitHub Trending repositories (rank, stars, stars gained today, language, and description), filterable by language and time window. | about $0.0012 per call |
| [`github/user`](../models/github/user.md) | Fetch a GitHub user's public profile by handle (name, bio, company, location, followers, and repo counts). | about $0.0012 per call |
| [`github/user-activity`](../models/github/user-activity.md) | List a GitHub user's public contribution activity by handle (grouped monthly summaries of commits, pull requests, and issues with… | about $0.0012 per call |
| [`github/user-contributions`](../models/github/user-contributions.md) | Fetch a GitHub user's contribution graph for a year (total contributions plus per-day counts and heatmap intensity). | about $0.0012 per call |
| [`github/user-followers`](../models/github/user-followers.md) | List a GitHub user's followers by handle (each follower's login, type, avatar, and profile URL) with pagination. | about $0.0012 per call |
| [`github/user-following`](../models/github/user-following.md) | List the GitHub users a given user follows by handle (each account's login, type, avatar, and profile URL) with pagination. | about $0.0012 per call |
| [`github/user-pull-requests`](../models/github/user-pull-requests.md) | List a GitHub user's public pull requests by handle (title, repository, state, creation date, and URL) with optional date filtering and… | about $0.0012 per call |
| [`github/user-repositories`](../models/github/user-repositories.md) | List a GitHub user's public repositories (name, description, language, stars, and forks) with sorting and cursor pagination. | about $0.0012 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "github/issue-comments", "url": "https://github.com/openai/whisper/pull/1838"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
