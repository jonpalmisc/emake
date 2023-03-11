from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from benedict import benedict
from typing import Dict, List, Optional


def default() -> benedict:
    """Load user settings from the default path(s)."""

    settings_path = Path("emake.toml")
    if not settings_path.is_file():
        settings_path = Path.home().joinpath(".config", "emake.toml")

    try:
        with open(settings_path, "rb") as f:
            raw = tomllib.load(f)
    except FileNotFoundError:
        raw = {}

    return benedict(raw)
