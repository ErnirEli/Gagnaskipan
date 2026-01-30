from fixarray import FixedSizeArray
import collections
from collections.abc import Iterable

class DAList:
    """
    Dynamic array (mimicking most of Python's list behavior).
    """

    ##############################################################################################################
    # Part 1 section
    ##############################################################################################################

    def __init__(self, capacity: int = 4):
        """
        Constructor
        Time complexity: O(n)
        :param capacity:
        """

        # Define class variables
        self.__original_capacity: int = capacity
        self.capacity: int = capacity
        self.__array = FixedSizeArray(self.capacity)
        self.__lenght: int = 0

    def __len__(self) -> int:
        """
        Returns the number of elements in the array ( ... = len(A))
        Time Complexity: O(1) Worst case
        :return: number of elements
        """

        return self.__lenght

    def __getitem__(self, index: int):
        """
        Accessing an element at given index (... = A[index]).
        Time complexity: O(1)
        :param index
        :return Element at index (exception if index is out of range)
        """

        # Validate Index
        index = self.__index_validation(index)

        return self.__array[index]

    def __setitem__(self, index: int ,value: object):
        """
        Updating an element at given index (A[index] = value).
        Time complexity: O(1) Worst cse
        :param index:
        """
        # Validate Index
        index = self.__index_validation(index)
        
        # Update array
        self.__array[index] = value
        

    def __str__(self) -> str:
        """
        Returns a string representation of the array, e.g, [1, 2, 3] (str(A))
        Time complexity: O(n) Worst case
        :return: string representation
        """

        # Define string
        string = "["

        for k in range(len(self)):

            # Check for element location and create new string
            if k == len(self) - 1:
                string += str(self.__array[k])

            else:
                string += str(self.__array[k]) + ", "

        # Close and return string
        string +=  "]"
        return string

    def __delitem__(self, index: int):
        """
        Delete an element at given index (del A[index]).
        Time complexity: O(n) Worst Case
        :param index
        """

        # Validade index
        index = self.__index_validation(index)
        
        #Shift, remove item & update length
        self.__array[index] = None
        self.__lenght -= 1
        self.__shift(index, len(self), 1)
        
    

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: O(1) Worst case
        :return self
        """
        # Set starting index
        self.__index = 0

        return self
        

    def __next__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        Time complexity: O(1) Worst case
        :return the element at index self.__index (exception if out of range)
        """
        # Check if valid
        if self.__index >= len(self):
            raise StopIteration
        
        # Find element at index
        value = self.__array[self.__index]
        self.__index += 1

        # Return found value
        return value


    def clear(self):
        """
        Clears the array. Ensure you clear the references to the cleared object (such that the garbage collector
        can reclaim them).
        Time complexity: O(1) Worst case
        """

        # New array and updated length & capacity
        self.__array = FixedSizeArray(self.__original_capacity)
        self.__lenght = 0
        self.capacity = self.__original_capacity

    def count(self, value: object) -> int:
        """
        Counts the number of times an element 'value' appears in the list.
        Time complexity: O(n) Worst case
        :return: number of times value appears
        """

        # Create counter = 0
        counter: int = 0

        for k in range(len(self)):
            if self.__array[k] == value:
                # Update counter if value is found
                counter += 1

        # Return counter = times value was found
        return counter

    def index(self, value: object) -> int:
        """
        Returns the index of the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: O(n) Worst case
        :param value: The value to look for
        :return:  index of first occurrence in list
        """
        
        for index in range(len(self)):
            if self.__array[index] == value:
                # Return index when value was found
                return index
        
        else: # Raise error if value not found
            raise ValueError(f"{value} is not in list")

        
        

    def insert(self, index: int, value: object):
        """
        Inserts the element 'value' at position index in the array (shifting the subsequent items).
        Time complexity: O(n) Worst case
        :param index: position where to append the element.
        :param value: element to append
        """
        
        # Account for minus indexing
        if index < 0: 
            index = max(0, index + len(self))

        # Check if I can just append
        elif len(self) <= index:
            self.append(value)
            return

        # Extend capacity if needed
        if len(self) == self.capacity:
            self.__double()

        # Shift, update Array and variables
        self.__shift(len(self), index, -1)
        self.__array[index] = value
        self.__lenght += 1


    def reverse(self):
        """
        Reverses the array 'in place', e.g. [1, 2, 3] becomes [3, 2, 1].
        Time complexity: O(n) Worst case
        """

        # Last element index
        back_idx: int = len(self) - 1

        for front_idx in range(round(len(self) / 2)):
            
            #Store front and curresponding back element as varebles
            new_back = self.__array[front_idx]    
            new_front = self.__array[back_idx]

            # Swap elements and update
            self.__array[front_idx] = new_front    
            self.__array[back_idx] = new_back

            # Update back element index
            back_idx -= 1
            


    ##############################################################################################################
    # Part 2 section
    ##############################################################################################################

    def append(self, value: object):
        """
        Appends the element 'value' to the end of the array. Doubles the capacity of the array
        if it is already full before inserting an element.
        Time complexity: O(n) Worst Case
        Time complexity: O(1) Amortized 
        :param value: element to append
        """

        # Update capacity if needed
        if len(self) == self.capacity:
            self.__double()

        # Update array and variables
        self.__array[len(self)] = value
        self.__lenght += 1

    def copy(self):
        """
        Returns a shallow copy of the array.
        Time complexity: O(n) Worst case
        :return: copy of array
        """
        # Create a new array
        copy = DAList(self.capacity)

        # Take everyting old array has and put also on new array
        for k in range(len(self)):
            copy.append(self.__array[k])

        return copy

    def extend(self, iterable: Iterable):
        """
        Extends the array with the elements from iterable.
        Time complexity: O(n) Worst case
        :param iterable: An iterable object (e.g., a list)
        """

        # Append all things in iterable
        for k in iterable:
            self.append(k)

    def pop(self, index: int):
        """
        Remove the element at a given index from the array
        Time complexity: O(n) Worst case
        :param index: position of element to remove
        :return: the poped element
        """

        # Valisate index
        index = self.__index_validation(index)
        
        # Update array
        value = self.__array[index]
        del self[index]

        return value


    def remove(self, value: object):
        """
        Removes the first occurrence of element 'value' in the array, or raises ValueError if not found.
        Time complexity: O(n) Worst case
        :param value: The value to remove
        """
        # Iterate to find Value
        for k in range(len(self)):
            if self.__array[k] == value:
                # Delete if found
                del self[k]
                break
        else: # Raise error if not found
            raise ValueError(f"{value} is not in list")
        
        


    ##############################################################################################################
    # More made by us
    ##############################################################################################################

    def __double(self) -> None:
        """
        Doubles the arrays capacity, if its length has reached it maximum capacity and more is needed.
        Time complexity: O(n) Worst case
        :param self: 
        """

        # New array with double capacity
        self.capacity *= 2
        new = FixedSizeArray(self.capacity)

        # New array gets all elements from old array
        for k in range(len(self)):
            new[k] = self.__array[k]

        # Udate array
        self.__array = new
        # self.__array.__capacity = self.capacity

        return
    
    def __shift(self, start: int, stop: int, move: int) -> None:
        """
        Shifts part of the array to the left or the right if neccesary, after an item has been removed or added
        Time Complexity: O(n) Worst case
        :param self: 
        :param start: The index of  the first item that needs to be moved
        :param stop: The index of the last item that has to be removed
        :param move: The Direction items are going to be moved in (1 / -1)
        """

        # Shifts what needs to be shifted
        for k in range(start, stop, move):
                self.__array[k] = self.__array[k + move]

        return


    def __index_validation(self, index: int) -> int:
        """
        Docstring for __index_validation
        Time Complexity: O(1) Worst case
        :param self: 
        :param index: The Index that needs validation and maby modication if its less than 0
        :return: The Validated index
        """
        # Account for minus indexing
        if index < 0:
            index += len(self)

        # Check for valid range
        if index < 0 or index >= len(self):
            raise IndexError('Index out of range')
        
        # Return valid index
        return index