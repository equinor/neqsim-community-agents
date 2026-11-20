# Python quality checks

For changes in this repository, use `uv sync --locked`, install the local hook
with `uv run pre-commit install`, and run
`uv run pre-commit run --files <changed-files>` plus relevant tests before
handover. The hooks run Ruff linting and Black formatting.

When an agent edits Python in a target repository:

- Follow that repository's Ruff configuration and pre-commit hooks.
- Run its documented Ruff checks and formatter on changed files, plus relevant
  tests, before handing over changes.
- Fix findings introduced by the changes. Do not weaken rules, add blanket
  suppressions, or bypass hooks to make checks pass.
- Report unrelated existing failures explicitly rather than claiming success.

## Portable paths and delegation

Never bake an author's absolute checkout, interpreter, EOS or task path into
code or prompts. Use explicit inputs, documented environment variables,
workspace-relative discovery or installed resources; validate configured paths
and report missing inputs instead of silently substituting another model.
Pass resolved absolute paths, the selected interpreter and this portability
requirement to every delegated agent. A plugin installation needs no checkout.
