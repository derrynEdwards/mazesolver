# ~*~ coding: utf-8 ~*~
"""
    File name           : maze.py
    Author              : Derryn Edwards
    Date Created        : 2023/08/12
    Date Last Modified  : 2023/08/12
    Python Version      : 3.11
"""
# ==================================================================================================
# IMPORTS
# ==================================================================================================
from cell import Cell
import time
import random


class Maze:
    """
    Holds all the cells in the maze in a 2-dimensional grid.

    Attributes
    ----------
    __x1 : int
        x-coordinate on where the Maze starts.
    __y1 : int
        y-coordinate on where the Maze starts.
    __num_rows : int
        Number of rows the maze will have.
    __num_cols : int
        Number of columns the maze will have.
    __cell_size_x : float
        Width of each cell.
    __cell_size_y : float
        Height of each cell.
    __win : Window object
        Default: None
        Instance of Window class.

    Methods
    -------
    __create_cells(self)
        Creates the cells of the maze in a 2-dimensional grid.
    __draw_cell(self, i, j)
        Method that draws the cells on the Maze.
    __animate(self)
        Allows to visualize what algorithms are doing in real time.
    __break_entrance_and_exit(self)
        Breaks wall on entrance and exit of maze.
    __break_walls_r(self, i, j)
        Recursive method that breaks walls in a breadth-first traversal.
    __reset_cells_visited(self)
        Resets all cells visited attribute to False.
    __solve_r(self, i, j)
        Recursive method that attempts to solve the maze.
    solve(self)
        Calls __solve_r method. Returns True if successful, otherwise False.
    get_cells(self)
        Returns __cells attribute.
    """

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        """
        Parameters
        ----------
        x1 : int
            x-coordinate on where the Maze starts.
        y1 : int
            y-coordinate on where the Maze starts.
        num_rows : int
            Number of rows the maze will have.
        num_cols : int
            Number of columns the maze will have.
        cell_size_x : float
            Width of each cell.
        cell_size_y : float
            Height of each cell.
        win : Window object
            Default: None
            Instance of Window class.
        seed : int
            Default: None
            Seed used for random generator.
        """
        self.__cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        if seed:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        """Creates the cells of the maze in a 2-dimensional grid."""
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        """
        Method that draws the cells on the Maze.

        Parameters
        ----------
        i: int
            Columns
        j: int
            Rows
        """
        if self.__win is None:
            return self

        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        """Allows to visualize what algorithms are doing in real time."""
        if self.__win is None:
            return

        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        """Breaks wall on entrance and exit of maze."""
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        """Recursive method that breaks walls in a breadth-first traversal."""
        self.__cells[i][j].visited = True

        while True:
            next_index_list = []
            possible_direction_indices = 0

            # check left
            if i > 0 and not self.__cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
                possible_direction_indices += 1
            # check right
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
                possible_direction_indices += 1
            # check up
            if j > 0 and not self.__cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
                possible_direction_indices += 1
            # check down
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
                possible_direction_indices += 1

            # if nowhere to go, break wall
            if possible_direction_indices == 0:
                self.__draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(possible_direction_indices)
            next_index = next_index_list[direction_index]

            # break walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self.__break_walls_r(next_index[0], next_index[1])

    def __reset_cells_visited(self):
        """Resets all cells visited attribute to False."""
        for col in self.__cells:
            for cell in col:
                cell.visited = False

    def __solve_r(self, i, j):
        """Recursive method that attempts to solve the maze."""
        self.__animate()

        # visit current cell
        self.__cells[i][j].visited = True

        # if at end cell, maze is solved!
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        # move left if no wall and not visited
        if (
                i > 0
                and not self.__cells[i][j].has_left_wall
                and not self.__cells[i - 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self.__solve_r(i - 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)

        # move right if no wall and not visited
        if (
                i < self.__num_cols - 1
                and not self.__cells[i][j].has_right_wall
                and not self.__cells[i + 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self.__solve_r(i + 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)

        # move up if no wall and not visited
        if (
                j > 0
                and not self.__cells[i][j].has_top_wall
                and not self.__cells[i][j - 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self.__solve_r(i, j - 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)

        # move down if no wall and not visited
        if (
                j < self.__num_rows - 1
                and not self.__cells[i][j].has_bottom_wall
                and not self.__cells[i][j + 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self.__solve_r(i, j + 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)

        # went wrong way; return False
        return False

    def solve(self):
        """Calls __solve_r method. Returns True if successful, otherwise False."""
        return self.__solve_r(0, 0)

    def get_cells(self):
        """Returns __cells attribute."""
        return self.__cells
