# Lunar Ridge

**Python** · **v0.1.0**

_Secure random password generator with configurable length and character sets_

---

## Features

- Cryptographically secure random generation (secrets module)
- Configurable length and number of passwords
- Optional exclusion of special characters

## Installation

```bash
git clone https://github.com/DevCode01/lunar-ridge.git
cd lunar-ridge
```

## Usage

```bash
./lunar-ridge.py --length 16 --count 5
```

## How it works

Uses Python's `secrets` module (cryptographically secure random) to draw each character from a mixed pool of lowercase, uppercase, digits and symbols. Symbols are excluded with `--no-symbols` for systems with strict password rules.

## Options

- `-l, --length N` - password length (default 16)
- `-n, --count N` - number of passwords to generate (default 1)
- `--no-symbols` - exclude special characters
- `-h, --help` - show usage

## Example

```bash
$ ./lunar-ridge.py --length 12 --count 2
X{8f$w2!pQkL
vZ~4bR@3nTdS
```

## Testing

```bash
bash tests/run.sh
```

Runs the build/syntax check (interactive/random/networked output isn't asserted exactly).

## License

MIT
