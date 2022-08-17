import logging
import os

logging.basicConfig(level=logging.DEBUG)


# # Custom Handlers
# format_handler = logging.FileHandler(os.environ["MY_BASEPATH"] + "format.log")
# org_handler = logging.FileHandler("organization.log")
#
# # Custom Formatters. Add to handlers.
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# format_handler.setFormatter(formatter)
# org_handler.setFormatter(formatter)

# test a log.
# test_logger = logging.getLogger(__name__)
# test_logger.addHandler(format_handler)
# test_logger.debug("hi")
