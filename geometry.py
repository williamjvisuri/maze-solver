class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, color="black"):
        canvas.create_line(self.point_a.x, self.point_a.y,
                           self.point_b.x, self.point_b.y, fill=color, width=2)


class Cell():
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1),
                        Point(self.__x1, self.__y2))
            self.__win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1),
                        Point(self.__x2, self.__y1))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1),
                        Point(self.__x2, self.__y2))
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2),
                        Point(self.__x2, self.__y2))
            self.__win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        color = "gray"
        if not undo:
            color = "red"
        x1 = (self.__x1 + self.__x2) / 2
        y1 = (self.__y1 + self.__y2) / 2
        x2 = (to_cell.__x1 + to_cell.__x2) / 2
        y2 = (to_cell.__y1 + to_cell.__y2) / 2
        self.__win.draw_line(Line(Point(x1, y1), Point(x2, y2)), color)
