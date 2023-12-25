from random import choice

import pygame

pygame.init()


class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.board = [[0] * w for i in range(h)]
        self.left = 10
        self.right = 10
        self.cell_size = 30
        self.has_red = None

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        x_pos, y_pos = mouse_pos
        x = (x_pos - self.left) // self.cell_size
        y = (y_pos - self.left) // self.cell_size
        if 0 <= x < self.w and 0 <= y <= self.h - 1:
            return x, y

        return None

    def process_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            y, x = cell
            if self.board[x][y] == 0:
                if self.has_red:
                    self.b1 = False
                    self.b2 = False
                    self.b3 = False
                    self.b4 = False
                    if self.has_path(*self.has_red, x, y):
                        self.board[x][y] = 1
                        self.board[self.has_red[0]][self.has_red[1]] = 0
                        self.has_red = None
                    else:
                        self.board[self.has_red[0]][self.has_red[1]] = 2
                else:
                    self.board[x][y] = 1
            elif self.board[x][y] == 1:
                if self.has_red:
                    self.board[self.has_red[0]][self.has_red[1]] = 1
                self.has_red = [x, y]
                self.board[x][y] = 2
            elif self.board[x][y] == 2:
                self.has_red = None
                self.board[x][y] = 1


class Lines(Board):
    def render(self, screen):
        for y in range(self.h):
            for x in range(self.w):
                if self.board[y][x] == 1:
                    pygame.draw.circle(screen, pygame.Color((0, 0, 255)),
                                       (x * self.cell_size + self.left + self.cell_size / 2,
                                        y * self.cell_size + self.top + self.cell_size / 2), self.cell_size / 2)
                elif self.board[y][x] == 2:
                    pygame.draw.circle(screen, pygame.Color((255, 0, 0)),
                                       (x * self.cell_size + self.left + self.cell_size / 2,
                                        y * self.cell_size + self.top + self.cell_size / 2), self.cell_size / 2)

                pygame.draw.rect(screen, pygame.Color((190, 190, 190)),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def has_path(self, x1, y1, x2, y2):
        # print(x1, y1, x2, y2)
        if x1 == x2 and y1 == y2:
            return True
        else:
            # if self.board[x1][y1] != 0:
            #     return False
            # self.board[x1][x2] = 3
            self.board[x1][y1] = 3

            w1 = w2 = w3 = w4 = False

            if x1 - 1 < 0:
                self.b1 = True
            if not self.b1 and self.board[x1 - 1][y1] == 0:
                w1 = self.has_path(x1 - 1, y1, x2, y2)
            for i in range(self.h):
                for j in range(self.w):
                    if self.board[i][j] == 3:
                        self.board[i][j] = 0
            if x1 + 1 > self.w - 1:
                self.b2 = True
            if not self.b2 and self.board[x1 + 1][y1] == 0:
                w2 = self.has_path(x1 + 1, y1, x2, y2)
            for i in range(self.h):
                for j in range(self.w):
                    if self.board[i][j] == 3:
                        self.board[i][j] = 0
            if y1 - 1 < 0:
                self.b3 = True
            if not self.b3 and self.board[x1][y1 - 1] == 0:
                w3 = self.has_path(x1, y1 - 1, x2, y2)
            for i in range(self.h):
                for j in range(self.w):
                    if self.board[i][j] == 3:
                        self.board[i][j] = 0
            if y1 + 1 > self.h - 1:
                self.b4 = True
            if not self.b4 and self.board[x1][y1 + 1] == 0:
                print(123)
                w4 = self.has_path(x1, y1 + 1, x2, y2)
            for i in range(self.h):
                for j in range(self.w):
                    if self.board[i][j] == 3:
                        self.board[i][j] = 0
            # if self.b1 and self.b2 and self.b3 and self.b3:
            #     print(123)
            #     return False

            return w1 or w2 or w3 or w4
            # e = True
            # if x1 > 0:
            #     # e = False
            # if x1 < self.w - 1:
            # e = False
            # w3 = self.has_path(x1, y1 - 1, x2, y2)
            # w4 = self.has_path(x1, y1 + 1, x2, y2)
            # if e:
            #     return False
            # return w1 or w2
            # return w1 or w2 or w3 or w4


size = 440, 440
screen = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()

board = Lines(10, 10)
board.set_view(20, 20, 40)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.process_click(event.pos)

    screen.fill((0, 0, 0))
    board.render(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
