#!/bin/usr/python3
"""Square Class

Square class

"""


class Square:
    """Square

    This class designs a square

    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__

        This method initializes the size value of the square

        Attributes:
            size (:obj:`int`, optional): size of the square
            position (obj: `tuple`): position of square

        Raises:
            TypeError: if `size` type is not `int`

            ValueError: if `size` is less than 0

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        if self.__check_tuple(position) is False \
                or self.__check_indexes(position) is False \
                or self.__check_integers(position) is False \
                or self.__check_values(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        """position

        This setter method update the position value of the square

        Attributes:
            position (:obj: `int`): position of square

        Raises:
            TypeError: if position is not a tuple of 2 positive integers

        """

        if self.__check_tuple(position) is False \
                or self.__check_indexes(position) is False \
                or self.__check_integers(position) is False \
                or self.__check_values(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def __check_tuple(self, position):
        if type(position) is tuple:
            return True

        return False

    def __check_indexes(self, position):
        if len(position) == 2:
            return True

        return False

    def __check_integers(self, position):
        if type(position[0]) is int and type(position[1]) is int:
            return True

        return False

    def __check_values(self, position):
        if position[0] >= 0 and position[1] >= 0:
            return True

        return False

    def area(self):
        """area

        This method returns the current square area

        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if j % self.__size == 0 and j > 0:
                print()
