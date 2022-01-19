# ВЫВОДИТ ВСЕ ВОЗМОЖНЫЕ КОМБИНАЦИИ ДЛИНОЙ REPEAT = 6
# БУКВЫ НЕ ДОЛЖНЫ ПОВТОРЯТЬСЯ ВО ВХОДНОЙ СТРОКЕ СИМВОЛОВ ДЛЯ ПЕРЕБОРА
from itertools import product

x = list(product("abcd", repeat=6))
cnt = 0
for el in x:
    s = "".join(el)
    print(s)
