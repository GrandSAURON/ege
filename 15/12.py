def func(x, y, A):
    return (x * y < 140) or (y > A) or (x > A)

def ok(A):
    for x in range(1, 100):
        for y in range(1, 100):
            if not (func(x, y, A)):
                return False
    return True

for A in range(1, 100):
    if ok(A):
        print(A)

