


def power(base: int, exp: int) -> int:
    num = base
    if exp == 1:
        return base
    else:
        num *= power(base, exp -1)

    return num

print(power(3, 3))