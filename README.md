# 📤 maildir2mbox

**Convert Evolution-style Maildir folders to standard MBOX files.**

This tool scans a directory (like Evolution’s `~/.local/share/evolution/mail/local`) and exports each subfolder matching a given prefix into a clean, importable `.mbox` file — preserving email headers, encodings, and structure.

---

## ✨ Features

- Converts **Maildir** to **MBOX** with full fidelity
- Parses emails using Python's robust `email.parser`
- Accepts **folder prefixes** (e.g., `.gmail`) to process multiple folders at once
- Outputs one `.mbox` per folder
- Includes verbose logging option
- No dependencies beyond the Python standard library

---

## 🐍 Requirements

- Python 3.7 or newer
- Linux/macOS/WSL (tested on Debian + Evolution)

---

## 🛠️ Usage

```bash
python3 maildir2mbox.py \
  --maildir-root ~/.local/share/evolution/mail/local \
  --prefix .gmail \
  --output-dir ~/mbox-export \
  --verbose
```

### 👻 Author
Developed by Tiago “Bruxo” Almeida
Inspired by a real battle against Gmail storage quotas 🦴🔥