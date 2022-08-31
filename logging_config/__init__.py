""" 3 Options to Configure Logging: dictConfig(), fileConfig(), or explicit logger + handler + formatter creation. """
import os

from definitions import Definitions

LOGGING_CONFIG_DICT = {
    # required keys.
    "version": 1,
    "disable_existing_loggers": False,
    # optional keys.
    "formatters": {  # creates Formatter objects.
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # required.
            "datefmt": "%Y-%m-%d %H:%M:%S",  # default value.
            "style": "%",  # %, {, or $. default is %.
            "validate": True,  # checks style and formats.
        }
    },
    "handlers": {  # creates Handler objects.
        "default": {
            "level": "INFO",
            "class": "logging.StreamHandler",  # required.
            "formatter": "standard",
            "stream": 'ext://sys.stdout',
        },
        "org_handler": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": os.path.join(Definitions.LOG_DIR, "org.log"),
            "maxBytes": 10000000,
            "backupCount": 5
        }
    },
    "loggers": {  # creates Logger objects.
        "__main__": {
            "handlers": ["default", "org_handler"],
            "level": "INFO",
            "propagate": True
        },
        "org_logger": {
            "handlers": ["org_handler"],
            "level": "INFO",
            "propagate": False
        }
    },
    "root": {  # default logger, basicConfig()
        "handlers": ["default", "org_handler"],
        "level": "INFO",
        "propagate": True
    }
}
