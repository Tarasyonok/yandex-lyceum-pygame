import pygame

width = int(input())
height = int(input())
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.init()


def draw(screen):
    screen.fill((0, 0, 0))
    color = pygame.Color(255, 0, 0)
    pygame.draw.rect(screen, color, [(1, 1), (width - 1, height - 1)])


draw(screen)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
