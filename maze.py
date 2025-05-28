from cell import Cell
import time
import random


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self.__cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)
        self.__create_cells()
        self.___break_entrance_and_exit()
        self.__break_walls_r(0, 0)

    def __create_cells(self):
        for col in range(self.num_cols):
            cur_row = []
            for row in range(self.num_rows):
                cur_row.append(Cell(self.win))
            self.__cells.append(cur_row)
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.__draw_cell(col, row)

    def __draw_cell(self, i, j):
        x = self.cell_size_x * i + self.x1
        y = self.cell_size_y * j + self.y1
        if self.win is None:
            return
        self.__cells[i][j].draw(
            x, y, x + self.cell_size_x, y + self.cell_size_y)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def ___break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.num_cols - 1][self.num_rows -
                                        1].has_bottom_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self.__cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
            direction = random.choice(to_visit)
            if direction == (i - 1, j):
                self.__cells[i][j].has_left_wall = False
            elif direction == (i, j - 1):
                self.__cells[i][j].has_top_wall = False
            elif direction == (i + 1, j):
                self.__cells[i][j].has_right_wall = False
            else:
                self.__cells[i][j].has_bottom_wall = False
            self.__draw_cell(i, j)
            self.__break_walls_r(*direction)
