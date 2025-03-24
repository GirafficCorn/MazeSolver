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
            top_left = Point(self._x1, self._y1)
            bottom_left = Point(self._x1, self._y2)
            wall = Line(top_left, bottom_left)
            self._win.draw_line(wall, fill_color="red")

        if self.has_right_wall:
            top_right = Point(self._x2, self._y1)
            bottom_right = Point(self._x2, self._y2)
            wall = Line(top_right, bottom_right)
            self._win.draw_line(wall, fill_color="red")

        if self.has_top_wall:
            top_left = Point(self._x1, self._y1)
            top_right = Point(self._x2, self._y1)
            wall = Line(top_left, top_right)
            self._win.draw_line(wall, fill_color="red")

        if self.has_bottom_wall:
            bottom_left = Point(self._x1, self._y2)
            bottom_right = Point(self._x2, self._y2)
            wall = Line(bottom_left, bottom_right)
            self._win.draw_line(wall, fill_color="red")

