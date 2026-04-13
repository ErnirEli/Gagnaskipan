
opps = ('+', '/', '*', '-')
num = 0
variables = {}

while True:
    
    _input = input().split()


    if '=' in _input:
        variables[_input[0]] = int(_input[-1])

    else:
        if '/' in _input or '*' in _input:
            for k in _input:
                if k == '/':
                    x = _input.index('/')
                    a = _input[x - 1]
                    b = _input[x + 1]

                    try:
                        a = int(a)
                    except ValueError:
                        a = variables[a]

                    try:
                        b = int(b)
                    except ValueError:
                        b = variables[b]

                    _input[x-1 : x+2] = [str(a / b)]


                elif k == '*':
                    x = _input.index('*')
                    a = _input[x - 1]
                    b = _input[x + 1]

                    try:
                        a = int(a)
                    except ValueError:
                        a = variables[a]

                    try:
                        b = int(b)
                    except ValueError:
                        b = variables[b]

                    _input[x-1 : x + 2] = [str(a * b)]

        for k in range(len(_input) - 1, -1, -1):
            k = _input[k]
            if k in opps:
                if k == '+':
                    x = _input.index('+')
                    a = _input[x - 1]
                    b = _input[x + 1]
                    

                    try:
                        a = int(a)
                    except ValueError:
                        a = variables[a]

                    try:
                        b = int(b)
                    except ValueError:
                        b = variables[b]

                    _input[x-1 : x+2] = [str(a + b)]
                
                if k == '-':
                    x = _input.index('-')
                    a = _input[x - 1]
                    b = _input[x + 1]
                    

                    try:
                        a = int(a)
                    except ValueError:
                        a = variables[a]

                    try:
                        b = int(b)
                    except ValueError:
                        b = variables[b]

                    _input[x-1 : x+2] = [str(a - b)]

        break

print(_input[0])

