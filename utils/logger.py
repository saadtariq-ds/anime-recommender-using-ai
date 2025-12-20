import os
import logging
from datetime import datetime

LOGS_DIRECTORY = "logs"
os.makedirs(LOGS_DIRECTORY, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIRECTORY, f"log_{datetime.now().strftime('%d_%m_%Y')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def get_logger(name):
    """Returns the configured logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
