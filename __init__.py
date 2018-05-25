import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
logger = logging.getLogger()
handler = logging.StreamHandler()
