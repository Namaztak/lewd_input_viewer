import os
from pynput import keyboard

intensity = 0
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

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

#button_left
#button_right
#button_down
#button_up
#button_cw
#button_ccw
#button_hold
#button_zone