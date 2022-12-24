#!/usr/bin/env python3

"""
Usage: econf [-hRU] [-d DIR] [--] [<args> ...]

Arguments:
  args                  Additional configure arguments for CMake

Options:
  -R, --reconfigure     Reconfigure even if build setup is present
  -U, --ignore-user     Ignore user settings
  -d, --dir DIR         Custom build directory (default: `emake_build`)
  -h, --help            Show help and exit

"""

from emake.core.config import configure
from emake.core.make import build

from docopt import docopt

import os


def main():
    args = docopt(__doc__)

    build_dir = args["--dir"] or "emake_build"
    reconfigure = args["--reconfigure"]
    ignore_user = args["--ignore-user"]
    extra_args = args["<args>"]

    if not os.path.isdir(build_dir) or reconfigure:
        configure(build_dir, reconfigure, extra_args, ignore_user)


if __name__ == "__main__":
    main()
