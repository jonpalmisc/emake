import os
import subprocess
import sys
from typing import List


def call(command: List[str], quiet: bool = False) -> None:
    """Call (and echo) a shell command."""

    print(f"> {' '.join(command)}")

    if quiet:
        result = subprocess.call(command, stdout=open(os.devnull, "wb"))
    else:
        result = subprocess.call(command)

    if result != 0:
        sys.exit(result)
