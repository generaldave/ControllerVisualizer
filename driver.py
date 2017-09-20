################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# Driver File                                                                  #
#                                                                              #
# Created on 2017-3-18                                                         #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                              IMPORT STATEMENTS                               #
#                                                                              #
################################################################################

from   app import logger   # Error logging package
from   app import App      # Main application package
import os                  # For file handling

################################################################################
#                                                                              #
#                                   DRIVER                                     #
#                                                                              #
################################################################################

# Initialize app
def main(appDirectory) -> None:
    App(appDirectory)

# If this file was ran directly: try to run app, or log errors
if __name__ == "__main__": 
    # Store app directory
    appDirectory = os.path.dirname(os.path.realpath(__file__))

    # Initialize error logging
    log = logger.Logger(appDirectory, 'w')

    # Try to run app, otherwise log error
    try:   
        main(appDirectory)
    except:
        log.createLog('')
