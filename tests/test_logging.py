""" Testing the current Logging setup. """
import os
import logging
import logging.config

import logging_config
from definitions import Definitions


def test_logger_setup() -> None:
    """ Configure logging & ensure it is set up correctly. """
    # Make sure the logs directory exists.
    if not os.path.exists(Definitions.LOG_DIR):
        os.mkdir(Definitions.LOG_DIR)

    assert os.path.exists(Definitions.LOG_DIR)

    # Configure logging.
    logging.config.dictConfig(logging_config.LOGGING_CONFIG_DICT)

    org_logger = logging.getLogger("org_logger")
    assert os.path.exists(os.path.join(Definitions.LOG_DIR, "org.log"))
    assert len(org_logger.handlers) == 2

    main_logger = logging.getLogger(__name__)
    assert __name__ != "__main__" and len(main_logger.handlers) == 0


def test_org_logger() -> None:
    """ Tests the logger named org_logger. """
    # Create the logs dir if it doesn't exist.
    logger = logging.getLogger("org_logger")
    log_path = os.path.join(Definitions.LOG_DIR, "org.log")

    # Test for the appropriate level.
    with open(log_path) as f:
        original_file_content: list[str] = f.readlines()
        num_lines = len(original_file_content)

    logger.debug("debug!")
    with open(log_path) as f:
        assert len(f.readlines()) == num_lines

    logger.info("info!")
    with open(log_path) as f:
        assert len(f.readlines()) == num_lines + 1

    logger.warning("warning!")
    with open(log_path) as f:
        assert len(f.readlines()) == num_lines + 2

    logger.error("error!")
    with open(log_path) as f:
        assert len(f.readlines()) == num_lines + 3

    logger.critical("critical!")
    with open(log_path) as f:
        assert len(f.readlines()) == num_lines + 4

    # End, delete the file.
    os.remove(log_path)
    assert not os.path.exists(log_path)
