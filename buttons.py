import pygame
import os

#load icons
dim_icons = {
    "up": pygame.image.load(os.path.join("icons", "u_dim.png")),
    "down": pygame.image.load(os.path.join("icons", "d_dim.png")),
    "left": pygame.image.load(os.path.join("icons", "l_dim.png")),
    "right": pygame.image.load(os.path.join("icons", "r_dim.png")),
    "1": pygame.image.load(os.path.join("icons", "1_dim.png")),
    "2": pygame.image.load(os.path.join("icons", "2_dim.png")),
    "3": pygame.image.load(os.path.join("icons", "3_dim.png")),
    "4": pygame.image.load(os.path.join("icons", "4_dim.png")),
    "5": pygame.image.load(os.path.join("icons", "5_dim.png")),
    "6": pygame.image.load(os.path.join("icons", "6_dim.png")),
    "7": pygame.image.load(os.path.join("icons", "7_dim.png")),
    "8": pygame.image.load(os.path.join("icons", "8_dim.png")),
}
bright_icons = {
    "up": pygame.image.load(os.path.join("icons", "u_bright.png")),
    "down": pygame.image.load(os.path.join("icons", "d_bright.png")),
    "left": pygame.image.load(os.path.join("icons", "l_bright.png")),
    "right": pygame.image.load(os.path.join("icons", "r_bright.png")),
    "1": pygame.image.load(os.path.join("icons", "1_bright.png")),
    "2": pygame.image.load(os.path.join("icons", "2_bright.png")),
    "3": pygame.image.load(os.path.join("icons", "3_bright.png")),
    "4": pygame.image.load(os.path.join("icons", "4_bright.png")),
    "5": pygame.image.load(os.path.join("icons", "5_bright.png")),
    "6": pygame.image.load(os.path.join("icons", "6_bright.png")),
    "7": pygame.image.load(os.path.join("icons", "7_bright.png")),
    "8": pygame.image.load(os.path.join("icons", "8_bright.png")),
}

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, name, key=None, controller_button=None, is_trigger=False):
        super().__init__()
        self.key = key
        self.is_trigger = is_trigger
        self.controller_button = controller_button
        self.image = dim_icons[name]
        self.d_image = dim_icons[name]
        self.b_image = bright_icons[name]
        self.rect = self.d_image.get_rect()
        self.rect.topleft = (x, y)