import os.path
import uuid

import jarior.producer
import loggers
import pathlib
logger_name = str(pathlib.Path(__file__).stem)
logger_dir= str(pathlib.Path(__file__).parent)
msg_foler = r"C:\code\python\msg"
file_foler = r"C:\code\python\files"
log = loggers.get_logger(logger_name=logger_name,logger_dir=logger_dir)
jarior.producer.config(
    msg_folder=msg_foler,
    file_folder=file_foler,
    age_of_msg_in_minutes=1,
logger=log)
jarior.producer.commit(msg_id=str(uuid.uuid4()),msg_type="txt", info= dict(
    content="Hello"
), files_path=[os.path.join(file_foler, "thu cai coi.mp4")])
