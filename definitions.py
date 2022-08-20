import os
import logging


class Definitions:
    """ Class-Level Attributes """
    DESKTOP_PATH = os.path.expanduser("~/Desktop")
    DOCUMENTS_PATH = os.path.expanduser("~/Documents")
    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
    LOG_DIR = PROJECT_PATH + "/logs"
