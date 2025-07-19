import pygame
import os

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
    def __init__(self, x, y, name, key=None, controller_button=None):
        super().__init__()
        self.key = key
        self.controller_button = controller_button
        self.image = dim_icons[name]
        self.d_image = dim_icons[name]
        self.b_image = bright_icons[name]
        self.rect = self.d_image.get_rect()
        self.rect.topleft = (x, y)