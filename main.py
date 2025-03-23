from window import Window
from line import Line, Point





def main():
    point1 = Point(100, 100)
    point2 = Point(700, 500)
    line = Line(point1, point2)
    win = Window(800, 600)
    win.draw_line(line, "red")
    win.wait_for_close()




if __name__ == "__main__":
    main()
