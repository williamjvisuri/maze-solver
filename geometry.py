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
