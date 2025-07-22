import pygame
import os
import threading
import sys
import asyncio
import random
from globals import *
from plug import *
from pynput import keyboard, mouse
from buttons import *

#initialize pygame window
pygame.init()

pygame.joystick.init()
width, height = 430, 110
screen = pygame.display.set_mode((width, height))
surface = pygame.display.get_surface()
pygame.display.set_caption("Input Viewer")

#set background to green for chromakey usage
screen.fill((0, 255, 0))



left = Button(0, 0, "left", key_left, controller_button_left)
right = Button(120, 0, "right", key_right, controller_button_right)
down = Button(60, 0, "down", key_down, controller_button_down)
up = Button(120, 60, "up", key_up, controller_button_up)
button1 = Button(200, 0, "1", key_1, controller_button_1)
button2 = Button(260, 0, "2", key_2, controller_button_2)
button3 = Button(320, 0, "3", key_3, controller_button_3)
button4 = Button(380, 0, "4", key_4, controller_button_4)
button5 = Button(200, 60, "5", key_5, controller_button_5)
button6 = Button(260, 60, "6", key_6, controller_button_6)
button7 = Button(320, 60, "7", key_7, controller_button_7, is_trigger=True)
button8 = Button(380, 60, "8", key_8, controller_button_8, is_trigger=True)

buttons = [left, right, down, up, button1, button2, button3, button4, button5, button6, button7, button8]
#add buttons to sprite group
button_group = pygame.sprite.Group()
button_group.add(buttons)

pressed_keys = []

#Functions to handle mouse input
def on_move(x, Y):
    global intensity
    intensity += mouse_move_intensity

def on_click(x, y, button, pressed):
    global intensity
    intensity += mouse_click_intensity

def on_scroll(x, y, dx, dy):
    global intensity
    intensity += mouse_scroll_intensity

def listen_to_mouse():
    with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener:
        mouse_listener.join()


#Functions to handle keyboard input
def on_press(key):
    global intensity, pressed_keys, buttons
    if key not in pressed_keys:
        for button in buttons:
            if button.key == key:
                button.image = bright_icons[button.name]
        pressed_keys.append(key)
        intensity += button_intensity

def on_release(key):
    global intensity, buttons
    for button in buttons:
        if button.key == key:
            button.image = dim_icons[button.name]
    pressed_keys.remove(key)

def on_controller_press(sent_button=None, val=None):
    global intensity, buttons
    if sent_button is not None:
        for button in buttons:
            if button.controller_button == sent_button and not button.is_trigger:
                button.image = button.b_image
        intensity += button_intensity
    elif val is not None:
        if val[0] == 1:
            right.image = bright_icons["right"]
        if val[1] == 1:
            up.image = bright_icons["up"]
        if val[0] == -1:
            left.image = bright_icons["left"]
        if val[1] == -1:
            down.image = bright_icons["down"]
        if val[0] == 0:
            right.image = dim_icons["right"]
            left.image = dim_icons["left"]
        if val[1] == 0:
            up.image = dim_icons["up"]
            down.image = dim_icons["down"]
        intensity += button_intensity/2

def on_controller_release(sent_button=None):
    if sent_button is not None:
        for button in buttons:
            if button.controller_button == sent_button and not button.is_trigger:
                button.image = button.d_image

def listen_to_keyboard():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


#Handles main communication with toy, and reduces intensity after sending the vibration each loop
async def reduce_intensity(vibe):
    global intensity
    if intensity == 0:
        for i in vibe.actuators:
            await i.command(0)
        for i in vibe.rotatory_actuators:
            await i.command(0, True)
        for i in vibe.linear_actuators:
            await i.command(granularity * 1000, 0)
    if intensity > 0:
        if intensity > 100:
            for i in vibe.actuators:
                await i.command(1)
            for i in vibe.rotatory_actuators:
                await i.command(1, random.choice([True, False]))
            for i in vibe.linear_actuators:
                await i.command(granularity * 1000, 1)
            intensity = 100
            print('Sending vibration, intensity: MAX')
            intensity = max(0, intensity - intensity_reduction_factor)
            return
        else:
            for i in vibe.actuators:
                await i.command(intensity/100)
            for i in vibe.rotatory_actuators:
                await i.command(intensity/100, random.choice([True, False]))
            for i in vibe.linear_actuators:
                await i.command(granularity * 1000, intensity/100)
    print(f'Sending vibration, intensity: {intensity:.2f}')
    intensity = max(0, intensity - intensity_reduction_factor)
    

keyboard_thread = threading.Thread(target=listen_to_keyboard)
keyboard_thread.daemon = True  # Set as daemon thread so it exits when main thread exits
keyboard_thread.start()


# Comment these next three lines out if you wanna fix the window dragging issue, but lose the progam caring about mouse inputs.
mouse_thread = threading.Thread(target=listen_to_mouse)
mouse_thread.daemon = True  # Set as daemon thread so it exits when main thread exits
mouse_thread.start()

async def main():
    
    global intensity
    vibe = await plug_connect()
    reduction_counter = 0
    joysticks = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.JOYDEVICEADDED:
                print(f"Joystick {event.device_index} connected")
                joysticks.append(pygame.joystick.Joystick(event.device_index))
                for i in range(len(joysticks)):
                    print(i, joysticks[i].get_name())
            elif event.type in [pygame.JOYBUTTONDOWN, pygame.JOYAXISMOTION,pygame.JOYHATMOTION]:
                if event.type == pygame.JOYAXISMOTION:
                    print(event.axis, event.value)
                    for button in buttons:
                        if button.controller_button == event.axis and event.value >= 0.1 and button.is_trigger:
                            button.image = button.b_image
                        elif button.controller_button == event.axis and event.value < 0.1 and button.is_trigger:
                            button.image = button.d_image
                    intensity += analog_intensity
                    print(f'Intensity: {intensity:.2f}')
                else:
                    if event.type == pygame.JOYHATMOTION:
                        try:
                            on_controller_press(val=event.value)
                        except AttributeError:
                            pass
                    elif event.type == pygame.JOYBUTTONDOWN:
                        try:
                            on_controller_press(event.button)
                        except AttributeError:
                            pass
                print(f'Intensity: {intensity:.2f}')
            elif event.type == pygame.JOYBUTTONUP:
                on_controller_release(event.button)
                
        button_group.draw(screen)
        pygame.display.update()
        pygame.time.Clock().tick(60)  # Limit to 60 FPS
        surface.fill((0, 255, 0))
        if reduction_counter > (60 * granularity) and vibe != None:
            await reduce_intensity(vibe)
            reduction_counter = 0
        elif vibe == None:
            intensity = 0
        reduction_counter += 1
if __name__ == "__main__":
    asyncio.run(main())