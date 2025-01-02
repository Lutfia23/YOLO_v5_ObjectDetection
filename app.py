from SignLanguage.logger import logging
from SignLanguage.exception import SignException
import sys

#logging.info("Welcome to the project....")

try:
    #a = 7 / '9'
    a= 5 / 5

except Exception as e:
    raise SignException(e, sys) from e