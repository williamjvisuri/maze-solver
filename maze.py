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
        self.__reset_cells_visited()

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
        time.sleep(0.01)

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
                self.__cells[i - 1][j].has_right_wall = False
            elif direction == (i, j - 1):
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False
            elif direction == (i + 1, j):
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            else:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
            self.__draw_cell(i, j)
            self.__break_walls_r(*direction)

    def __reset_cells_visited(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.__cells[col][row].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self.__cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            if self.num_cols - 1 >= i + direction[0] >= 0 and self.num_rows - 1 >= j + direction[1] >= 0:
                left_possible = (direction[0] == -1 and not self.__cells[i]
                                 [j].has_left_wall and not self.__cells[i - 1][j].has_right_wall and not self.__cells[i - 1][j].visited)
                up_possible = (direction[1] == -1 and not self.__cells[i]
                               [j].has_top_wall and not self.__cells[i][j - 1].has_bottom_wall and not self.__cells[i][j - 1].visited)
                right_possible = (direction[0] == 1 and not self.__cells[i]
                                  [j].has_right_wall and not self.__cells[i + 1][j].has_left_wall and not self.__cells[i + 1][j].visited)
                bottom_possible = (direction[1] == 1 and not self.__cells[i]
                                   [j].has_bottom_wall and not self.__cells[i][j + 1].has_top_wall and not self.__cells[i][j + 1].visited)
                if left_possible:
                    self.__cells[i][j].draw_move(self.__cells[i - 1][j])
                    if self._solve_r(i - 1, j):
                        return True
                    self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)
                elif up_possible:
                    self.__cells[i][j].draw_move(self.__cells[i][j - 1])
                    if self._solve_r(i, j - 1):
                        return True
                    self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)
                elif right_possible:
                    self.__cells[i][j].draw_move(self.__cells[i + 1][j])
                    if self._solve_r(i + 1, j):
                        return True
                    self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)
                elif bottom_possible:
                    self.__cells[i][j].draw_move(self.__cells[i][j + 1])
                    if self._solve_r(i, j + 1):
                        return True
                    self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)
        return False
