import os
import subprocess
import sys
from typing import Dict, List


def call(
    command: List[str], quiet: bool = False, extra_env: Dict[str, str] = {}
) -> None:
    """Call (and echo) a shell command."""

    env_prefix = ""
    env = os.environ.copy()
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
