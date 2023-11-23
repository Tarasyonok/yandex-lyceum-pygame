import pygame

width = 450
height = 300
n = int(input())
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.init()


def draw(screen):
    screen.fill('yellow')
    for i in range(width // n):
        for j in range(height // n):
            p1 = (i * n + n / 2, j * n)
            p2 = (i * n, j * n + n / 2)
            p3 = (i * n + n, j * n + n / 2)
            p4 = (i * n + n / 2, j * n + n)
            pygame.draw.polygon(screen, 'orange', [p1, p2, p4, p3])


draw(screen)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
