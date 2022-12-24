from emake.core.shell import call

def configure(build_dir: str, reconfigure: bool) -> None:
    """Configure the build setup with CMake."""

    command = ["cmake", "-S", ".", "-B", build_dir]
    if reconfigure:
        command += ["--fresh"]

    call(command)
