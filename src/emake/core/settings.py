from pathlib import Path

import tomli

from typing import List, Optional

# https://stackoverflow.com/a/3405143
class SafeDict(dict):
    """Dictionary which cannot produce key errors."""

    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


class Settings:
    """User settings structure."""

    configure_args: List[str]
    configure_generator: Optional[str]

    build_jobs: Optional[int]
    build_copy_cc: bool

    def __init__(self, raw: SafeDict) -> None:
        self.configure_args = raw["configure"].get("args") or []
        self.configure_generator = raw["configure"].get("generator") or None

        self.build_jobs = raw["build"].get("jobs") or None
        self.build_copy_cc = raw["build"].get("copy_cc") or False


def default() -> Settings:
    """Load user settings from the default path(s)."""

    local_path = Path("emake.toml")
    if local_path.is_file():
        settings_path = local_path
    else:
        settings_path = Path.home().joinpath(".config", "emake.toml")

    try:
        with open(settings_path, "rb") as f:
            raw = tomli.load(f)
            raw = SafeDict(raw)
    except FileNotFoundError:
        raw = SafeDict()

    return Settings(raw)
