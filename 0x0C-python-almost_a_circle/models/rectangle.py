#!/usr/bin/python3
'''
This module contains the Rectangle Class.
'''
from models.base import Base


class Rectangle(Base):
    '''
    The rectangle class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constrictor method for the Rectangle class
        Args:
            width (int): The width of the rectangle instance
            height (int): The height of the rectangle instance
            x:
            y:
            id (int): The id of the instance
        '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''
        Getter method for width
        Returns:
            The width of the Rectangle instance
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter method for the width
        Args:
            value (int): The value to be set as the width
        '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        Getter method for height
        Returns:
            The height of the Rectangle instance
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter method for the height
        Args:
            value (int): The value to be set as the width
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        Getter method for x
        Returns:
            The value of x
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter methos for the width
        Args:
            value (int): The value to be set as x
        '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        Getter method for width
        Returns:
            The value of y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter methos for the width
        Args:
            value (int): The value to be set as y
        '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__y = value
