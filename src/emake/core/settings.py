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

    def __init__(self, raw: SafeDict) -> None:
        self.configure_args = raw["configure"]["args"] or []
        self.configure_generator = raw["configure"]["generator"] or None

        self.build_jobs = raw["build"]["jobs"] or None


def default() -> Settings:
    """Load user settings from the default path(s)."""

    try:
        with open("emake.toml", "rb") as f:
            raw = tomli.load(f)
            raw = SafeDict(raw)
    except FileNotFoundError:
        raw = SafeDict()

    return Settings(raw)
