#!/usr/bin/env python3

import argparse
from pathlib import Path

import oead


def parse_args():
    parser = argparse.ArgumentParser(description='Quick tool for yaz0 compression')
    parser.add_argument('--level', '-L', help="Compression level (default 7)", default=7, type=int)
    parser.add_argument('input', help="File to compress")
    parser.add_argument(
        'output',
        help="Where to output compressed file (default same folder with \"s\" extension prefix)",
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
        return
    out_file = Path(args.output) if args.output else in_file.with_suffix(f'.s{in_file.suffix[1:]}')
    if not out_file.parent.exists():
        out_file.parent.mkdir(parents=True, exist_ok=True)
    data = in_file.read_bytes()
    if data[0:4] == b'Yaz0':
        print(f'{in_file.name} is already yaz0 compressed')
        return
    out_file.write_bytes(
        oead.yaz0.compress(data, level=args.level)
    )


if __name__ == '__main__':
    main()
