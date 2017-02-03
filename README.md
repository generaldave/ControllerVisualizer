Gamepad Visualizer

- Written in Python 3.5.2
- using pygame 1.9.3




To install pygame:
from the command prompt or Terminal, run the following:

- python -m pip install --upgrade pip
- python -m pip install pygame




App allows user to see, on screen, what buttons are being pressed on an NES or N64 controller. Currently the app is set up for the USB adapter cables from retrousb.com and authentic controllers.

There is no error checking. If an appropriate controller is not plugged in, the app will crash.




Image of both conrollers with buttons pushed:

![controllers](https://cloud.githubusercontent.com/assets/7481680/22580616/dd9f9280-e9a7-11e6-9588-f043db20665f.png)




TODO

- Work on N64 joystick rotation. It currently only knows up, down, left, and right. Also, rolling from one to the other without centering the stick is not picked up.
- Better graphic for N64 contoller.
