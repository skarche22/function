# Logging==tracking events that happen when some software runs
# Logging is important for software developing, debugging, and running.

#
#
#
# Levels of Log Message
# There are five built-in levels of the log message.
#
# Debug (10): These are used to give Detailed information, typically of interest only when diagnosing problems.
# Info (20): These are used to confirm that things are working as expected
# Warning (30):(alert) These are used an indication that something unexpected happened, or is indicative of some problem in the near future
# Error (40): This tells that due to a more serious problem, the software has not been able to perform some function
# Critical (50): This tells serious error, indicating that the program itself may be unable to continue running


# importing module
import logging

# # Create and configure logger
# logging.basicConfig(filename="newfile.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
#
# # Creating an object
# logger = logging.getLogger()
#
# # Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)
#
# # Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")

# ##2
# import logging
# logging.basicConfig(filename='log.txt',level=logging.WARNING)
# print("logging demo")              ## HERE WE HAVE TAKEN WARNING
# logging.debug("DEBUGG")
# logging.info("INFO")
# logging.warning("WARNING")
# logging.error("ERROR")
# logging.critical("CRITICAL")


# ##3
# import logging
# logging.basicConfig(filename='log.txt',level=logging.DEBUG)
# print("logging demo")                     ## HERE WE HAVE TAKEN DEBUG
# logging.debug("DEBUGG")
# logging.info("INFO")
# logging.warning("WARNING")
# logging.error("ERROR")
# logging.critical("CRITICAL")

## DEFAULT IT IS TAKING WARNING(LEVEL=30)
##4
# import logging
# logging.basicConfig(filename='log.txt',level=logging)
# print("logging demo")                     ## HERE WE HAVE NOT TAKEN
# logging.debug("DEBUGG")
# logging.info("INFO")
# logging.warning("WARNING")
# logging.error("ERROR")
# logging.critical("CRITICAL")


##4,1 by using nubering instead of lavel name

import logging
logging.basicConfig(filename='log.txt',level=20)
print("logging demo")                     ## HERE WE HAVE TAKEN level numbering
logging.debug("DEBUGG")
logging.info("INFO")
logging.warning("WARNING")
logging.error("ERROR")
logging.critical("CRITICAL")

##5 dATE TIME
import logging
logging.basicConfig(format='%(asctime)s:%(levelnmae)s:%(message)s',datefmt='%d:%m:%Y %I:%M:%S %p')
print("logging demo")                     ## HERE WE HAVE NOT TAKEN
logging.debug("DEBUGG")
logging.info("INFO")
logging.warning("WARNING")
logging.error("ERROR")
logging.critical("CRITICAL")


##6 lOGGING TO HANDLE EXCEPTION

import logging
from logging import *
