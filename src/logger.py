import os
import logging

def setup_logger():
    log_dir = os.path.join(os.path.dirname(__file__), "logs")
    os.makedirs(log_dir, exist_ok=True)  #  Auto-create logs folder if missing

    log_file = os.path.join(log_dir, "inventory.log")

    logger = logging.getLogger("inventory_logger")
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
