import os
import time

from loguru import logger

base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger_path = os.path.join(base_directory, "app_logs")

if not os.path.exists(logger_path):
    os.makedirs(logger_path)

error_path = os.path.join(logger_path, f'{time.strftime("%d-%m-%Y")}_error.log')

logger.add(error_path, rotation="1:00", retention="10 days", enqueue=True)

__all__ = ["logger"]
