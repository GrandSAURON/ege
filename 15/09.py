def del_func(n, m):
    if n % m == 0:
        return True
    return False


def func(x, A):
    return del_func(A, 45) and (not (del_func(750, x)) or (del_func(A, x) or not (del_func(120, x))))


def ok(A):
    for x in range(1, 10000):
        if not (func(x, A)):
            return False
    return True


for A in range(1, 10000):
    if ok(A):
        print(A)
