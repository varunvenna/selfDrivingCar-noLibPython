import pygame

def scale_image(img,scaleFactor):
    size = round(img.get_width() * scaleFactor), round(img.get_height() * scaleFactor) 
    return pygame.transform.scale(img,size)
    