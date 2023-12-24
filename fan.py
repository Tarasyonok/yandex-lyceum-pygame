from math import sin, cos, pi, radians

import pygame

pygame.init()

FRAMES_PER_SECOND = 50
clock = pygame.time.Clock()

size = width, height = 201, 201
screen = pygame.display.set_mode(size)

r1 = 0
r2 = radians(120)
r3 = radians(240)

points = []

mediana = 67.62
x11 = -15
y11 = -mediana
x12 = 15
y12 = -mediana

x21 = x11 * cos(r2) - y11 * sin(r2)
y21 = x11 * sin(r2) + y11 * cos(r2)
x22 = x12 * cos(r2) - y12 * sin(r2)
y22 = x12 * sin(r2) + y12 * cos(r2)

x31 = x11 * cos(r3) - y11 * sin(r3)
y31 = x11 * sin(r3) + y11 * cos(r3)
x32 = x12 * cos(r3) - y12 * sin(r3)
y32 = x12 * sin(r3) + y12 * cos(r3)

angle = radians(0)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                angle += radians(1)
            elif event.button == 3:
                angle -= radians(1)

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, pygame.Color(255, 255, 255), (100, 100), 10)

    # pygame.draw.circle(screen, pygame.Color(255, 255, 255), (x1 + 100, y1 + 100), 10)
    pygame.draw.polygon(screen, pygame.Color(255, 255, 255),
                        [(100, 100), (x11 + 100, y11 + 100), (x12 + 100, y12 + 100), (100, 100)])
    pygame.draw.polygon(screen, pygame.Color(255, 255, 255),
                        [(100, 100), (x21 + 100, y21 + 100), (x22 + 100, y22 + 100), (100, 100)])
    pygame.draw.polygon(screen, pygame.Color(255, 255, 255),
                        [(100, 100), (x31 + 100, y31 + 100), (x32 + 100, y32 + 100), (100, 100)])
    # pygame.draw.polygon(screen, pygame.Color(255, 255, 255), [(0, 0), (x21, y21), (x22, y22), (0, 0)])
    # pygame.draw.polygon(screen, pygame.Color(255, 255, 255), [(0, 0), (x31, y31), (x32, y32), (0, 0)])
    # pygame.draw.circle(screen, pygame.Color(255, 255, 255), (x2 + 100, y2 + 100), 10)
    # pygame.draw.circle(screen, pygame.Color(255, 255, 255), (x3 + 100, y3 + 100), 10)

    n_x11 = x11 * cos(angle) - y11 * sin(angle)
    n_y11 = x11 * sin(angle) + y11 * cos(angle)
    n_x12 = x12 * cos(angle) - y12 * sin(angle)
    n_y12 = x12 * sin(angle) + y12 * cos(angle)
    x11 = n_x11
    y11 = n_y11
    x12 = n_x12
    y12 = n_y12

    n_x21 = x21 * cos(angle) - y21 * sin(angle)
    n_y21 = x21 * sin(angle) + y21 * cos(angle)
    n_x22 = x22 * cos(angle) - y22 * sin(angle)
    n_y22 = x22 * sin(angle) + y22 * cos(angle)
    x21 = n_x21
    y21 = n_y21
    x22 = n_x22
    y22 = n_y22

    n_x31 = x31 * cos(angle) - y31 * sin(angle)
    n_y31 = x31 * sin(angle) + y31 * cos(angle)
    n_x32 = x32 * cos(angle) - y32 * sin(angle)
    n_y32 = x32 * sin(angle) + y32 * cos(angle)
    x31 = n_x31
    y31 = n_y31
    x32 = n_x32
    y32 = n_y32

    clock.tick(50)

    pygame.display.flip()

pygame.quit()
