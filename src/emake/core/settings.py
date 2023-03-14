from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from benedict import benedict
from typing import Union, Dict, Any


def __get_opts(config: Path) -> Union[Dict[str, Any], Dict]:
    """ Get values from given TOML configuration. """

    try:
        with config.open("rb") as f:
            data = tomllib.load(f)
    except FileNotFoundError:
        data = {}

    return data


def default() -> benedict:
    """Load user settings from the default path(s)."""

    local_path = Path("emake.toml")
    global_path = Path.home().joinpath(".config", "emake.toml")

    local_opts = __get_opts(local_path)
    global_opts = __get_opts(global_path)

    defaults = benedict(local_opts)
    defaults.merge(global_opts, concat=True)

    return defaults
