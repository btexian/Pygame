import os
import pygame

pygame.init()
img_path = os.path.abspath("images/apple.png")
print("Loading:", img_path)
image = pygame.image.load(img_path)
