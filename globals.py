import os
from pynput import keyboard
from pygame import joystick, event

intensity = 0
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"


#===================Intensity reduction====================
#This variable controls how fast the intensity goes down
#The intensity variable is reduced by this amount every loop
    #Every loop is 3 seconds, so, for example, if this is set to 10, mashing up to 80 intensity,
    #then chilling for 3 seconds will reduce it to 70, and so on.
#Try out different values to see how high your APM needs to be for the intended strength of vibrations.
#I'd recommend starting with 10, then going up or down until it feels right. You can use decimals, too, if you feel like it.

intensity_reduction_factor = 11

#===================Keyboard binds=========================
#Tetris keybinds for the input viewer
#If any of the keys you use aren't letters
#find what the keycode is here:
#https://pynput.readthedocs.io/en/latest/_modules/pynput/keyboard/_base.html#Controller.press

key_left = "r"
key_right = "t"
key_down = "s"
key_up = keyboard.Key.alt_l
key_cw = "i"
key_ccw = "n"
key_hold = "e"
key_zone = keyboard.Key.space

#===============Xbox 360 controller binds==================
# Leave the directions alone
# Button values can be found here: https://www.pygame.org/docs/ref/joystick.html

button_left = (-1, 0)   #Dpad Left
button_right = (1, 0)   #Dpad Right
button_down = (0, -1)   #Dpad Down
button_up = (0, 1)      #Dpad Up
button_cw = 2           # X Button
button_ccw = 3          # Y Button
button_hold = 5         # Right Bumper
button_zone = 0         # A Button