from window import Window
from cell import Cell





def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.has_bottom_wall = False
    cell1 = Cell(win)
    cell1.has_top_wall = False
    cell.draw(50, 50, 100, 100)
    cell1.draw(200, 100, 300, 300)

    cell.draw_move(cell1, undo=True)
    win.wait_for_close()




if __name__ == "__main__":
    main()
