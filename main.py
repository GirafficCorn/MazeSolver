from window import Window
from line import Line, Point
from cell import Cell





def main():
    win = Window(800, 600)
    cell = Cell(50, 150, 50, 150, win)
    cell.draw()
    win.wait_for_close()




if __name__ == "__main__":
    main()
