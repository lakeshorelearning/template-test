from loguru import logger
import sys
import os

logger.remove(0)
log_level = os.getenv("CONFIG_LOG_LEVEL", "INFO")
logger.add(sys.stderr, level=log_level)
