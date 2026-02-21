#
# Gagnaskipan.
# Deque implementation
# Student(s):
#  - Ernir Elí Ellertsson
#
import sll
import dll

class Deque:

    def __init__(self, lst: sll.SLList | dll.DLList | None = None):
        """
        Constructor.
        """
        
        if lst is None:
            self._lst = dll.DLList()
        else:
            self._lst = lst

    def __len__(self):
        """
        Returns the number of elements in the deque.
        :return: Number of elements.
        """
        
        return len(self._lst)

    def __str__(self):
        """
        Returns the string representation of the deque.
        :return: String representation.
        """
        
        return str(self._lst)

    def is_empty(self):
        """
        Returns True if the deque is empty, otherwise False.
        """
        return self._lst.is_empty()

    def front(self):
        return self._lst.front()

    def back(self):
        return self._lst.back()

    def append(self, item):
        """
        Inserts the element to the right (top) of the deque.
        :return: None
        """
        self._lst.push_back(item)

    def appendleft(self, item):
        """
        Inserts the element to the left (bottom) of the deque.
        :return: None
        """
        self._lst.push_front(item)

    def pop(self):
        """
        Removes the element at the right (top) of the deque.
        :return: None. Raises an exception if empty.
        """
        self._lst.pop_back()

    def popleft(self):
        """
        Removes the element at the left (bottom) of the deque.
        :return: None. Raises an exception if empty.
        """
        self._lst.pop_front()

