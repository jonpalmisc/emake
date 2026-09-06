from pathlib import Path

import typer

from emake.core.config import configure
from emake.core.make import build

app = typer.Typer(rich_markup_mode=None, pretty_exceptions_enable=False)


@app.command(help="Quickly build (and configure) a CMake project.")
def make(
    build_dir: str = typer.Option(
        "ebuild", "--dir", "-d", help="Build directory to use/create."
    ),
    target: str | None = typer.Argument(None, help="Target to build/run."),
) -> None:
    if not Path(build_dir).is_dir():
        configure(build_dir, False)

    build(build_dir, target)


def main() -> None:
    app()
