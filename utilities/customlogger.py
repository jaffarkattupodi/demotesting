import logging
from selenium import webdriver
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='auto.txt',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m%d%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger