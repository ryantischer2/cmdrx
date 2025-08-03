# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2024-12-01

### Added
- Initial release of CmdRx
- Support for multiple LLM providers:
  - OpenAI (GPT-4, GPT-3.5-turbo)
  - Anthropic Claude (Claude-3 models)
  - Grok (xAI models)
  - Custom/on-premises endpoints
- Two input modes:
  - Standalone mode: `cmdrx command`
  - Piped mode: `command | cmdrx`
- Text-based user interface (TUI) for configuration
- Secure credential storage using system keyring
- Automated log file generation with timestamps
- Fix script generation with safety confirmations
- Command line interface with comprehensive options
- Cross-platform support (Linux, macOS)
- Package management support:
  - Debian/Ubuntu (apt)
  - Red Hat/Fedora (dnf)
  - macOS (Homebrew)
- Comprehensive documentation and man pages
- Unit tests and CI/CD pipeline
- MIT license

### Security
- API keys stored securely in system keyring
- No plain text credential storage
- HTTPS-only for remote API communications
- Input validation to prevent injection attacks
- Generated fix scripts include safety warnings

[Unreleased]: https://github.com/cmdrx/cmdrx/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/cmdrx/cmdrx/releases/tag/v0.1.0