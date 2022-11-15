import logging

def get_logger():
    # Gets or creates a logger
    logger = logging.getLogger(__name__)  

    # set log level
    logger.setLevel(logging.INFO)

    # define file handler and set formatter
    file_handler = logging.FileHandler('/disk1/eeoFiles/log_chk/logfile.log', mode='w')
    formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)

    # add file handler to logger
    if not logger.hasHandlers():
     logger.addHandler(file_handler)
    
    return logger

logger = get_logger()
# Logs
logger.info('An info message')