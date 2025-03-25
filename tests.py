import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 12
        nums_rows = 10
        m1 = Maze(0, 0, nums_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells), num_cols
        )

    def test_maze_create_negatives(self):
        win = Window(800, 600)
        num_cols = 10
        nums_rows = 10
        m1 = Maze(-10, -10, nums_rows, num_cols, -10, -10, win)
        self.assertEqual(
            len(m1._cells), num_cols
        )

    def test_break_entrance_and_exit(self):
        win = Window(800, 600)
        num_cols = 10
        nums_rows = 10
        m1 = Maze(10, 10, nums_rows, num_cols, 10, 10, win)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)


if __name__ == "__main__":
    unittest.main()