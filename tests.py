# ~*~ coding: utf-8 ~*~
"""
    File name           : tests.py
    Author              : Derryn Edwards
    Date Created        : 2023/08/12
    Date Last Modified  : 2023/08/12
    Python Version      : 3.11
"""
# ==================================================================================================
# IMPORTS
# ==================================================================================================
import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.get_cells()),
            num_cols,
        )
        self.assertEqual(
            len(m1.get_cells()[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.get_cells()),
            num_cols,
        )
        self.assertEqual(
            len(m1.get_cells()[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1.get_cells()[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1.get_cells()[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )


if __name__ == "__main__":
    unittest.main()
