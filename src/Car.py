import pygame 

import consts 

class Car:
    def __init__(self, x_pos_on_screen, y_pos_on_screen, car_width, car_height, max_vel, rotation_vel, color=None):
        self.car = consts.CAR
        self.color = color
        if self.color != None:
            self.set_color()

        self.x_pos = x_pos_on_screen
        self.y_pos = y_pos_on_screen
        
        self.car_width = car_width
        self.car_height = car_height

        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        # initial conditions
        self.vel = 0  #init vel
        self.angle = 0 #init angle / direction

    def set_window(self, window):
        self.window = window
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT

    def scale_image(self, img, scaleFactor):
        size = round(img.get_width() * scaleFactor), round(img.get_height() * scaleFactor) 
        return pygame.transform.scale(img,size)

    def resize_image(self,img, width, height):
        return pygame.transform.scale(img,(width, height))

    def draw(self,car = consts.CAR):
        car = self.resize_image(car, self.car_width, self.car_height)
        pos  = ((self.x_pos - self.car_width )/2, (self.y_pos - self.car_height)/2)
        
        # pos  = ((self.SCREEN_WIDTH - self.x_pos)/2, (self.SCREEN_HEIGHT - self.y_pos)/2)
        self.window.blit(car,pos)

    def set_color(self):
        # Get the pixels
        pixels = pygame.PixelArray(self.car)
        # Iterate over every pixel                                             
        for x in range(self.car.get_width()):
            for y in range(self.car.get_height()):
                # Turn the pixel data into an RGB tuple
                rgb = self.car.unmap_rgb(pixels[x][y])
                # Get a new color object using the RGB tuple and convert to HSLA
                color = pygame.Color(*rgb)
                h, s, l, a = color.hsla
                # Add 120 to the hue (or however much you want) and wrap to under 360
                color.hsla = self.color, int(s), int(l), int(a)
                # Assign directly to the pixel
                pixels[x][y] = color
        # The old way of closing a PixelArray object
        del pixels
        # self.car = self.car

    