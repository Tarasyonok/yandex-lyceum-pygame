import pygame

width = 300
height = 300
n = int(input())
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.init()


def draw(screen):
    screen.fill('black')
    x = width / n / 2
    y = height / n / 2
    for i in range(n):
        pygame.draw.ellipse(screen, 'white', (x * i, 0, width - x * i * 2, height), 1)
        pygame.draw.ellipse(screen, 'white', (0, y * i, width, height - y * i * 2), 1)


draw(screen)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
