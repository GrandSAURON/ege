#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=6&mode=print
from itertools import product

x = list(product("magistr", repeat=5))
cnt = 0
for el in x:
    s = "".join(el)
    for ch in "magistr":
        if s.count(ch) > 1:
            break
    else:  
        if s.count("a") + s.count("i") <=  1:  
            cnt +=1
print(cnt)
