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
    get_cells(self)
        Returns __cells attribute.
    """

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
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
        """
        self.__cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__create_cells()

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

    def get_cells(self):
        """Returns __cells attribute."""
        return self.__cells
