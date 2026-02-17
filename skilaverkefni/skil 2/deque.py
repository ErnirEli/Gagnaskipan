#
# Gagnaskipan.
# Deque implementation
# Student(s):
#  - ... your name ...
#
import sll
import dll

class Deque:

    def __init__(self, lst):
        """
        Constructor.
        """
        ...

    def __len__(self):
        """
        Returns the number of elements in the deque.
        :return: Number of elements.
        """
        ...
        return 0

    def __str__(self):
        """
        Returns the string representation of the deque.
        :return: String representation.
        """
        ...
        return ""

    def is_empty(self):
        """
        Returns True if the deque is empty, otherwise False.
        """
        ...
        return True

    def front(self):
        ...

    def back(self):
        ...

    def append(self, item):
        """
        Inserts the element to the right (top) of the deque.
        :return: None
        """
        ...

    def appendleft(self, item):
        """
        Inserts the element to the left (bottom) of the deque.
        :return: None
        """
        ...

    def pop(self):
        """
        Removes the element at the right (top) of the deque.
        :return: None. Raises an exception if empty.
        """
        ...

    def popleft(self):
        """
        Removes the element at the left (bottom) of the deque.
        :return: None. Raises an exception if empty.
        """
        ...

