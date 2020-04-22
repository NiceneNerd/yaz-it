#!/usr/bin/env python3

import argparse
from pathlib import Path

import oead


def parse_args():
    parser = argparse.ArgumentParser(description='Quick tool for yaz0 decompression')
    parser.add_argument('input', help="File to decompress")
    parser.add_argument(
        'output',
        help="Where to output decompressed file (default same folder without extension prefix)",
        nargs='?',
        default=None,
        type=str
    )
    return parser.parse_args()


def main():
    args = parse_args()
    in_file = Path(args.input)
    if not in_file.exists():
        print(f'{in_file} could not be found')
    out_file = Path(args.output) if args.output else in_file.with_suffix(f'.{in_file.suffix[2:]}')
    if not out_file.parent.exists():
        out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_bytes(
        oead.yaz0.decompress(in_file.read_bytes())
    )


if __name__ == '__main__':
    main()
