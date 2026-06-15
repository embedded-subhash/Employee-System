import logging

logger = logging.getLogger("employee_system")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    "logs/application.log"
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)