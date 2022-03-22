def func(x, y, A):
    return (3*x + 4*y != 70) or (A > x) or (A > y)

def ok(A):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(func(x, y, A)):
                return False
    return True

for A in range(1, 100):
    if ok(A):
        print(A)