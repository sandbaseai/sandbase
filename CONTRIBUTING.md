# Contributing

Thanks for helping. Issues, pull requests, commit messages and review comments in this repository are in **English**.

## Ways to contribute

| You want to | Do this |
|---|---|
| Add your API to SandBase | Open a pull request under [`integrations/`](integrations/README.md) |
| Ask for a model or API we don't have | Open a [model or API request](../../issues/new?template=capability-request.yml) |
| Report a wrong field, schema or price | Open a [catalog issue](../../issues/new?template=catalog-issue.yml) with the model name |
| Improve an SDK, example or doc | Open a pull request |

## Generated files

`catalog/`, `docs/` (except hand-written guides) and `openapi/` are generated daily from the live API by `.github/workflows/refresh.yml`. Don't edit them by hand. Report the problem instead: we fix the source, and the next refresh picks up the fix.

## SDKs

| SDK | Test |
|---|---|
| `sdk/python` | `python -c "import sys; sys.path.insert(0, 'sdk/python'); import sandbase"` |
| `sdk/typescript` | `cd sdk/typescript && npm install && npm test` |
| `sdk/go` | `cd sdk/go && go vet ./... && go test ./...` |

The SDKs have no runtime dependencies. Please keep it that way. Unit tests must not call the live API.

## Commits and pull requests

- Use [Conventional Commits](https://www.conventionalcommits.org/): `feat(sdk-go): add Cost helper`, `fix(integrations): ...`, `docs: ...`.
- Keep each pull request to one change, and fill in the pull request template.
- Never commit API keys, tokens or personal data. CI runs a secret scan.

## Security

Report vulnerabilities privately. See [SECURITY.md](SECURITY.md).
