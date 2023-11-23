import pygame

width = int(input())
n = int(input())
x = width // n
size = (width, width)
screen = pygame.display.set_mode(size)
pygame.init()


def draw(screen):
    screen.fill((0, 0, 0))
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), [(i * x, j * x), (i * x + x, j * x + x)])
            else:
                pygame.draw.rect(screen, pygame.Color(0, 0, 0), [(i * x, j * x), (i * x + x, j * x + x)])


draw(screen)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
