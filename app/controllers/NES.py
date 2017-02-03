########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# NES class: Handle NES controller                                     #
#                                                                      #
# Created on 2017-2-3                                                  #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from .Constants import *   #Constants file

########################################################################
#                                                                      #
#                               NES CLASS                              #
#                                                                      #
########################################################################

class NES(object):
    def __init__(self, name: str, directory: str) -> None:
        self.imgDirectory = directory
        self.image        = self.imgDirectory + "nes.png"
        self.name         = name

    def getVisibleImages(self) -> []:
        return self.visible

    def getType(self) -> str:
        return "NES"

    def getImage(self) -> str:
        return self.image

    def getName(self) -> str:
        return self.name

    def loadImages(self) -> []:
        images = []
        images.append(self.imgDirectory + "b.png")
        images.append(self.imgDirectory + "a.png")
        images.append(self.imgDirectory + "select.png")
        images.append(self.imgDirectory + "start.png")
        images.append(self.imgDirectory + "d_up.png")
        images.append(self.imgDirectory + "d_down.png")
        images.append(self.imgDirectory + "d_left.png")
        images.append(self.imgDirectory + "d_right.png")
        self.visible = []
        for img in images:
            self.visible.append(False)
        return images

    def enabler(self, button: int, flag: bool) -> None:
        self.visible[button] = flag

    def buttonPressed(self, button: int) -> None:
        self.enabler(button, True)
            
    def buttonReleased(self, button: int) -> None:
        self.enabler(button, False)

    def axisMotion(self, axis: int, motion: int) -> None:
        # Handle left and right
        if (axis == ZERO):
            if (motion < ZERO):
                self.enabler(LEFT, True)
            elif (motion > ZERO):
                self.enabler(RIGHT, True)
            else:
                self.enabler(LEFT, False)
                self.enabler(RIGHT, False)

        # Handles up and down
        if (axis == ONE):
            if (motion < ZERO):
                self.enabler(UP, True)
            elif (motion > ZERO):
                self.enabler(DOWN, True)
            else:
                self.enabler(UP, False)
                self.enabler(DOWN, False)
