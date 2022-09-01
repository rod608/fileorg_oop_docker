""" running simple checks! """
import logging.config
import os

import logging_config
from definitions import Definitions

# main method; signifies a script
if __name__ == "__main__":
    # configure logging setup.
    logging.config.dictConfig(logging_config.LOGGING_CONFIG_DICT)
    logger = logging.getLogger("org_logger")
