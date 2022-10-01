import jarior.producer
import loggers
import pathlib
logger_name = str(pathlib.Path(__file__).stem)
logger_dir= str(pathlib.Path(__file__).parent)
msg_foler = r"C:\code\python\msg"
file_foler = r"C:\code\python\files"
log = loggers.get_logger(logger_name=logger_name,logger_dir=logger_dir)
jarior.producer.config(msg_folder=msg_foler, file_folder=file_foler, age_of_msg_in_minutes=1)

