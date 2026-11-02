# Add your API to SandBase

You can propose any public HTTP API. Once it is approved, every SandBase user can call it with their SandBase key. It also becomes available to AI agents through the SandBase CLI and MCP server.

## What you get

- **Distribution.** Your API gets a page in this catalog and a page on its platform list, and it appears on sandbase.ai. It is also discoverable through the [SandBase CLI / MCP server](https://github.com/sandbaseai/cli), which Claude Code, Codex, Cursor and 22 more AI clients use.
- **No integration work for your users.** Every SandBase user can call your API with their existing key and balance, using the same request format as every other capability.
- **Your price, shown openly.** The catalog shows your list price and links to your pricing page.

## How it works

1. **Open a pull request.** Copy [`_template/`](_template/) to `integrations/<vendor-slug>/<capability>/integration.yaml` and fill it in. The folder path must match `id`.
2. **Automatic checks.** CI validates the file against [`schema/integration.schema.json`](schema/integration.schema.json). It also checks that the `id` is new and that the file contains no credentials.
3. **Review.** A SandBase maintainer reviews the proposal, usually within a few business days, and contacts you through `contact` to arrange API access. **Never put keys or secrets in the pull request.**
4. **Approval and rollout.** Merging the pull request approves it. Merging starts an automated pipeline: SandBase registers the capability as disabled, verifies it with real calls, and then enables it.
5. **Live.** The capability appears in [`catalog/`](../catalog/) and on sandbase.ai with the next daily refresh. Users call it with `POST /v1/run` and `"model": "<id>"`.

If you would rather not write the file yourself, open an [integration request](../../../issues/new?template=integration-request.yml) and we will draft it with you.

## What makes a good proposal

- **A stable, documented API.** It should be served over HTTPS and return JSON.
- **An honest description** of what the API returns and its limits.
- **A real `output_example`**, redacted, with no personal data.
- **A public pricing page** in `pricing.source_url`. The `usd` value is your list price.
- **One capability per file.** Add several folders for several endpoints.

Supported today:
- Methods: `GET`, `POST`.
- Auth: `bearer`, `header`, `query`, `none`.
- Execution: sync, or async with a poll endpoint.

## Validate locally

```bash
pip install pyyaml jsonschema
python scripts/validate_integrations.py integrations/<vendor-slug>/<capability>/integration.yaml
```
