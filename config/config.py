"""parse config file"""

from sys import version_info
from pathlib import Path

CONFIG_PATH = "config.toml"


def get_config(path: str = CONFIG_PATH):
    """get config data"""
    if version_info.major == 3 and version_info.minor >= 11:
        # import tomllib
        pass
    else:
        import toml

        with Path(path).open("r") as f:
            return toml.load(f)

