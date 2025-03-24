from window import Window
from line import *

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            top_left = Point(x1, y1)
            bottom_left = Point(x1, y2)
            wall = Line(top_left, bottom_left)
            self._win.draw_line(wall)

        if self.has_right_wall:
            top_right = Point(x2, y1)
            bottom_right = Point(x2, y2)
            wall = Line(top_right, bottom_right)
            self._win.draw_line(wall)

        if self.has_top_wall:
            top_left = Point(x1, y1)
            top_right = Point(x2, y1)
            wall = Line(top_left, top_right)
            self._win.draw_line(wall)

        if self.has_bottom_wall:
            bottom_left = Point(x1, y2)
            bottom_right = Point(x2, y2)
            wall = Line(bottom_left, bottom_right)
            self._win.draw_line(wall)

    def draw_move(self, to_cell, undo=False):
        from_x = ((self._x1 + self._x2) / 2)
        from_y = ((self._y1 + self._y2) / 2)
        to_x = ((to_cell._x1 + to_cell._x2) / 2)
        to_y = ((to_cell._y1 + to_cell._y2) / 2)

        line = Line(Point(from_x, from_y), Point(to_x, to_y))
        color = None
        if undo == False:
            color = "grey"
        else:
            color = "red"
        self._win.draw_line(line, color)



