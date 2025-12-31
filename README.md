# 🛡️ AegisPassGen

Advanced password wordlist generation engine for authorized security auditing

AegisPassGen is a high-performance, modular password wordlist generation engine designed for authorized security audits, controlled penetration testing, and defensive cybersecurity research.

The project focuses on realistic, human-like password generation, combining rule-based mutations, mask-based patterns, and hybrid logic, while maintaining a low memory footprint and a professional command-line interface.

------------------------------------------------------------

KEY FEATURES

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

------------------------------------------------------------

PROJECT PHILOSOPHY

Unlike password cracking tools, AegisPassGen DOES NOT perform attacks.

Instead, it provides a powerful and efficient password generation layer that can be:

- used independently
- piped into other tools
- integrated into existing security workflows

This strict separation between generation and attack ensures:

- responsible use
- higher flexibility
- better performance
- easier integration

------------------------------------------------------------

HOW AEGISPASSGEN WORKS

1. Input Tokens  
User-provided words, names, years, keywords, or arbitrary strings.

2. Character Extraction  
Tokens are decomposed into characters to allow logical recombination.

3. Rules Engine  
Applies transformations such as:
- uppercase / lowercase variations
- leetspeak substitutions
- repetitions
- truncation and extension

4. Mask Engine  
Generates candidates based on patterns such as:
?l?l?d?d  
?u?l?l?d  

5. Streaming Output  
Candidates are generated on-the-fly, avoiding large memory usage.

------------------------------------------------------------

EXAMPLE USE CASES

- Internal password audits
- Red team / blue team simulations
- Security awareness training
- Password policy evaluation
- Custom wordlist generation
- Cybersecurity research and education

------------------------------------------------------------

INSTALLATION (OFFICIAL METHOD)

The official installation method is via Git clone.

Repository:
https://github.com/Moustosidad/Aegispassgen.git

Installation steps:

git clone https://github.com/Moustosidad/Aegispassgen.git
cd Aegispassgen
python3 -m pip install .

------------------------------------------------------------

USAGE

Interactive mode:

aegispassgen

CLI example:

aegispassgen --words David Gayan Futbol --numbers 2009 --max 100000 --output wordlist.txt

Mask-based generation:

aegispassgen --mask ?l?l?d?d

------------------------------------------------------------

MASK SYNTAX

?l  lowercase letters (a–z)  
?u  uppercase letters (A–Z)  
?d  digits (0–9)  
?s  symbols  

Example:
?u?l?l?d?d → Abc12

------------------------------------------------------------

PROJECT STRUCTURE

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

------------------------------------------------------------

LEGAL DISCLAIMER

This software is intended exclusively for authorized security testing, educational purposes, and research.

The author assumes no responsibility for misuse.
Using this tool against systems without explicit authorization may be illegal and unethical.

------------------------------------------------------------

LICENSE

MIT License.
See the LICENSE file for full license text.

------------------------------------------------------------

FINAL NOTES

AegisPassGen is designed to be:

- clean
- extensible
- efficient
- professional
- responsible

Contributions, reviews, and security-focused discussions are welcome.
