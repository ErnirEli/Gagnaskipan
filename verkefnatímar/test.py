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


print(
    is_onto
    ({21: 'N', 25: 'J', 2: 'G', 8: 'f', 15: 'K', 13: 'g', 24: 'c', 12: 'L', 7: 'v', 3: 'X', 9: 'W', 14: 'N', 17: 'r', 16: 'o', 18: 'q', 0: 'V', 4: 'j', 20: 'E', 1: 'P', 10: 'z', 23: 'F', 11: 'i', 5: 'H', 22: 'm', 19: 'Q', 6: 'I'},
    {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25},
    {'K', 'L', 'E', 'f', 'g', 'v', 'c', 'J', 'I', 'P', 'V', 'r', 'N', 'j', 'o', 'F', 'i', 'W', 'Q', 'z', 'm', 'H', 'X'})
    )


