import os
from pynput import keyboard
from pygame import joystick, event

intensity = 0
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

#Tetris keybinds for the input viewer
#If any of the keys you use aren't letters
#find what the keycode is here:
#https://pynput.readthedocs.io/en/latest/_modules/pynput/keyboard/_base.html#Controller.press


#This variable controls how fast the intensity goes down
intensity_reduction_factor = 11

#===================Keyboard binds=========================
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