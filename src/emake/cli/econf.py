#!/usr/bin/env python3

"""
Usage: econf [-hrRU] [-d DIR] [--] [<args> ...]

Arguments:
  args                  Additional configure arguments for CMake

Options:
  -r, --reconfigure     Reconfigure even if build setup is present
  -R, --remove          Remove build directory before reconfiguring
  -U, --ignore-user     Ignore user settings
  -d, --dir DIR         Custom build directory (default: `ebuild`)
  -h, --help            Show help and exit

"""

import os
import shutil

import typer

from emake.core.config import configure

app = typer.Typer(rich_markup_mode=None)


@app.command(help="Quickly configure a CMake project.")
def conf(
    build_dir: str = typer.Option(
        "ebuild", "--dir", "-d", help="Build directory to use/create."
    ),
    reconfigure: bool = typer.Option(
        False,
        "-r",
        "--reconfigure",
        help="Reconfigure the project even if a build directory is already present.",
    ),
    remove: bool = typer.Option(
        False,
        "-R",
        "--remove",
        help="Remove the build directory & forcefully reconfigure the project.",
    ),
    ignore_user: bool = typer.Option(
        False, "-U", "--ignore-user", help="Ignore global user settings/defaults."
    ),
    extra_args: list[str] = typer.Argument(  # noqa: B008
        [], help="Extra arguments to pass to CMake upon configuration."
    ),
):
    if os.path.isdir(build_dir) and remove:
        shutil.rmtree(build_dir)
    if not os.path.isdir(build_dir) or reconfigure:
        configure(build_dir, reconfigure, extra_args, ignore_user)


def main():
    app()
