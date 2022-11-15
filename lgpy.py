
import logging  
  

#Creating an object of the logging  
logger=logging.getLogger()  
  
  
#Test messages  
logger.debug("This is a harmless debug Message")  
logger.info("This is just an information")  
logger.warning("It is a Warning. Please make changes")  
logger.error("You are trying to divide by zero")  
logger.critical("Internet is down")   