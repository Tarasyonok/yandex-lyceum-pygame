import pygame

width = 300
height = 300
W = int(input())
Hue = int(input())
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.init()

color = pygame.Color(255, 255, 255)
hsv = color.hsva
color2 = pygame.Color(255, 255, 255)
hsv2 = color2.hsva
color3 = pygame.Color(255, 255, 255)
hsv3 = color3.hsva

color_top = pygame.Color(255, 255, 255)
hsv_top = color_top.hsva
color_top.hsva = (Hue, hsv_top[1] + 100, hsv_top[2], hsv_top[3])

color_front = pygame.Color(255, 255, 255)
hsv_front = color_front.hsva
color_front.hsva = (Hue, hsv_front[1] + 100, hsv_front[2] - 25, hsv_front[3])

color_side = pygame.Color(255, 255, 255)
hsv_side = color_side.hsva
color_side.hsva = (Hue, hsv_side[1] + 100, hsv_side[2] - 50, hsv_side[3])


def draw(screen):
    screen.fill('black')
    p11 = (width / 2 - W / 2 - W / 4, height / 2 - W / 4)
    p12 = (width / 2 + W / 2 - W / 4, height / 2 - W / 4)
    p13 = (width / 2 + W / 2 - W / 4, height / 2 + W - W / 4)
    p14 = (width / 2 - W / 2 - W / 4, height / 2 + W - W / 4)

    pygame.draw.polygon(screen, color_front, [p11, p12, p13, p14])

    p21 = (p11[0] + W / 2, p11[1] - W / 2)
    p22 = (p11[0] + W / 2 + W, p11[1] - W / 2)
    p23 = p12
    p24 = p11

    pygame.draw.polygon(screen, color_top, [p21, p22, p23, p24])

    p31 = p12
    p32 = p22
    p33 = (p13[0] + W / 2, p13[1] - W / 2)
    p34 = p13

    pygame.draw.polygon(screen, color_side, [p31, p32, p33, p34])


draw(screen)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
