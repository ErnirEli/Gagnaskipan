


class Stack():
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, item: object) -> None:
        '''
        Takes an object and puts it on thop of the stack
        
        :param item: Object that is to be put on top of the stack
        '''
        self.stack.append(item)

    def pop(self):
        '''
        Removes the top object from the stack and returns it
        
        :return: Returns the top object from the stack
        '''

        return self.stack.pop()
    
    def top(self):
        '''
        Returns the top object from the stack without remving it
        
        :return: Returns the top object from the stack
        '''

        return self.stack[-1]
    
    def is_empty(self) -> bool:
        '''
        A method that checks if the stack is empty and returns
        true if the stack is empty and returning false otherwise
        
        :return: Returns True if stack is empty, false otherwise
        :rtype: bool
        '''

        return len(self.stack) == 0
        
        
        
