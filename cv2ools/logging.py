import logging
import os

FORMAT = '[%(asctime)s][%(levelname)s][%(name)s] %(message)s'
DATE_FORMAT = '%Y-%m-%d_%H:%M:%S'

LEVEL_MAP = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'NOSET': logging.NOTSET,
}


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    level = os.getenv('LOG_LEVEL', 'INFO').upper()
    logger.setLevel(level)

    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(FORMAT, datefmt=DATE_FORMAT)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
