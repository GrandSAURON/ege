def del_func(n, m):
    if n % m == 0:
        return True
    return False

def func(x, A):
    return del_func(x, A) or (not(del_func(x, 6)) or not(del_func(x, 9)))

def ok(A):
    for x in range(1, 100):
        if not(func(x, A)):
            return False
    return True

for A in range(1, 100):
    if ok(A):
        print(A)