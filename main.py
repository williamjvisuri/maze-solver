from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white",
                               width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, color="black"):
        line.draw(self.__canvas, color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, color):
        canvas.create_line(self.point_a.x, self.point_a.y,
                           self.point_b.x, self.point_b.y, fill=color, width=2)


def main():
    win = Window(800, 600)
    point_a = Point(50, 50)
    point_b = Point(150, 150)
    line = Line(point_a, point_b)
    win.draw_line(line, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
