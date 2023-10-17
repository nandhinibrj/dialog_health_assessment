import json
import os
from pathlib import Path
from typing import Dict


def read_config():
    file_name = (
        str(Path(__file__).parent.parent)
        + os.sep
        + "config"
        + os.sep
        + "settings"
        + os.sep
        + "dev_config.json"
    )
    with open(file_name, "r") as config:
        return json.load(config)


def get_config(name: str):
    return read_config()[name]


class APPSettings:
    CONFIG = get_config("MAIN_CONFIG")
    APP_NAME = CONFIG["NAME"]
    APP_DESCRIPTION = CONFIG["DESCRIPTION"]
    APP_VERSION = CONFIG["API_VERSION"]
    APP_VERSION_PATH = CONFIG["API_VERSION_PATH"]
    APP_HOST = CONFIG["HOST"]
    APP_PORT = CONFIG["PORT"]
    APP_CORS_ORIGIN = CONFIG["CORS_ORIGIN"]
    APP_CORS_ALLOWED_METHODS = CONFIG["CORS_ALLOWED_METHODS"]
    APP_CORS_ALLOWED_HEADERS = CONFIG["CORS_ALLOWED_HEADERS"]


class DBSettings:
    CONFIG = get_config("DATABASE_CONFIG")
    SQL_ALCHEMY_URL = CONFIG["SQLALCHEMY_URL"]
