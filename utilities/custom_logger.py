import logging
import inspect

class CustomLogger():

    def customLog(self,logLevel = logging.DEBUG):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.DEBUG)

        fhandler = logging.FileHandler("automation.log",mode='a')
        fhandler.setLevel(logLevel)

        formatter = logging.Formatter('%(asctime)s -%(name)s %(levelname)s %(message)s',datefmt='%d/%m/%y %I:%M:%S')
        fhandler.setFormatter(formatter)

        logger.addHandler(fhandler)
        return logger

