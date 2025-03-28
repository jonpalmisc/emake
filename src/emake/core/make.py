from emake.core.shell import call
from emake.core import settings

from pathlib import Path
import shutil
from typing import Optional


def build(build_dir: str, target: Optional[str]) -> None:
    """Perform the build via CMake."""

    command = ["cmake", "--build", build_dir]

    # Build a specific target if requested, otherwise build the default target
    # per CMake's standard behavior.
    if target:
        command += ["-t", target]

    user = settings.default()
    if jobs := user.build.jobs:
        command += ["-j", str(jobs)]

    # Move 'compile_commands.json' to project root if requested.
    build_cc_path = Path(build_dir).joinpath("compile_commands.json")
    should_move = user.build.copy_cc or user.build.move_cc
    if should_move and build_cc_path.is_file():
        dest_cc_path = Path(build_dir).parent.joinpath("compile_commands.json")
        shutil.move(str(build_cc_path), str(dest_cc_path))

    call(command)
