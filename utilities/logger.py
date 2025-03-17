import logging


class Logs:
    def __init__(self):
        self.logger = logging
        self.logger.basicConfig(
            level=logging.DEBUG,  # Set logging level (DEBUG, INFO, etc.)
            format='%(asctime)s - %(levelname)s - %(message)s',  # Format with timestamp
            datefmt='%Y-%m-%d %H:%M:%S'  # Format the timestamp (e.g., '2025-03-17 12:00:00')
        )

    def info(self, message):
        return self.logger.info(message)

    def error(self, message):
        return self.logger.error(message)

    def warning(self, message):
        return self.logger.warning(message)

    def critical(self, message):
        return self.logger.critical(message)
