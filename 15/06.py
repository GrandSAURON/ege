def func(x, y, A):
    return (3*x + 4*y != 60) or ((A >= x) and (A >= y))

def ok(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(func(x, y, A)):
                return False
    return True

for A in range(1, 1000):
    if ok(A):
        print(A)