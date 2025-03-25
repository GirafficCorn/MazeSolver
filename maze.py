from cell import Cell
import time
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        

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
        time.sleep(.01)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self.num_cols - 1][self.num_rows - 1]
        entrance.has_top_wall = False
        self._draw_cell(0, 0)
        exit.has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            left = None
            right = None
            top = None
            bottom = None
            if i - 1 >= 0:
                left = i - 1
            if i + 1 < self.num_cols:
                right = i + 1
            if j - 1 >= 0:
                top = j - 1
            if j + 1 < self.num_rows:
                bottom = j + 1
            if left is not None and self._cells[left][j].visited is False:
                to_visit.append((left, j))
            if right is not None and self._cells[right][j].visited is False:
                to_visit.append((right, j))
            if top is not None and self._cells[i][top].visited is False:
                to_visit.append((i, top))
            if bottom is not None and self._cells[i][bottom].visited is False:
                to_visit.append((i, bottom))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            random_direction = random.randrange(len(to_visit))
            new_i = to_visit[random_direction][0]
            new_j = to_visit[random_direction][1]
            if i == new_i:
                if j + 1 == new_j:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][new_j].has_top_wall = False
                else:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][new_j].has_bottom_wall = False
            if j == new_j:
                if i + 1 == new_i:
                    self._cells[i][j].has_right_wall = False
                    self._cells[new_i][j].has_left_wall = False
                else:
                    self._cells[i][j].has_left_wall = False
                    self._cells[new_i][new_j].has_right_wall = False
            self._break_walls_r(new_i, new_j)


