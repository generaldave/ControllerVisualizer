########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# N64 class: Handle N64 controller                                     #
#                                                                      #
# Created on 2017-2-3                                                  #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from .Constants import *

########################################################################
#                                                                      #
#                               N64 CLASS                              #
#                                                                      #
########################################################################

class N64(object):
    def __init__(self, name: str, directory: str) -> None:
        self.imgDirectory = directory
        self.image        = self.imgDirectory + "n64.png"
        self.name         = name

    def getStickImage(self) -> str:
        return self.imgDirectory + "stick.png"

    def getVisibleImages(self) -> []:
        return self.visible

    def getType(self) -> str:
        return "N64"

    def getImage(self) -> str:
        return self.image

    def getName(self) -> str:
        return self.name

    def loadImages(self) -> []:
        images = []
        images.append(self.imgDirectory + "d_right.png")
        images.append(self.imgDirectory + "d_left.png")
        images.append(self.imgDirectory + "d_down.png")
        images.append(self.imgDirectory + "d_up.png")
        images.append(self.imgDirectory + "start.png")
        images.append(self.imgDirectory + "z.png")
        images.append(self.imgDirectory + "b.png")
        images.append(self.imgDirectory + "a.png")
        images.append(self.imgDirectory + "c_right.png")
        images.append(self.imgDirectory + "c_left.png")
        images.append(self.imgDirectory + "c_down.png")
        images.append(self.imgDirectory + "c_up.png")
        images.append(self.imgDirectory + "r_trigger.png")
        images.append(self.imgDirectory + "l_trigger.png")
        self.visible = []
        for img in images:
            self.visible.append(False)
        self.visible[len(images) - ONE] = True
        return images

    def enabler(self, button: int, flag: bool) -> None:
        self.visible[button] = flag

    def buttonPressed(self, button: int) -> None:
        self.enabler(button, True)
            
    def buttonReleased(self, button: int) -> None:
        self.enabler(button, False)

    def axisMotion(self, axis: int, motion: int) -> (int, int):
        # Handle left and right
        if (axis == ZERO):
            if (motion < ZERO):
                offset = (-FIVE, ZERO)
            elif (motion > ZERO):
                offset = (FIVE, ZERO)
            else:
                offset = (ZERO, ZERO)

        # Handles up and down
        if (axis == ONE):
            if (motion < ZERO):
                offset = (ZERO, -FIVE)
            elif (motion > ZERO):
                offset = (ZERO, FIVE)
            else:
                offset = (ZERO, ZERO)

        return offset
