from cell import Cell
from window import Window
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            cell_list = []
            for j in range(self.num_rows):
                cell_list.append(Cell(self._win))
            self._cells.append(cell_list)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        x1 = self._x1 + i * self.cell_size_x
        x2 = x1 + self.cell_size_x
        y1 = self._y1 + j * self.cell_size_y
        y2 = y1 + self.cell_size_y
        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(.05)


win = Window(800, 600)
test = Maze(100, 100, 10, 10, 50, 50, win)

cells = test._create_cells()
for i in cells: print(i)