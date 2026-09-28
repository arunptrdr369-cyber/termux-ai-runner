# 📑 Changelog

All notable changes to **Termux AI Runner** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [v0.1.0] - 2026-09-28
### Added
- Initial public release of **Termux AI Runner**.
- Setup script (`setup.sh`) that installs dependencies:
  - `Python`, `clang`, `cmake`, `git`, `wget`.
- Automatic compilation of **llama.cpp**.
- Runner script linked as `termux-run-model`.
- Beginner‑friendly CLI with flags:
  - `--download` for fetching models.
  - `--run` for executing models.
- Model manager with storage in `~/termux-ai-runner/models`.

---

## [Unreleased]
### Planned
- Support for ONNX models.
- Thread control and performance tuning options.
- Enhanced cleanup commands for model management.
- Workflow diagram and screenshots in README.

---
