import datetime
import logging
from pathlib import Path

from framework.system._system_settings import SYSTEM_LOG_LEVEL

_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

# level_name_to_level = {
#     "CRITICAL": logging.CRITICAL,
#     "FATAL": logging.FATAL,
#     "ERROR": logging.ERROR,
#     "WARNING": logging.WARNING,
#     "WARN": logging.WARN,
#     "INFO": logging.INFO,
#     "DEBUG": logging.DEBUG,
#     "NOTSET": logging.NOTSET
# }


def get_file_handler():
    root_dir = Path(__file__).parent.parent.parent
    file_handler = logging.FileHandler(f"{root_dir}\\logs\\{datetime.date.today()}.log")
    file_handler.setLevel(SYSTEM_LOG_LEVEL)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(SYSTEM_LOG_LEVEL)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(SYSTEM_LOG_LEVEL)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
