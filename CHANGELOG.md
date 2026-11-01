# Changelog

All notable changes to this project are listed here.

## [Unreleased]

### Added
- Release workflow that creates a GitHub Release from a version tag (for example `v1.0.0`) using the notes in this file.
- Unit tests for both link checkers (`tests/`), run with pytest in CI.
- Coverage summary written to the GitHub job summary.
- Weekly external link report (`scripts/check_external_links.py`) that never fails the build and writes its results to the job summary.
- Offline link and image checker (`scripts/check_links.py`) using only the Python standard library.
- GitHub Actions CI workflow that runs the checker on every push and pull request.
- Dependabot configuration to keep GitHub Actions up to date.
- Contributing guide, pull request template, and `.editorconfig`.
