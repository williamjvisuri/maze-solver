from geometry import Line, Point


class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win is None:
            return
        left_wall = Line(Point(self.__x1, self.__y1),
                         Point(self.__x1, self.__y2))
        top_wall = Line(Point(self.__x1, self.__y1),
                        Point(self.__x2, self.__y1))
        right_wall = Line(Point(self.__x2, self.__y1),
                          Point(self.__x2, self.__y2))
        bottom_wall = Line(Point(self.__x1, self.__y2),
                           Point(self.__x2, self.__y2))
        if self.has_left_wall:
            self.__win.draw_line(left_wall, "black")
        else:
            self.__win.draw_line(left_wall, "white")
        if self.has_top_wall:
            self.__win.draw_line(top_wall, "black")
        else:
            self.__win.draw_line(top_wall, "white")
        if self.has_right_wall:
            self.__win.draw_line(right_wall, "black")
        else:
            self.__win.draw_line(right_wall, "white")
        if self.has_bottom_wall:
            self.__win.draw_line(bottom_wall, "black")
        else:
            self.__win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if not undo:
            color = "green"
        x1 = (self.__x1 + self.__x2) / 2
        y1 = (self.__y1 + self.__y2) / 2
        x2 = (to_cell.__x1 + to_cell.__x2) / 2
        y2 = (to_cell.__y1 + to_cell.__y2) / 2
        if self.__win is None:
            return
        self.__win.draw_line(Line(Point(x1, y1), Point(x2, y2)), color)

    def __repr__(self):
        return f"{self.visited}"
