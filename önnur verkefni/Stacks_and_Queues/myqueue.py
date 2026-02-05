
# End == 0 edge case & start == 0 edge case

class Queue:

    def __init__(self, capacity: int = 4):
        

        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.start = self.capacity - 1
        self.end = self.start - 1
        self.len = 0

    def __str__(self):
        string = ''

        return f'Queue({str(self.queue)})'

    def __double(self):
        capacity = self.capacity * 2
        temp_queue = [None] * self.capacity

        self.queue[self.end: self.start] =  temp_queue

        self.start += self.capacity
        self.capacity = capacity
        
        
        

    def enqueue(self, item: object) -> None:
        '''
        Takes an object and adds to the back of the queue

        :param item: Objects that is to be added to the queue
        :type item: object
        '''
        self.end += 1
        if self.end == len(self.queue):
            self.end = 0
        if self.queue[self.end] != None:
            self.__double()
        
        self.queue[self.end] = item
        self.len += 1

    def dequeue(self) -> object:
        
        item = self.queue[self.start]
        self.queue[self.start] = None
        
        self.start += 1
        if self.start == len(self.queue):
            self.start = 0

        self.len -= 1
        # if self.is_empty():
        #     print('hooray')
        #     self.start = self.end
        return item

    def front(self) -> object:

        return self.queue[self.start]
    
    def is_empty(self):
        return self.len == 0
    
    def is_full(self):
        return self.len == len(self.queue)
