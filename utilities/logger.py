import logging


class Logs:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def info(self, message):
        return self.logger.info(message)

    def error(self, message):
        return self.logger.error(message)

    def warning(self, message):
        return self.logger.warning(message)

    def critical(self, message):
        return self.logger.critical(message)
