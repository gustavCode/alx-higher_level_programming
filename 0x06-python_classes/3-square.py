#!/usr/bin/python3
class Square:
    """Square Class

    This class designs a square

    """
    
    def __init__(self, size=0):
        """__init__

        This method initializes the size value of the square.

        Attributes:
            size (:obj:`int`, optional): size of the square

        Raises:
            TypeError: if `size` type is not `int`

            ValueError: if `size` is less than `0`

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """area

        This method returns the current square area

        """
        return self.__size ** 2
