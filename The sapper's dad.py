from random import choice

import pygame

pygame.init()


class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.board = [[-1] * w for i in range(h)]
        self.left = 10
        self.right = 10
        self.cell_size = 30

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
            self.open_cell(cell)
            for i in range(self.h):
                for j in range(self.w):
                    if self.board[i][j] == -10:
                        self.board[i][j] = 0


class Minesweeper(Board):
    def __init__(self, w, h, mines):
        super().__init__(w, h)
        poses = []
        for i in range(h):
            for j in range(w):
                poses.append((i, j))

        for _ in range(mines):
            pos = choice(poses)
            self.board[pos[0]][pos[1]] = 10
            poses.remove(pos)

    def render(self, screen):
        for y in range(self.h):
            for x in range(self.w):
                if self.board[y][x] == 10:
                    pygame.draw.rect(screen, pygame.Color((255, 0, 0)),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size))
                elif 0 <= self.board[y][x] <= 9:
                    f = pygame.font.Font(None, 35)
                    sc_text = f.render(str(self.board[y][x]), 1, pygame.Color(0, 255, 0))
                    x_coord = x * self.cell_size + self.cell_size / 2 + self.left
                    y_coord = y * self.cell_size + self.cell_size / 2 + self.top
                    pos = sc_text.get_rect(center=(x_coord, y_coord))
                    screen.blit(sc_text, pos)

                pygame.draw.rect(screen, pygame.Color((190, 190, 190)),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def open_cell(self, cell):
        x, y = cell
        if self.board[y][x] == 10 or self.board[y][x] == -10:
            return
        around = 0
        cells = self.cells_around(x, y)
        for c in cells:
            if self.board[c[0]][c[1]] == 10:
                around += 1
        if around == 0:
            self.board[y][x] = -10
            if x < self.w - 1:
                self.open_cell((x + 1, y))
            if x > 0:
                self.open_cell((x - 1, y))
            if y < self.h - 1:
                self.open_cell((x, y + 1))
            if y > 0:
                self.open_cell((x, y - 1))
        else:
            self.board[y][x] = around

    def cells_around(self, j, i):
        cells = []
        if i > 0 and j > 0:
            cells.append((i - 1, j - 1))
        if i > 0:
            cells.append((i - 1, j))
        if i > 0 and j < self.w - 1:
            cells.append((i - 1, j + 1))
        if j > 0:
            cells.append((i, j - 1))
        if j < self.w - 1:
            cells.append((i, j + 1))
        if i < self.h - 1 and j > 0:
            cells.append((i + 1, j - 1))
        if i < self.h - 1:
            cells.append((i + 1, j))
        if i < self.h - 1 and j < self.w - 1:
            cells.append((i + 1, j + 1))
        return cells


size = 440, 640
screen = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()

board = Minesweeper(10, 15, 10)
board.set_view(20, 20, 40)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.process_click(event.pos)

    screen.fill((0, 0, 0))
    board.render(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
