import pygame


class Board:
    def __init__(self, width, height, mines):
        self.mines = mines
        self.width = width
        self.height = height
        self.board = [[0] * self.width for i in range(self.height)]

        self.need_get_teleport = False

        self.left_start = 20
        self.top_start = 20
        self.cell_size = 50

    def render(self, screen):
        screen.fill((0, 0, 0))
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.circle(screen, pygame.Color((0, 0, 255)),
                                       (self.cell_size * x + self.left_start + self.cell_size // 2,
                                        self.cell_size * y + self.top_start + self.cell_size // 2),
                                       self.cell_size // 2 - 2)
                elif self.board[y][x] == 2:
                    pygame.draw.circle(screen, pygame.Color((255, 0, 0)),
                                       (self.cell_size * x + self.left_start + self.cell_size // 2,
                                        self.cell_size * y + self.top_start + self.cell_size // 2),
                                       self.cell_size // 2 - 2)

                pygame.draw.rect(screen, pygame.Color((200, 200, 200)),
                                 (self.cell_size * x + self.left_start, self.cell_size * y + self.top_start,
                                  self.cell_size, self.cell_size), width=1)

    def find_red(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 2:
                    return (x, y)
        return None

    def on_click(self, cell):
        x, y = cell
        if not self.need_get_teleport:
            if self.board[y][x] == 0:
                if self.find_red() is None:
                    self.board[y][x] = 1
                else:
                    self.need_get_teleport = True
            elif self.board[y][x] == 1:
                red_coords = self.find_red()
                if red_coords is not None:
                    self.board[red_coords[1]][red_coords[0]] = 1
                self.board[y][x] = 2
            elif self.board[y][x] == 2:
                self.board[y][x] = 1

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left_start) // self.cell_size
        y = (mouse_pos[1] - self.top_start) // self.cell_size
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return None
        return x, y

    def check_click(self, mouse_cords):
        cell = self.get_cell(mouse_cords)
        if cell:
            self.on_click(cell)


class Lines(Board):
    def has_path(self, x1, y1, x2, y2):
        opened = [(y1, x1)]
        queue = [(y1, x1)]
        can_move = False
        if x1 != x2 or y1 != y2:
            while queue:
                cur_pos = queue.pop()
                y, x = cur_pos
                if y + 1 < self.height and (y + 1, x) not in opened and self.board[y + 1][x] != 1:
                    queue.append((y + 1, x))
                    opened.append((y + 1, x))

                if y - 1 >= 0 and (y - 1, x) not in opened and self.board[y - 1][x] != 1:
                    queue.append((y - 1, x))
                    opened.append((y - 1, x))

                if x - 1 >= 0 and (y, x - 1) not in opened and self.board[y][x - 1] != 1:
                    queue.append((y, x - 1))
                    opened.append((y, x - 1))

                if x + 1 < self.width and (y, x + 1) not in opened and self.board[y][x + 1] != 1:
                    queue.append((y, x + 1))
                    opened.append((y, x + 1))

                if (y2, x2) in opened:
                    can_move = True
                    break

        return can_move

    def teleport(self, x1, y1, x2, y2):
        self.board[y2][x2] = 1
        self.board[y1][x1] = 0
        self.need_get_teleport = False


lines = Lines(10, 10, 50)
run = True
pygame.init()
screen = pygame.display.set_mode((540, 540))
screen.fill((0, 0, 0))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            lines.check_click(event.pos)
            if lines.need_get_teleport:
                red_coords = lines.find_red()
                mouse_coords = lines.get_cell(event.pos)
                if mouse_coords is not None:
                    res = lines.has_path(red_coords[0], red_coords[1], mouse_coords[0], mouse_coords[1])
                    if res:
                        lines.teleport(red_coords[0], red_coords[1], mouse_coords[0], mouse_coords[1])
                    else:
                        lines.board[red_coords[1]][red_coords[0]] = 1
                        lines.need_get_teleport = False

    lines.render(screen)
    pygame.display.flip()
