"""parse config file"""

from sys import version_info
from typing import Any

CONFIG_PATH = "config.toml"

if version_info.major == 3 and version_info.minor >= 11:
    import tomllib

    with open(CONFIG_PATH, "br", encoding="utf-8") as f:
        _config = tomllib.load(f)
else:
    import toml

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        _config = toml.load(f)


def get_config() -> dict[str:Any]:
    """get config data"""
    return _config
