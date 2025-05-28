from window import Window
from maze import Maze


def main():
    win = Window(1920, 1080)
    maze = Maze(50, 50, 20, 37, 50, 50, win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
