""" 3 Options to Configure Logging: dictConfig(), fileConfig(), or explicit logger + handler + formatter creation. """
import logging
import logging.handlers
import os
from definitions import Definitions


def log_dict_config() -> dict:
    """ Configure logging via a dictionary of information. """
    log_dict = {
        # required keys.
        "version": 1,
        "disable_existing_loggers": False,
        # optional keys.
        "formatters": {  # creates Formatter objects.
            "standard": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # required.
                "datefmt": "%Y-%m-%d %H:%M:%S",  # default value.
                "style": "%",      # %, {, or $. default is %.
                "validate": True,  # checks style and formats.
            }
        },
        "handlers": {  # creates Handler objects.
            "default": {
                "level": logging.INFO,
                "class": logging.StreamHandler,  # required.
                "formatter": "standard",
                "stream": 'ext://sys.stdout',
            },
            "org_handler": {
                "level": logging.INFO,
                "class": logging.handlers.RotatingFileHandler,
                "formatter": "standard",
                "filename": os.path.join(Definitions.LOG_DIR, "org"),
                "maxbytes": 10000000,
                "backupCount": 5
            }
        },
        "loggers": {  # creates Logger objects.
            "__main__": {
                "handlers": ["default", "org_handler"],
                "level": logging.INFO,
                "propagate": True
            },
            "org_logger": {
                "handlers": ["org_handler"],
                "level": logging.INFO,
                "propagate": False
            }
        },
        "root": {  # default logger, basicConfig()
            "handlers": ["default", "org_handler"],
            "level": logging.INFO,
            "propagate": True
        }
    }

    return log_dict
