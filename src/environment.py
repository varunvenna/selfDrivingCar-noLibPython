import pygame
import time
import math

from utils import scale_image
import consts
from Car import Car

pygame.display.set_caption("self driving car")

window = pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))

car = Car(  x_pos_on_screen = 100, 
            y_pos_on_screen = 100, 
            car_width = 20, 
            car_height = 35, 
            max_vel = 10, 
            rotation_vel = 5)

car.set_window(window)

clock = pygame.time.Clock()
run = True

while run:
    clock.tick(consts.FPS)
    car.draw()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()

pygame.quit()