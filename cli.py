import argparse
import sys

from .banner import animate_banner
from .engine import generate
from .masks import generate_mask
from .progress import progress
from .colors import CYAN, RESET


def write_stream(generator, output, limit):
    with open(output, "w", buffering=1024 * 1024) as f:
        for i, word in enumerate(generator, 1):
            f.write(word + "\n")
            if i % 1000 == 0:
                progress(i, limit)
    print(f"\n{CYAN}[+] Output written to {output}{RESET}")


def interactive_menu():
    while True:
        animate_banner()
        print("[1] Generate from words")
        print("[2] Generate from mask")
        print("[3] Exit")

        choice = input(">> ").strip()

        if choice == "1":
            words = input("Words (comma separated): ").split(",")
            limit = int(input("Limit: "))
            randomize = input("Randomize? [y/N]: ").lower() == "y"
            output = input("Output file [output.txt]: ") or "output.txt"

            write_stream(
                generate(words, limit, randomize=randomize),
                output,
                limit
            )

        elif choice == "2":
            mask = input("Mask (?l?l?d?d): ")
            limit = int(input("Limit: "))
            output = input("Output file [output.txt]: ") or "output.txt"

            write_stream(
                generate_mask(mask, limit),
                output,
                limit
            )

        elif choice == "3":
            sys.exit(0)


def main():
    if len(sys.argv) == 1:
        interactive_menu()
        return

    parser = argparse.ArgumentParser(description="AegisPassGen v2")
    sub = parser.add_subparsers(dest="command")

    g = sub.add_parser("generate")
    g.add_argument("-i", "--input", required=True)
    g.add_argument("-n", "--limit", type=int, default=100000)
    g.add_argument("-o", "--output", default="output.txt")
    g.add_argument("--random", action="store_true")
    g.add_argument("--seed", type=int)
    g.add_argument("--block-size", type=int, default=5000)

    m = sub.add_parser("mask")
    m.add_argument("mask")
    m.add_argument("-n", "--limit", type=int, default=100000)
    m.add_argument("-o", "--output", default="output.txt")

    args = parser.parse_args()

    if args.command == "generate":
        words = args.input.split(",")
        write_stream(
            generate(
                words,
                args.limit,
                randomize=args.random,
                seed=args.seed,
                block_size=args.block_size
            ),
            args.output,
            args.limit
        )

    elif args.command == "mask":
        write_stream(
            generate_mask(args.mask, args.limit),
            args.output,
            args.limit
        )


if __name__ == "__main__":
    main()
