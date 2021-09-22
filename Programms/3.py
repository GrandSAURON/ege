a = input()
b = input()
c = min(a, b)
while True:
    if c % a == 0 and c % b == 0:
        break
    c += 1
print(c)