#!/usr/bin/env python3
# Secure random password generator using the secrets module.
import argparse
import secrets
import string


def generate(length, use_symbols):
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description="Generate secure random passwords")
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length (default: 16)")
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of passwords (default: 1)")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude special characters")
    args = parser.parse_args()

    if args.length < 4:
        print("Password length must be at least 4")
        return 1

    for _ in range(args.count):
        print(generate(args.length, not args.no_symbols))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
