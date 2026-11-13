# Spotify API: 7 endpoints with pricing and code examples

Call 7 Spotify endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`spotify/album`](../models/spotify/album.md) | Fetch a Spotify album's tracklist, play counts, label, and release details by album URL or ID. | about $0.0012 per call |
| [`spotify/artist`](../models/spotify/artist.md) | Fetch a Spotify artist's discography (albums, singles, top tracks) and metadata by artist URL or ID. | about $0.0012 per call |
| [`spotify/play-count`](../models/spotify/play-count.md) | Fetch stream counts and stats for a Spotify track, album, or artist URL. | about $0.0022 per call |
| [`spotify/podcast`](../models/spotify/podcast.md) | Fetch a Spotify podcast show's name, publisher, description, rating, and topics by show URL or ID. | about $0.0012 per call |
| [`spotify/podcast-episodes`](../models/spotify/podcast-episodes.md) | List a Spotify podcast show's episodes with titles, durations, descriptions, and release dates by show URL or ID. | about $0.0012 per call |
| [`spotify/search`](../models/spotify/search.md) | Search Spotify for matching tracks, albums, artists, podcasts, and playlists by keyword. | about $0.0012 per call |
| [`spotify/track`](../models/spotify/track.md) | Fetch a Spotify track's play count, popularity, duration, and album details by track URL or ID. | about $0.0012 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "spotify/album"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
