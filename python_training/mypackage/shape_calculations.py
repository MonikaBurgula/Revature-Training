""" Area, Circumference of SQ, RECT, CIRCLE """

from math import pi

def area_of_square(side):
    """
    Area of Square
    :param side: side of square
    :return: area of square
    """
    return side * side


def area_of_circle(radius):
    """
    Area of Circle
    :param radius: radius of circle
    :return: area of circle
    """
    return pi * radius * radius


def area_of_rect(length, brd):
    """ Area of Rectangle
    :param len: length of rectangle
    :param brd: breadth of rectangle"""
    return length * brd
