import logging
import os.path


def get_logger(logger_name:str, logger_dir:str)-> logging.Logger:
    # create logger for prd_ci
    log = logging.getLogger(logger_name)
    log.setLevel(level=logging.INFO)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    full_log_dir= os.path.join(logger_dir,logger_name)
    if not os.path.isdir(full_log_dir):
        os.makedirs(full_log_dir)
    full_log_file = os.path.join(full_log_dir,"log.txt")
    fh = logging.FileHandler(full_log_file)
    fh.setLevel(level=logging.DEBUG)
    fh.setFormatter(formatter)


    log.addHandler(fh)

    return log