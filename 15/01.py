def func(x, y, a):
    return (2 * x + 3 * y != 60) or (a >= x) or (a >= y)

def ok(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(func(x, y, a)):
                return False
    return True

for a in range(1, 100):
    if ok(a):
        print(a)