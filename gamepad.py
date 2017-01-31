# NES Controller = RetroUSB.com RetroPad
# N64 Controller = SealieComputing N64 RetroPort
import pygame
import os

pygame.init()

width = 500
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gamepad Stuffs")

appDirectory  = os.path.dirname(os.path.realpath(__file__))
controllerImg = pygame.image.load(appDirectory + "/images/nes.png")
upImg         = pygame.image.load(appDirectory + "/images/d_up.png")
downImg       = pygame.image.load(appDirectory + "/images/d_down.png")
leftImg       = pygame.image.load(appDirectory + "/images/d_left.png")
rightImg      = pygame.image.load(appDirectory + "/images/d_right.png")
selectImg     = pygame.image.load(appDirectory + "/images/select.png")
startImg      = pygame.image.load(appDirectory + "/images/start.png")
bImg          = pygame.image.load(appDirectory + "/images/b.png")
aImg          = pygame.image.load(appDirectory + "/images/a.png")

images = []
images.append(upImg)
images.append(downImg)
images.append(leftImg)
images.append(rightImg)
images.append(selectImg)
images.append(startImg)
images.append(bImg)
images.append(aImg)

clock = pygame.time.Clock()
pygame.joystick.init()

screen.blit(controllerImg, (10,10))

counter = 0
index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.JOYBUTTONDOWN:
            print("button pressed")
        if event.type == pygame.JOYBUTTONUP:
            print("button released")
    

    gamepads = []
    padCount = pygame.joystick.get_count()
    for i in range(padCount):
        gamepads.append(pygame.joystick.Joystick(i))

    for pad in gamepads:
        pad.init()
        name = pad.get_name()
##        if name == "RetroUSB.com RetroPad":
##            print("NES gamepad plugged in")            
##        elif name == "SealieComputing N64 RetroPort":
##            print("N64 gamepad plugged in")

        buttons = pad.get_numbuttons()
        for i in range(buttons):
            button  = pad.get_button(i)        
            if button:
                print(name, str(i), str(button))

    counter = counter + 1
    if counter == 60:
        screen.blit(controllerImg, (10,10))
        screen.blit(images[index], (10,10))
        index = index + 1
        if index == len(images):
            index = 0
        counter = 0

    pygame.display.update()
    clock.tick(60)

pygame.quit()
