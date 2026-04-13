## 1: (Problem 1.7.3) Python Comprehensions: Function Composition
def my_function_composition(f, g):
    
    f: dict = f
    g: dict = g

    composition: dict = {}

    for _input, _output in f.items():
        
        if _output in g:
            composition[_input] = g[_output]

    return composition
        

## 2: Image of a function
def image(f: dict, D):
    
    f: dict = f
    D: set = D

    images: list = []

    for _input, _output in f.items():
        if _input in D:
            images.append(_output)

    return set(images)
        
        
## 3: Image cardinality of a function
def image_cardinality(f, D):
    
    f: dict = f
    D: set = D

    images: list = []

    for _input, _output in f.items():
        if _input in D:
            images.append(_output)

    return len(set(images))


## 4: One-to-one functions
def is_one_to_one(f, D):
    
    f: dict = f
    D: set = D

    if len(list(f.values())) != len(set(f.values())):
        return False
    
    return True
    

## 5: Onto functions

def is_onto(f, D, C):
    
    f: dict = f
    D: set = D
    C: set = C
    dupe: set = C.copy()
    

    for _input, _output in f.items():
        if _input in D and _output in dupe:
                # continue
                D.remove(_input)
                C.discard(_output)

    print(D)
    print(C)
    return D == C


## 6: Invertible functions
def is_invertible(f, D, C):
    
    f: dict = f
    D: set = D
    C: set = C



    if is_one_to_one(f, D) and is_onto(f, D, C):
        return True
    return False


## 7: Caesar Cipher Encoder
def encode(s):
    
    s: str = s
    encoded: str = ""

    for letter in s:
        num: int = ord(letter)
        num += 3

        if num > 90:
            num -= 26

        encoded += chr(num)

    return encoded        


## 8: Caesar Cipher Decoder
def decode(s):
    
    s: str = s
    decoded: str = ""

    for letter in s:
        num: int = ord(letter)
        num -= 3

        if num < 65:
            num += 26

        decoded += chr(num)

    return decoded




print('-2'.isnumeric())