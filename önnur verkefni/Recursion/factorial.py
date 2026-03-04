



def factorial(num: int) -> int:
    fact = 0
    if num == 0:
        return 1
    elif num <= 0:
        raise ValueError('factorial called on negative number')
    else:
        fact += num * factorial(num - 1)

    return fact


print(factorial(10))