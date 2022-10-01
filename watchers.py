import jarior.watcher
import loggers
import pathlib
log= loggers.get_logger(str(pathlib.Path(__file__).stem),str(pathlib.Path(__file__).parent))
jarior.watcher.config(
    msg_folder=  r"C:\code\python\msg",
    logger=log

)
def handler(context: jarior.watcher.Context):
    for x in context.files:
        print(x)
ret=jarior.watcher.watch(
    msg_type="txt",
    handler=handler

).join()