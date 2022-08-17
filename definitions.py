import os
import logging


class Definitions:
    """ Class-Level Attributes """
    DESKTOP_PATH = os.path.expanduser("~/Desktop")
    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
    LOG_DIR = PROJECT_PATH + "/logs"


print(Definitions.DESKTOP_PATH)
print(Definitions.PROJECT_PATH)
print(Definitions.LOG_DIR)
