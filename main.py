from window import Window
from cell import Cell
from maze import Maze





def main():
    win = Window(800, 600)
    
    maze = Maze(50, 50, 12, 16, 20, 20, win)

    win.wait_for_close()




if __name__ == "__main__":
    main()
