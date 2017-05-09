import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))

def draw_rect(screen, x, y):
    screen.fill((0, 0, 0))
    pygame.draw.rect(
      screen,
      (255, 0, 0),
      (x, y, 100, 100),
      0
)

pygame.display.update()



while True:
    pass
