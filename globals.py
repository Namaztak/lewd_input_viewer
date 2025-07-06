import os
from pynput import keyboard

intensity = 0
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"


#======================Intensity==========================
#These variables control how fast the intensity goes up and down

#intensity_reduction_factor: The global intensity variable is reduced by this amount after every time a vibration is sent
    #Every loop is 3 seconds by default, so, for example, if this is set to 10, mashing up to 80 intensity,
    #then chilling for 3 seconds will reduce it to 70, and so on.
#Try out different values to see how high your APM needs to be for the intended strength of vibrations.
#I'd recommend starting with 10, then going up or down a bit until it feels right. You can use decimals, too, if you feel like it.

intensity_reduction_factor = 10

#analog_intensity: Moving any analog axis (this includes triggers) increases intensity by this amount.
    #I highly recommend setting this to a decimal value between 0 and 0.5, erring lower, especially for games that use both sticks.
    #Sticks get polled for their movement A LOT, so adjust this with caution.

analog_intensity = 0.05

#button_intensity: Pressing any button, or moving the Dpad on the controller increases intensity by this amount
#I built the program with 1 in mind, so try it as is first.

button_intensity = 1

#granularity: #How many seconds between firing commands to the vibrator, lower is faster. Don't go lower than 1, these toys aren't THAT responsive.
#Also keep in mind this is directly affected by the intensity_reduction_factor. The higher that is, the faster this will make the intensity go down.
#In other words, if you want longer vibrations, set intensity_reduction_factor lower and granularity higher.

granularity = 3

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