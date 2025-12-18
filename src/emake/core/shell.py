import os
import subprocess
import sys


def call(
    command: list[str], quiet: bool = False, extra_env: dict[str, str] | None = None
) -> None:
    """Call (and echo) a shell command."""

    env_prefix = ""
    env = os.environ.copy()

    if extra_env:
        for k, v in extra_env.items():
            env_prefix += k + "=" + f"`{v}` "
            env[k] = v

    print(f"> {env_prefix}{' '.join(command)}")

    if quiet:
        result = subprocess.call(command, stdout=open(os.devnull, "wb"), env=env)
    else:
        result = subprocess.call(command, env=env)

    if result != 0:
        sys.exit(result)
