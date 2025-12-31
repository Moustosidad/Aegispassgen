import os
import sys
import time
import random
import shutil

from .colors import GREEN, CYAN, MAGENTA, RED, YELLOW, RESET, BOLD

GLITCH_CHARS = "▓▒░█<>/\\|#@$%&*"
DELAY = 0.015


ASCII_LARGE = [
" █████╗ ███████╗ ██████╗ ██╗███████╗",
"██╔══██╗██╔════╝██╔════╝ ██║██╔════╝",
"███████║█████╗  ██║  ███╗██║███████╗",
"██╔══██║██╔══╝  ██║   ██║██║╚════██║",
"██║  ██║███████╗╚██████╔╝██║███████║",
"╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝",
]

ASCII_SMALL = [
"A E G I S  P A S S  G E N",
"Advanced Password Engine",
]


def _clear():
    os.system("clear" if os.name == "posix" else "cls")


def _terminal_size():
    size = shutil.get_terminal_size(fallback=(80, 24))
    return size.columns, size.lines


def _center(line, width):
    if len(line) >= width:
        return line
    pad = (width - len(line)) // 2
    return " " * pad + line


def _glitch(line):
    out = ""
    for ch in line:
        if ch != " " and random.random() < 0.15:
            out += random.choice(GLITCH_CHARS)
        else:
            out += ch
    return out


def animate_banner():
    cols, rows = _terminal_size()
    large_mode = cols >= 80 and rows >= 24

    _clear()

    # ── GLITCH INTRO ─────────────────────────────
    if large_mode:
        for _ in range(5):
            _clear()
            print(GREEN + BOLD)
            for line in ASCII_LARGE:
                print(_center(_glitch(line), cols))
            print(RESET)
            time.sleep(0.08)

    _clear()

    # ── FINAL LOGO ───────────────────────────────
    print(GREEN + BOLD)
    logo = ASCII_LARGE if large_mode else ASCII_SMALL
    for line in logo:
        print(_center(line, cols))
        time.sleep(DELAY if large_mode else 0)
    print(RESET)

    # ── INFO PANEL ───────────────────────────────
    if large_mode:
        panel = [
            "╔══════════════════════════════════════════════════════╗",
            "║   A E G I S  ·  P A S S  ·  G E N   [ v2.0 ]          ║",
            "║                                                      ║",
            "║   ▸ Streaming Wordlist Engine                        ║",
            "║   ▸ Mask / Hybrid Generation                         ║",
            "║   ▸ Low Memory · High Throughput                     ║",
            "║                                                      ║",
            "╚══════════════════════════════════════════════════════╝",
        ]

        print(CYAN + BOLD)
        for line in panel:
            print(_center(line, cols))
        print(RESET)

        print(MAGENTA)
        print(_center("[+] Mode    : WORDLIST · MASK · HYBRID", cols))
        print(_center("[+] Engine  : STREAMING PIPELINE", cols))
        print(_center("[+] Target  : AUTHORIZED SECURITY AUDITS", cols))
        print(RESET)

        print(RED + BOLD)
        print(_center("!!!  AUTHORIZED USE ONLY  !!!", cols))
        print(RESET)
    else:
        print(YELLOW)
        print(_center("AUTHORIZED SECURITY USE ONLY", cols))
        print(RESET)


# El resto del programa solo llama a esto
