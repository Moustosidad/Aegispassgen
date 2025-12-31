# 🛡️ AegisPassGen

> **Advanced password wordlist generation engine for authorized security auditing**

AegisPassGen is a high-performance, modular password generation engine designed for **authorized security audits**, controlled penetration testing, and defensive cybersecurity research.

It focuses on **realistic, human-like password generation**, combining rule-based mutations, mask-based patterns, and hybrid logic — while maintaining a **low memory footprint** and a **professional CLI interface**.

---

## 🚀 Key Features

- 🔹 Advanced wordlist generation from custom inputs
- 🔹 Hashcat-style **mask-based generation**
- 🔹 Rule-based transformations (case, leetspeak, truncation, extension)
- 🔹 Hybrid engine (words + numbers + symbols)
- 🔹 Streaming generation (no large wordlists loaded into RAM)
- 🔹 Controlled randomness with reproducible seeds
- 🔹 Dynamic, hacker-style terminal banner
- 🔹 Terminal size detection and adaptive layout
- 🔹 Fully CLI-driven with interactive mode
- 🔹 Modular and extensible architecture
- 🔹 MIT licensed

---

## 🎯 Project Philosophy

Unlike cracking tools, **AegisPassGen does not perform attacks**.

Instead, it provides a **powerful and efficient generation layer** that can be piped into other tools or used independently to:

- simulate password risks
- test password policies
- generate targeted wordlists
- support security assessments

The separation between **generation** and **attack** ensures flexibility, performance, and responsible use.

---

## 🧠 How It Works

AegisPassGen builds password candidates using:

1. **Input tokens**  
   Names, years, keywords, or any custom strings.

2. **Character extraction**  
   Characters are decomposed and recombined logically.

3. **Rules engine**  
   Case changes, leetspeak, repetitions, truncation, extensions.

4. **Mask engine**  
   Patterns like `?l?l?d?d`, `?u?l?l?d`, etc.

5. **Streaming output**  
   Candidates are generated on-the-fly, not stored in memory.

---

## 🧪 Example Use Cases

- Internal password audits
- Red team / blue team simulations
- Security training and education
- Password policy evaluation
- Custom wordlist generation
- Cybersecurity research

---

## 📦 Installation

> Recommended: use a virtual environment

```bash
git clone https://github.com/YOUR_USERNAME/aegispassgen.git
cd aegispassgen
python3 -m venv venv
source venv/bin/activate
pip install .
