import logging

def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    if not l.hasHandlers():
        l.addHandler(fileHandler)
        l.addHandler(streamHandler)    

def main():
    setup_logger('log1', '/disk1/eeoFiles/log_chk/log1.log')
    setup_logger('log2', '/disk1/eeoFiles/log_chk/log2.log')
    log1 = logging.getLogger('log1')
    log2 = logging.getLogger('log2')

    log1.info('Info for log 3!')
    log2.info('Info for log 4!')
    log1.error('Oh, no! Something went wrong 1!')

if '__main__' == __name__:
    main()