import logging

__msg_folder__: str = None
__file_folder__: str = None
__logger__: logging.Logger = None
__age_of_msg__: int = 1

import os.path
import datetime
import threading


def __get_all_files__(p_dir: str):
    ret = []
    for x in os.walk(p_dir):
        if os.path.isfile(x):
            ret += [x]
    return ret


def __get_utc_time_of_file__(file_path):
    dt = os.path.getmtime(file_path)
    return datetime.datetime.utcfromtimestamp(dt)


def __get_age_of_file_in_minutes__(file_path):
    create_time = __get_utc_time_of_file__(file_path)
    return (datetime.datetime.utcnow() - create_time).total_seconds() / 60


def __thead_clean_up__(logger: logging.Logger = None):
    def run():
        try:
            global __msg_folder__
            global __age_of_msg__
            files = __get_all_files__(__msg_folder__)
            for file in files:
                age = __get_age_of_file_in_minutes__(file)
                if age > __age_of_msg__:
                    os.remove(file)
                    if isinstance(logger, logging.Logger):
                        logger.info(f"Delete {file}")
        except Exception as e:
            if isinstance(logger, logging.Logger):
                logger.debug(e)
            else:
                print(e)
    try:
        if isinstance(logger, logging.Logger):
            logger.info(f"Clean up start any file older than {__age_of_msg__} minutes will be deleted")
        threading.Thread(target=run, args=()).start()
        if isinstance(logger, logging.Logger):
            logger.info(f"Clean up start any file older than {__age_of_msg__} minutes will be deleted")
    except Exception as e:
        if isinstance(logger, logging.Logger):
            logger.debug(e)
        else:
            raise e


def config(
        msg_folder: str,
        file_folder: str,
        age_of_msg_in_minutes: int = 1, logger: logging.Logger = None):
    """
    Set up a config
    :param msg_folder: The folder of msg
    :param file_folder: The folder of content file
    :param age_of_msg_in_minutes: Clean if the age of  msg log file older than
    :param logger:
    :return:
    """
    global __msg_folder__
    global __file_folder__
    global __logger__
    global __age_of_msg__
    __msg_folder__ = msg_folder
    __file_folder__ = file_folder
    __age_of_msg__ = age_of_msg_in_minutes
    __logger__ = logger
    if not os.path.isdir(__msg_folder__):
        os.makedirs(__msg_folder__)
    if not os.path.isdir(__file_folder__):
        os.makedirs(__file_folder__)
    return None
