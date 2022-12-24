from emake.core.shell import call
from emake.core import settings

from typing import Optional


def build(build_dir: str, target: Optional[str]) -> None:
    """Perform the build via CMake."""

    command = ["cmake", "--build", build_dir]

    # Build a specific target if requested, otherwise build the default target
    # per CMake's standard behavior.
    if target:
        command += ["-t", target]

    user = settings.default()
    if jobs := user.build_jobs:
        command += ["-j", str(jobs)]

    call(command)
