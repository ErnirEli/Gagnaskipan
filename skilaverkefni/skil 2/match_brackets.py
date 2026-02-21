# Choose the one most appropriate of the following ADT for your implementation.
#  - Ernir Elí Ellertsson & Daníel Darri Ragnarsson

import stack
import queue
import deque

def match_brackets(s: str) -> bool:
    """
    Returns True if the sting has matching brackets, otherwise False.
    The program checks if for each bracket ( '(', '[' '}' ) there is a matching
    closing bracket. Note, the order and type of the brackets is important.
    For example, if you open a '(' and then a '[', then you need to "close" first
    the ']' before the ')'.
    An example of a matching bracket sting is for example
        "(a [b (c {dd} ) ] [2] )"
    where the following strings are not:
        "(a [b ) ]"  <--- closes [ with a )
        "]b ["   <--- close with ] before opening
        "{{ a }"   <-- missing }
    """
    A = stack.dll.DLList()
    _stack = stack.Stack(A)
    matching = {'}':'{', ']':'[', ')':'('}
    for letter in  s:
        if letter in matching.values():
            _stack.push(letter)
        elif letter in matching.keys():
            if _stack.is_empty() or matching[letter] != _stack.top():
                return False
            _stack.pop()
            
    if _stack.is_empty():
        return True
    return False

def main():
    name = 'brackets.txt'
    try:
        with open(name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                print(f'{line:40} {match_brackets(line)}')
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

