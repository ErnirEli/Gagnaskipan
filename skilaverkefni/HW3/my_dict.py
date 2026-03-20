#
# MyDict dictionary.
# Your name:
#  - <Ernir Elí Ellertsson>
#  - <Daníel Darri Ragnarsson>
#

from collections.abc import MutableMapping
from binary_search_tree import Pair, BinarySearchTree

class MyDict(MutableMapping):

    def __init__(self):
        self._bst = BinarySearchTree()  # Your BST, feel free to add more member variables as needed.
        # TO DO ...
        self._len = 0

    def __iter__(self):
        """
        Returns an iterator; note, for dictionaries one iterates on the keys (not key-value pairs)
        """
        return iter(self._bst.keys())

    def __str__(self):
        """
        Returns a string representation of the dictionary.
        """
        """
        Returns a string representation of the dictionary (in the same format as Python dict, e.g. {1: 755, 2: 290}
        """
        elements = []
        for elem in self._bst:
            elements.append(f'{elem.key}: {elem.value}')
        return '{' + ', '.join(elements) + '}'

    def __getitem__(self, key):
        """
        Returns the value at key entry, i.e. value = d[key].
        Raises KeyError if the key is not found.
        """
        # TO DO ...
        if self._bst.is_in(key):
            return self._bst.get(key)
        raise KeyError(key)
        

    def get(self, key, default=None):
        """
        Returns the value at key entry, i.e. value = d.get(key) ; or d.get(key,default) .
        Returns default if key not found.
        """
        # TO DO ...
        if self._bst.is_in(key):
            return self._bst.get(key)
        return default

    def __setitem__(self, key, value):
        """
        Sets the value at key entry, i.e. d[key] = value
        """
        # TO DO ...
        if self._bst.insert(Pair(key, value)):
            self._len += 1

    def __delitem__(self, key):
        """
        Returns the entry at kay, i.e. del d[key]
        """
        # TO DO ...
        if not self._bst.delete(key):
            raise KeyError(key)
        
        self._len -= 1

    def __len__(self):
        """
        Returns the number of entries in the dictionary.
        """
        # TO DO ...
        return self._len
