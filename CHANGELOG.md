# Changelog

All notable changes to this project are listed here.

## [Unreleased]

### Added
- Weekly external link report (`scripts/check_external_links.py`) that never fails the build and writes its results to the job summary.
- Offline link and image checker (`scripts/check_links.py`) using only the Python standard library.
- GitHub Actions CI workflow that runs the checker on every push and pull request.
- Dependabot configuration to keep GitHub Actions up to date.
- Contributing guide, pull request template, and `.editorconfig`.
