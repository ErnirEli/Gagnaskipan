# Choose the one most appropriate of the following ADT for your implementation.
import dll
import stack
import queue
import deque
A = dll.DLList()
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
    
    _stack = stack.Stack(A)

    for letter in  s:
        if letter in '{[(':
            _stack.push(letter)
            continue
        elif _stack.is_empty() and letter in '}])':
            return False
        elif letter == '}':
            if _stack.top() != '{':
                return False
            _stack.pop()
        elif letter == ')':
            if _stack.top() != '(':
                return False
            _stack.pop()
        elif letter == ']':
            if _stack.top() != '[':
                return False
            _stack.pop()

    if not _stack.is_empty() or s == '':
        return False
    return True

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

