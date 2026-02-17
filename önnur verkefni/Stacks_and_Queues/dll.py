class Node:

    def __init__(self, element: object = None, prev = None, next = None):
        self._element = element
        self._prev = prev
        self._next = next


class DLL:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head._next = self.tail
        self.tail._prev = self.head
        self.curr = self.tail
        self.size = 0

    def __len__(self):
        return self.size
    
    def 
