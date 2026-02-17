class NodeIterator:
    def __init__(self, node):
        self.__node = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.__node is None:
            raise StopIteration
        item = self.__node.item
        self.__node = self.__node.next
        return item
