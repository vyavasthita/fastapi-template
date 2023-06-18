import os
import logging
import logging.config
from app.dependencies.config_dependency import get_settings


class ApiLogger:
    __instance = None

    @staticmethod 
    def get_instance():
        """ Static access method. """
        if ApiLogger.__instance is None:
            ApiLogger()

        return ApiLogger.__instance

    def __init__(self):
        if ApiLogger.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ApiLogger.__instance = self

            self.initialize_logging()
            
            self.logger = logging.getLogger(__name__)
    
    def initialize_logging(self):
        logging.config.fileConfig(
            fname=get_settings().LOG_CONFIG_FILE, 
            disable_existing_loggers=False, 
            defaults={'log_file_name' : os.path.join(get_settings().LOGS_DIR, get_settings().LOG_FILE_NAME)}
        )

    @staticmethod
    def log_debug(log_message):
        ApiLogger.get_instance().logger.debug(log_message)

    @staticmethod
    def log_info(log_message):
        ApiLogger.get_instance().logger.info(log_message)

    @staticmethod
    def log_warning(log_message):            
        ApiLogger.get_instance().logger.warn(log_message)

    @staticmethod
    def log_error(log_message, exc_info=False):
        ApiLogger.get_instance().logger.error(log_message, exc_info=exc_info)

    @staticmethod
    def log_critical(log_message, exc_info=False):
        ApiLogger.get_instance().logger.critical(log_message, exc_info=exc_info)