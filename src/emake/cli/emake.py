#!/usr/bin/env python3

"""
Usage: emake [-h] [-d DIR] [<target>]

Arguments:
  target            Target to build

Options:
  -d, --dir DIR     Custom build directory (default: `emake_build`)
  -h, --help        Show help and exit

"""

from emake.core.config import configure
from emake.core.make import build

from docopt import docopt

from pathlib import Path


def main():
    args = docopt(__doc__)

    build_dir = args["--dir"] or "emake_build"
    if not Path(build_dir).is_dir():
        configure(build_dir, False)

    build(build_dir, args["<target>"])


if __name__ == "__main__":
    main()
