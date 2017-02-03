########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Driver File                                                          #
#                                                                      #
# Created on 2017-1-23                                                 #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   logger import *   # Error logging package
from   app    import *   # Main application package
import os                # For file handling

########################################################################
#                                                                      #
#                                DRIVER                                #
#                                                                      #
########################################################################

# Initialize app
def main(appDirectory) -> None:
    App(appDirectory)

# If this file was ran directly: try to run app, or log errors
if __name__ == "__main__": 
    # Store app directory
    appDirectory = os.path.dirname(os.path.realpath(__file__))

    # Initialize error logging
    logger = Logger(appDirectory, 'w')

    # Try to run app, otherwise log error
    try:   
        main(appDirectory)
    except:
        logger.createLog('')
