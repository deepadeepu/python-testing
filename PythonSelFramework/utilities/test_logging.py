# __name__ captures testscase name it will print in log file
import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)  # file handler object

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("info statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical")
