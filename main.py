import pygame
import os
import threading
import sys
import asyncio
import random
from globals import *
from plug import *
from pynput import keyboard, mouse

#initialize pygame window
pygame.init()

pygame.joystick.init()
width, height = 370, 110
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Input Viewer")

#set background to green for chromakey usage
screen.fill((0, 255, 0))


#load icons
dim_icons = {
    "up": pygame.image.load(os.path.join("icons", "u_dim.png")),
    "down": pygame.image.load(os.path.join("icons", "d_dim.png")),
    "left": pygame.image.load(os.path.join("icons", "l_dim.png")),
    "right": pygame.image.load(os.path.join("icons", "r_dim.png")),
    "cw": pygame.image.load(os.path.join("icons", "cw_dim.png")),
    "ccw": pygame.image.load(os.path.join("icons", "ccw_dim.png")),
    "hold": pygame.image.load(os.path.join("icons", "h_dim.png")),
    "zone": pygame.image.load(os.path.join("icons", "z_dim.png")),
}
bright_icons = {
    "up": pygame.image.load(os.path.join("icons", "u_bright.png")),
    "down": pygame.image.load(os.path.join("icons", "d_bright.png")),
    "left": pygame.image.load(os.path.join("icons", "l_bright.png")),
    "right": pygame.image.load(os.path.join("icons", "r_bright.png")),
    "cw": pygame.image.load(os.path.join("icons", "cw_bright.png")),
    "ccw": pygame.image.load(os.path.join("icons", "ccw_bright.png")),
    "hold": pygame.image.load(os.path.join("icons", "h_bright.png")),
    "zone": pygame.image.load(os.path.join("icons", "z_bright.png")),
}

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, name, key=None):
        super().__init__()
        self.key = key
        self.image = dim_icons[name]
        self.d_image = dim_icons[name]
        self.b_image = bright_icons[name]
        self.rect = self.d_image.get_rect()
        self.rect.topleft = (x, y)

left = Button(0, 0, "left", pygame.K_r)
right = Button(120, 0, "right", pygame.K_t)
down = Button(60, 0, "down", pygame.K_s)
up = Button(120, 60, "up", pygame.K_LALT)
cw = Button(320, 0, "cw", pygame.K_i)
ccw = Button(200, 0, "ccw", pygame.K_n)
hold = Button(260, 0, "hold", pygame.K_e)
zone = Button(200, 60, "zone", pygame.K_SPACE)

#add buttons to sprite group
button_group = pygame.sprite.Group()
button_group.add(left, right, down, up, cw, ccw, hold, zone)

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
    global intensity
    try:
        if key.char == key_left:  # left key
            left.image = left.b_image
        elif key.char == key_right:  # right key
            right.image = right.b_image
        elif key.char == key_down:  # down key
            down.image = down.b_image
        elif key.char == key_cw:  # cw key
            cw.image = cw.b_image
        elif key.char == key_ccw:  # ccw key
            ccw.image = ccw.b_image
        elif key.char == key_hold:  # hold key
            hold.image = hold.b_image          
        elif key.char == key_zone:
            zone.image = zone.b_image
    except AttributeError:
        if key == key_up:
            up.image = up.b_image
        elif key == key_left:  # left key
            left.image = left.b_image
        elif key == key_right:  # right key
            right.image = right.b_image
        elif key == key_down:  # down key
            down.image = down.b_image
        elif key == key_cw:  # cw key
            cw.image = cw.b_image
        elif key == key_ccw:  # ccw key
            ccw.image = ccw.b_image
        elif key == key_hold:  # hold key
            hold.image = hold.b_image
        elif key == key_zone:  # space key
            zone.image = zone.b_image
    intensity += button_intensity

def on_release(key):
    try:
        if key.char == key_left:  # left key
            left.image = left.d_image
        elif key.char == key_right:    # right key
            right.image = right.d_image
        elif key.char == key_down:     # down key
            down.image = down.d_image
        elif key.char == key_cw:       # cw key
            cw.image = cw.d_image
        elif key.char == key_ccw:      # ccw key
            ccw.image = ccw.d_image
        elif key.char == key_hold:     # hold key
            hold.image = hold.d_image
        elif key.char == key_zone:     # Zone key
            zone.image = zone.d_image
    except AttributeError:
        if key == key_up:
            up.image = up.d_image
        elif key == key_left:          # left key
            left.image = left.d_image
        elif key == key_right:         # right key
            right.image = right.d_image
        elif key == key_down:          # down key
            down.image = down.d_image
        elif key == key_cw:            # cw key
            cw.image = cw.d_image
        elif key == key_ccw:           # ccw key
            ccw.image = ccw.d_image
        elif key == key_hold:          # hold key
            hold.image = hold.d_image
        elif key == key_zone:          # Zone key
            zone.image = zone.d_image

def on_controller_press(button=None, val=None):
    global intensity
    if button != None:
        if button == button_cw:         # cw key
            cw.image = cw.b_image
        elif button == button_ccw:      # ccw key
            ccw.image = ccw.b_image
        elif button == button_hold:     # hold key
            hold.image = hold.b_image
        elif button == button_zone:     # Zone key
            zone.image = zone.b_image
        intensity += button_intensity
    elif val != None:
        if val[0] == 1:
            right.image = right.b_image
        if val[1] == 1:
            up.image = up.b_image
        if val[0] == -1:
            left.image = left.b_image
        if val[1] == -1:
            down.image = down.b_image
        if val[0] == 0:
            right.image = right.d_image
            left.image = left.d_image
        if val[1] == 0:
            up.image = up.d_image
            down.image = down.d_image
        intensity += button_intensity/2

def on_controller_release(button=None):
    if button != None:
        if button == button_cw:         # cw key
            cw.image = cw.d_image
        elif button == button_ccw:      # ccw key
            ccw.image = ccw.d_image
        elif button == button_hold:     # hold key
            hold.image = hold.d_image
        elif button == button_zone:
            zone.image = zone.d_image

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
        if reduction_counter > (60 * granularity) and vibe != None:
            await reduce_intensity(vibe)
            reduction_counter = 0
        elif vibe == None:
            intensity = 0
        reduction_counter += 1
if __name__ == "__main__":
    asyncio.run(main())