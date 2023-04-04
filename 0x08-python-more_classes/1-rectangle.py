#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width=0, height=0):
        """initializing this rectangle class
        Args:
            width: width of rectangle
            height: height of rectangle
        Raises:
            typeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width attribute"""
         if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height


    @height.setter
     def height(self, value):
        if not isinstance(value, int):
                raise TypeError("height must be an integer")
        if value < 0:
                raise ValueError("width must be greater than 0")
        self.__height = value
