# 🛡️ AegisPassGen

> Advanced password wordlist generation engine for authorized security auditing

AegisPassGen is a high-performance, modular password wordlist generation engine designed for authorized security audits, controlled penetration testing, and defensive cybersecurity research.

The project focuses on realistic, human-like password generation, combining rule-based mutations, mask-based patterns, and hybrid logic, while maintaining a low memory footprint and a professional command-line interface.

---

## Key Features

- Advanced wordlist generation from custom user inputs
- Hashcat-style mask-based generation
- Rule-based transformations (case changes, leetspeak, truncation, extension)
- Hybrid engine (words + numbers + symbols)
- Streaming generation (no large wordlists stored in RAM)
- Controlled randomness with reproducible seeds
- Dynamic hacker-style terminal banner
- Automatic terminal size detection
- Fully CLI-driven with interactive mode
- Modular and extensible architecture
- MIT licensed

---

## Project Philosophy

Unlike password cracking tools, AegisPassGen does NOT perform attacks.

Instead, it provides a powerful and efficient password generation layer that can be:

- used independently
- piped into other tools
- or integrated into existing security workflows

This strict separation between generation and attack ensures:

- responsible use
- higher flexibility
- better performance
- easier integration

---

## How AegisPassGen Works

Password candidates are generated through multiple logical stages:

1. Input Tokens  
   User-provided words, names, years, keywords, or any arbitrary strings.

2. Character Extraction  
   Tokens are decomposed into characters to allow logical recombination.

3. Rules Engine  
   Applies transformations such as:
   - uppercase / lowercase variations
   - leetspeak substitutions
   - repetitions
   - truncation and extension

4. Mask Engine  
   Generates candidates based on predefined patterns like:
   ?l?l?d?d
   ?u?l?l?d

5. Streaming Output  
   Candidates are generated on-the-fly, avoiding large memory usage.

---

## Example Use Cases

- Internal password audits
- Red team / blue team simulations
- Security awareness training
- Password policy evaluation
- Custom wordlist generation
- Cybersecurity research and education

---

## Installation (Official Method)

AegisPassGen is designed to be installed using pipx.

Why pipx?

- No manual virtual environments required
- No system Python pollution
- Isolated and secure execution
- Widely used in professional CLI tools

Requirements:

- Python 3.9 or newer
- pipx

Install pipx (Debian/Ubuntu example):

sudo apt install pipx
pipx ensurepath

Install AegisPassGen:

pipx install aegispassgen

---

## Usage

Interactive Mode:

aegispassgen

CLI Example:

aegispassgen --words potato  --numbers 897q --max 100000 --output wordlist.txt

Mask-Based Generation:

aegispassgen --mask ?l?l?d?d

---

## Mask Syntax

Symbol | Description
------ | -----------
?l     | lowercase letters (a–z)
?u     | uppercase letters (A–Z)
?d     | digits (0–9)
?s     | symbols

Example:

?u?l?l?d?d → Abc12

---

## Project Structure

aegispassgen/
├── aegispassgen/
│   ├── banner.py
│   ├── cli.py
│   ├── engine.py
│   ├── rules.py
│   ├── masks.py
│   ├── progress.py
│   └── colors.py
├── README.md
├── LICENSE
├── setup.cfg
└── pyproject.toml

---

## Legal Disclaimer

This software is intended exclusively for authorized security testing, educational purposes, and research.

The author assumes no responsibility for misuse. Using this tool against systems without explicit authorization may be illegal and unethical.

---

## License

MIT License. See the LICENSE file for full license text.

---

## Final Notes

AegisPassGen is designed to be:

- clean
- extensible
- efficient
- professional
- responsible

Contributions, reviews, and security-focused discussions are welcome.
