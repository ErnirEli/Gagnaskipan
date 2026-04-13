from stack import Stack

s = Stack()
opps = ('+', '/', '*', '-')
num = 0
variables = {}

while True:
    
    _input = input().split()


    if '=' in _input:
        variables[_input[0]] = int(_input[-1])

    else:
        for _ in _input:
            if _ in opps:
                if len(s) < 2:
                    print(s)
                    raise Exception
                
                a = s.top()
                s.pop()
                b = s.top()
                s.pop()
                
                if _ == '+':
                    num = a + b

                elif _ == '-':
                    num = b - a

                elif _ == '*':
                    num = a * b

                else:
                    num = b / a

                s.push(num)

            elif _.isnumeric():
                s.push(int(_))
            
            if _ in variables:
                s.push(variables[_])

        break

print(s.top())
            