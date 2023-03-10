from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from benedict import benedict
from typing import Dict, List, Optional


class Settings:
    """User settings structure."""

    configure_args: List[str]
    configure_generator: Optional[str]
    configure_env: Dict[str, str]

    build_jobs: Optional[int]
    build_copy_cc: bool

    def __init__(self, raw: benedict) -> None:
        self.configure_args = raw.configure.args or []
        self.configure_generator = raw.configure.generator or None
        self.configure_env = raw.configure.env or {}

        self.build_jobs = raw.build.jobs or None
        self.build_copy_cc = raw.build.copy_cc or False


def default() -> Settings:
    """Load user settings from the default path(s)."""

    local_path = Path("emake.toml")
    if local_path.is_file():
        settings_path = local_path
    else:
        settings_path = Path.home().joinpath(".config", "emake.toml")

    try:
        with open(settings_path, "rb") as f:
            raw = tomllib.load(f)
            raw = benedict(raw)
    except FileNotFoundError:
        raw = benedict()

    return Settings(raw)
