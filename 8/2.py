from itertools import product

x = list(product("оникс", repeat=6))
cnt = 0
for el in x:
    s = "".join(el)
    if s.count("с") == 3 and s.count("о") == 1:
        cnt += 1

print(cnt)
