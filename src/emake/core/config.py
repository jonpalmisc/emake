from emake.core.shell import call
from emake.core import settings

from typing import List, Optional


def configure(
    build_dir: str,
    reconfigure: bool,
    extra_args: Optional[List[str]] = None,
    ignore_user: bool = False,
) -> None:
    """Configure the build setup with CMake."""

    command = ["cmake", "-S", ".", "-B", build_dir]
    if reconfigure:
        command += ["--fresh"]

    user = settings.default()

    if not ignore_user:
        if generator := user.configure_generator:
            command += ["-G", generator]

        command += user.configure_args

        if extra_args:
            command += extra_args

    call(command)
