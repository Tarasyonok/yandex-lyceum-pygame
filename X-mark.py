import pygame

width = int(input())
height = int(input())
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.init()


def draw(screen):
    screen.fill((0, 0, 0))
    color = pygame.Color(255, 255, 255)
    pygame.draw.line(screen, color, (0, 0), (width, height), 5)
    pygame.draw.line(screen, color, (width, 0), (0, height), 5)


draw(screen)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
