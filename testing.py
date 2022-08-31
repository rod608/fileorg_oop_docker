""" running simple checks! """
import logging.config
import os

import logging_config
from definitions import Definitions

# main method; signifies a script
if __name__ == "__main__":
    # ensure the log directory exists.
    if not os.path.exists(Definitions.LOG_DIR):
        os.mkdir(Definitions.LOG_DIR)
        print("Directory now exists.")

    # configure logging setup.
    logging.config.dictConfig(logging_config.LOGGING_CONFIG_DICT)
    logger = logging.getLogger("org_logger")
    logger.warning("Test 2.")
