import os
import subprocess
import sys


def call(
    command: list[str], quiet: bool = False, extra_env: dict[str, str] | None = None
) -> None:
    """Call (and echo) a shell command."""

    env = os.environ.copy()

    if extra_env:
        env.update(extra_env)
        env_prefix = " ".join(f"{k}=`{v}`" for k, v in extra_env.items()) + " "
    else:
        env_prefix = ""

    print(f"> {env_prefix}{' '.join(command)}")

    try:
        subprocess.run(
            command,
            env=env,
            check=True,
            stdout=subprocess.DEVNULL if quiet else None,
            stderr=None,
        )
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
