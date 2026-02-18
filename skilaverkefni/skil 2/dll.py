#
# Gagnaskipan.
# Double-Linked-List
# Student(s):
#  - ... your name ...
#
from dll_node import Node
from iterator import NodeIterator

class Position:
    __slots__ = ['node']

    def __init__(self, node: Node):
        self.node = node


class DLList:

    #
    # Beginning of fundamental section.
    #

    def __init__(self):
        
        self._head = Node(None, None, None)
        self._tail = Node(None, None, None)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._len = 0


    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return: Iterator object.
        """
        return NodeIterator(self._head.next, self._tail)

    def __str__(self):
        """
        String representation of the list.
        Time complexity: O(n)
        :return: The string representation.
        """

        elems = []
        for item in self:
            elems.append(str(item))
        return '[' + ', '.join(elems) + ']'

    def __len__(self):
        """
        Returns the number of elements in the list.
        Time complexity: O(1)
        :return: Number of elements in the list.
        """
        return self._len

    def is_empty(self):
        """
        Checks if list is empty.
        Time complexity: O(1)
        :return: True if empty, otherwise false
        """
        return len(self) == 0

    def get_at(self, pos: Position) -> object:
        """
        Return element at position 'pos'.
        :param pos: Position to insert
        :return: Element
        """
            
        return pos.node.item

    def insert_after(self, pos: Position, item: object) -> Position:
        """
        Insert element following position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """
        new = self._insert_between(item, pos.node, pos.node.next)
        return Position(new)

    def insert_before(self, pos: Position, item: object) -> Position:
        """
        Insert element before position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """
        new = self._insert_between(item, pos.node.next, pos.node)
        return Position(new)

    def remove(self, pos: Position) -> object:
        """
        Remove element at position 'pos' in the list.
        :param pos: Position of element to remove.
        :return: Element deleted
        """
        pos.node.prev.next = pos.node.next
        pos.node.next.prev = pos.node.prev
        self._len -= 1
        return pos.node.item

    def replace(self, pos: Position, item: object) -> object:
        """
        Replace element at position 'pos' in the list.
        :param pos: Position of element to replace
        :param item: New element to replace the existing one.
        :return: The element replaced (formerly at position)
        """
        prev = pos.node.item
        pos.node.item = item
        return prev

    def front_pos(self) -> Position | None:
        """
        Return position of the element at the head of the list if list non-empty, or None if list is empty.
        """
        if self.is_empty():
            return None
        return self._head.next

    def back_pos(self) -> Position | None:
        """
        Return position of the element at the end of list if list non-empty, or None if list is empty.
        """
        if self.is_empty():
            return None
        return self._tail.prev

    def prev_pos(self, pos: Position) -> Position | None:
        """
        Return position before 'pos', or None if already at front of list.
        """
        if pos.node is self._head.next:
            return None
        return pos.node.prev

    def next_pos(self, pos: Position) -> Position | None:
        """
        Return position following 'pos', or None if already at end of list.
        """
        if pos.node is self._tail.prev:
            return None
        return pos.node.next

    #
    # End of fundamental section.
    # Implement the methods below by, for the most part, using/calling the ones you have implemented above.
    # Avoid unnecessary code duplication.
    #

    def front(self):
        """
        Returns the element at the front of the list.
        Time complexity: O(1)
        :return: If list non-empty, the front element, otherwise trows an exception.
        """
        if self.is_empty():
            return None
            raise IndexError('front called on an empty list')
        return self._head.next.item

    def back(self):
        """
        Returns the element at the back of the list.
        Time complexity: O(1)
        :return: If list non-empty, the back element, otherwise trows an exception.
        """
        if self.is_empty():
            return None
            raise IndexError('back called on an empty list')
        return self._tail.prev.item

    def push_front(self, item):
        """
        Insert an element to front of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        self._insert_between(item, self._head, self._head.next)

    def pop_front(self):
        """
        Remove an element from the front of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        if self.is_empty():
            raise IndexError('pop called on an empty list')
        self.remove(Position(self._head.next))
        

    def push_back(self, item):
        """
        Insert an element to back of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        self._insert_between(item, self._tail.prev, self._tail)

    def pop_back(self):
        """
        Remove an element from the back of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        if self.is_empty():
            raise IndexError('pop called on an empty list')
        self.remove(Position(self._tail.prev))


#
#
#
#
#

    def _insert_between(self, item: object, predecessor: Node, successor: Node):
        new = Node(predecessor, item, successor)

        predecessor.next = new
        successor.prev = new
        self._len += 1
        return new
    
