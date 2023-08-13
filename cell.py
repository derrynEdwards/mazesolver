# ~*~ coding: utf-8 ~*~
"""
    File name           : cell.py
    Author              : Derryn Edwards
    Date Created        : 2023/08/12
    Date Last Modified  : 2023/08/12
    Python Version      : 3.11
"""
# ==================================================================================================
# IMPORTS
# ==================================================================================================
from graphics import Line, Point


class Cell:
    """
    A class used for creating Cells.

    Attributes
    ----------
    has_left_wall : bool
        Boolean referencing left wall of the Cell. Defaults to True.
    has_right_wall : bool
        Boolean referencing right wall of the Cell. Defaults to True.
    has_top_wall : bool
        Boolean referencing top wall of the Cell. Defaults to True.
    has_bottom_wall : bool
        Boolean referencing bottom wall of the Cell. Defaults to True.
    visited : bool
        Boolean that checks if the Cell has been visited. Defaults to False.
    __x1 : int
        x coordinate for Point 1
    __x2 : int
        x coordinate for Point 2
    __y1 : int
        y coordinate for Point 1
    __y2 : int
        y coordinate for Point 2
    __win : Window Object
        Default: None
        Instance of Window class for drawing.

    Methods
    -------
    draw(self, x1, y1, x2, y2)
        Draws a Cell on the provided Window Object.
    draw_move(self, to_cell, undo=False)
        Draws a line between the center of 2 cells as a Path.
    """

    def __init__(self, window=None):
        """
        Parameters
        ----------
        window : Window Object
            Default: None
            Instance of Window class for drawing.
        """
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        """
        Draws a Cell on the provided Window Object.

        Parameters
        ----------
        x1 : int
            x coordinate for Point 1
        x2 : int
            x coordinate for Point 2
        y1 : int
            y coordinate for Point 1
        y2 : int
            y coordinate for Point 2
        """
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")

    def draw_move(self, to_cell, undo=False):
        """
        Draws a line between the center of 2 cells as a Path.

        Parameters
        ----------
        to_cell : Cell Object
            Instance of Cell Class on where to move to.
        undo : bool
            Identifier for backtracking. Change line fill_color.
        """
        if self.__win is None:
            return

        x_mid = (self.__x1 + self.__x2) / 2
        y_mid = (self.__y1 + self.__y2) / 2
        to_x_mid = (to_cell.__x1 + to_cell.__x2) / 2
        to_y_mid = (to_cell.__y1 + to_cell.__y2) / 2
        fill_color = "red"

        if undo:
            fill_color = "gray"

        # moving left
        if self.__x1 > to_cell.__x1:
            self.__win.draw_line(
                Line(Point(self.__x1, y_mid), Point(x_mid, y_mid)), fill_color
            )
            self.__win.draw_line(
                Line(Point(to_x_mid, to_y_mid), Point(to_cell.__x2, to_y_mid)), fill_color
            )
        # moving right
        elif self.__x1 < to_cell.__x1:
            self.__win.draw_line(
                Line(Point(x_mid, y_mid), Point(self.__x2, y_mid)), fill_color
            )
            self.__win.draw_line(
                Line(Point(to_cell.__x1, to_y_mid), Point(to_x_mid, to_y_mid)), fill_color
            )
        # moving up
        elif self.__y1 > to_cell.__y1:
            self.__win.draw_line(
                Line(Point(x_mid, y_mid), Point(x_mid, self.__y1)), fill_color
            )
            self.__win.draw_line(
                Line(Point(to_x_mid, to_cell.__y2), Point(to_x_mid, to_y_mid)), fill_color
            )
        # moving down
        elif self.__y1 < to_cell.__y1:
            self.__win.draw_line(
                Line(Point(x_mid, y_mid), Point(x_mid, self.__y2)), fill_color
            )
            self.__win.draw_line(
                Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell.__y1)), fill_color
            )