import logging
import os
from datetime import datetime

os.makedirs("logs",exist_ok=True)

def get_logger(name):
    log_file=datetime.now().strftime("logs/%Y-%m-%d_%H-%M-%S.log")
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh=logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)

        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger