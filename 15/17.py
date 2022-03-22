def func(x, A):
    return not(x&17 == 0) or (not(x&29 != 0) or (x&A != 0))

def ok(A):
    for x in range(1, 100):
        if not(func(x, A)):
            return False
    return True

for A in range(1,100):
    if ok(A):
        print(A)