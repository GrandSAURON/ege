def del_fun(n, m):
    if n % m == 0:
        return True

def func(x, A):
    return del_fun(x, A) or (not(del_fun(x, 21)) and not(del_fun(x, 35)))

def ok(A):
    for x in range(1, 1000):
        if not(func(x, A)):
            return False
    return True

for A in range(1, 1000):
    if ok(A):
        print(A)