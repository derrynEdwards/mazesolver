# ~*~ coding: utf-8 ~*~
"""
    File name           : graphics.py
    Author              : Derryn Edwards
    Date Created        : 2023/08/12
    Date Last Modified  : 2023/08/12
    Python Version      : 3.11
"""
# ==================================================================================================
# IMPORTS
# ==================================================================================================
from tkinter import Tk, BOTH, Canvas


class Window:
    """
    A class used for creating a Tkinter Window.

    Attributes
    ----------
    __root : Tk Object
        tkinter Tk Object
    __canvas : Canvas Object
        tkinter Canvas object
    __running : bool
        boolean that states if window is still running or not

    Methods
    -------
    redraw(self)
        Update the window for continuous running.
    wait_for_close(self)
        Updates the __running attribute to True
        Keeps the window running with redraw()
    close(self)
        Updates the __running attribute to False for closing the window.
    """

    def __init__(self, width, height):
        """
        Parameters
        ----------
        width : int
            Width of the window
        height : int
            Height of the window
        """
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """Update the window for continuous running."""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """Updates the __running attribute to True. Keeps the window running with redraw()"""
        self.__running = True

        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        """Updates the __running attribute to False for closing the window."""
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        """
        Draws a line on the canvas by calling the Line class draw method.

        Parameters
        ----------
        line : Line Object
            Instance of Line Class
        fill_color : str
            String defining the color such as "black" or "red".
        """
        line.draw(self.__canvas, fill_color)


class Point:
    """
    A class used for creating Points.

    x = 0 is the left of the screen
    y = 0 is the top of the screen

    Attributes
    ----------
    x : int
        the x-coordinate (horizontal) in pixels of the point
    y : int
        the y-coordinate (vertical) in pixels of the point
    """

    def __init__(self, x=0, y=0):
        """
        Parameters
        ----------
        x : int
            the x-coordinate (horizontal) in pixels of the point
        y : int
            the y-coordinate (vertical) in pixels of the point
        """
        self.x = x
        self.y = y


class Line:
    """
    A class used for creating Lines by providing two Points.

    Attributes
    ----------
    __p1 : Point Object
        Starting point of the line.
    __p2 : Point Object
        Ending point of the line.

    Methods
    -------
    draw(self, canvas, fill_color)
        Draws a line on the canvas with the specified color.
    """

    def __init__(self, p1, p2):
        """
        Parameters
        ----------
        p1 : Point Object
            Starting point of the line.
        p2 : Point Object
            Ending point of the line.
        """
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas, fill_color="black"):
        """
        Draws a line on the canvas with the specified color.

        Parameters
        ----------
        canvas : Canvas Object
            Instance of Canvas for drawing the line on.
        fill_color : str
            String defining the color such as "black" or "red".
        """
        canvas.create_line(
            self.__p1.x,
            self.__p1.y,
            self.__p2.x,
            self.__p2.y,
            fill=fill_color,
            width=2
        )
        canvas.pack(fill=BOTH, expand=1)
