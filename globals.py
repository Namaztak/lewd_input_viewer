import os
from pynput import keyboard

#initial intensity value. There's no reason to touch this, it's just here to keep the variable outside of the main script.
intensity = 0

#This is needed for the controller inputs to be read in the background. Again, don't touch this.
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"


#======================Intensity==========================
#These variables control how fast the intensity goes up and down

#intensity_reduction_factor: The global intensity variable is reduced by this amount after every time a vibration is sent
    #Every loop is 3 seconds by default, so, for example, if this is set to 10, mashing up to 80 intensity,
    #then chilling for 3 seconds will reduce it to 70, and so on.
#Try out different values to see how high your APM needs to be for the intended strength of vibrations.
#I'd recommend starting with 10, then going up or down a bit until it feels right. You can use decimals, too, if you feel like it.

intensity_reduction_factor = 10

#analog_intensity: Moving any analog axis (this includes triggers) ANY AMOUNT increases intensity by this amount.
    #I highly recommend setting this to a small decimal value between 0 and 0.3, erring lower, especially for games that use both sticks.
    #Sticks get polled for their movement A LOT, so adjust this with caution.

analog_intensity = 0.01

#button_intensity: Pressing any button (not including analog triggers, or arcade buttons bound to the triggers), or moving the Dpad on ANY controller increases intensity by this amount
#I built the program with 1 in mind, so try it as is first.

button_intensity = 1

#granularity: #How many seconds between firing commands to the vibrator, lower is faster. I've only tested as low as 1, these toys probably aren't THAT responsive.
#Also keep in mind this is directly affected by the intensity_reduction_factor. The higher that is, the faster this will make the intensity go down.
#In other words, if you want longer vibrations, set intensity_reduction_factor lower and granularity higher, and if you want more spiky pulses, do the opposite.

granularity = 3

#===================Keyboard binds=========================
#Keybinds for the input viewer
#If any of the keys you use aren't letters
#find what the keycode is here:
#https://pynput.readthedocs.io/en/latest/_modules/pynput/keyboard/_base.html#Controller.press

key_left = keyboard.KeyCode(char="r")
key_right = keyboard.KeyCode(char="t")
key_down = keyboard.KeyCode(char="s")
key_up = keyboard.Key.alt_l
key_1 = keyboard.KeyCode(char="n")
key_2 = keyboard.KeyCode(char="e")
key_3 = keyboard.KeyCode(char="i")
key_4 = keyboard.KeyCode(char="o")
key_5 = keyboard.Key.space
key_6 = keyboard.KeyCode(char=",")
key_7 = keyboard.KeyCode(char=".")
key_8 = keyboard.KeyCode(char="/")

#===============Xbox 360 controller binds==================
# Leave the directions alone
# Button values can be found here: https://www.pygame.org/docs/ref/joystick.html

controller_button_left = (-1, 0)   #Dpad Left
controller_button_right = (1, 0)   #Dpad Right
controller_button_down = (0, -1)   #Dpad Down
controller_button_up = (0, 1)      #Dpad Up
controller_button_1 = 3            # Y Button
controller_button_2 = 5            # Right Bumper
controller_button_3 = 2            # X Button
controller_button_4 = 4            # Left Bumper
controller_button_5 = 0            # A Button
controller_button_6 = 1            # B Button
controller_button_7 = 5            # Left Trigger (axis 2)
controller_button_8 = 4            # Right Trigger (axis 5)
#=====================Mouse Values=========================

# mouse_move_intensity: How much to increase intensity when just moving your mouse.
# I cannot stress enough how much you do not realize your mouse moves even when you're "holding still".
# For the safety of your nerves, do not set this higher than like 0.1
# Testing this at 0.05 was enough to make it so mouse movement alone could outpace the default intensity reduction factor.

mouse_move_intensity = 0.02

# mouse_click_intensity: How much to increase intensity when you click the mouse.
# Feel free to set this to whatever you want. If you're clicking a lot, lower it, and if not, raise it.

mouse_click_intensity = 1

# mouse_scroll_intensity: How much to increase intensity when you scroll the mouse wheel.
# If you, like me, are a speedrunner that likes to have jump bound to scrolling, say for bunnyhopping, maybe keep this one low.

mouse_scroll_intensity = 0.3