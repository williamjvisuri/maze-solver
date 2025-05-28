from cell import Cell
import time


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
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()
        self.___break_entrance_and_exit()

    def __create_cells(self):
        for col in range(self.num_cols):
            self.__cells.append(self.num_rows*[Cell(self.win)])
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
