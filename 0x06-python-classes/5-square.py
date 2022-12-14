#!/usr/bin/python3
"""Square Class

Square class

"""


class Square:
    """Square

    This class designs a square

    """

    def __init__(self, size=0):
        """__init__

        This method initializes the size value of the square

        Attributes:
            size (:obj:`int`, optional): size of the square

        Raises:
            TypeError: if `size` type is not `int`

            ValueError: if `size` is less than 0

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """size

        This setter method update the size value of the square

        Attributes:
            size (:obj: `int`): new size of the square

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

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        for i in range(1, self.area() + 1):
            print('#', end='')

            if i % self.__size == 0 and i > 0:
                print()
