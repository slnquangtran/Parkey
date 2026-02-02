# Changelog

All notable changes to Parkey will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2025-02-02

### Added

- Initial release of Parkey - Secure Password Manager
- Master password authentication (register & login)
- Encrypted storage for passwords using industry-standard cryptography
- GUI with login, register, and main menu
- Create, view, and edit password profiles
- Password generator
- Clean interface with custom backgrounds

### Requirements

- Python 3.8+
- Dependencies: `cryptography`, `Pillow` (see `requirements.txt`)

### How to run

From the repository root:

```bash
pip install -r requirements.txt
python parkey/main.py
```

Or from the `parkey` directory:

```bash
pip install -r requirements.txt
python main.py
```
