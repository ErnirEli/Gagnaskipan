import ctypes

class FixedSizeArray:

    """
        Fixed-size array (using the ctypes package to access the underlying C-code interface).
    """

    def __init__(self, capacity: int):
        """
        Creates an array of a fixed size, where each element is an object reference.
        :param capacity: array's capacity/size
        """
        if capacity <= 0:
            raise ValueError("FixedSizeArray capacity must be positive")
        self.__capacity = capacity
        self.__array = (ctypes.py_object * self.__capacity)()
        for i in range(self.__capacity):
            self.__array[i] = None   # Strictly speaking, not needed (NULL/None by default)

    def __getitem__(self, index: int):
        """
        Accessing an element at given index (x = A[index]).
        Time complexity: O(1)
        :param index
        :return Element at index (exception if index is out of range)
        """
        if index < 0 or index >= self.__capacity:
            raise IndexError("Index out of range")
        return self.__array[index]

    def __setitem__(self,index: int ,value: object):
        """
        Updating an element at given index (A[index] = x).
        Time complexity: O(1)
        :param index
        :return Element at index (exception if index is out of range)
        """
        if index < 0 or index >= self.__capacity:
            raise IndexError("Index out of range")
        self.__array[index] = value

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return:
        """
        self.__index = 0
        return self

    def __next__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return the element at index self.__index (exception if out of range)
        """
        if self.__index >= self.capacity():
            raise StopIteration
        elem = self.__array[self.__index]
        self.__index += 1
        return elem

    def capacity(self) -> int:
        """
        Returns the capacity of the array.
        :return: array's capacity
        """
        return self.__capacity



