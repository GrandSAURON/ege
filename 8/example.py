# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=20&mode=print
# ВЫВОДИТ ВСЕ ВОЗМОЖНЫЕ КОМБИНАЦИИ ДЛИНОЙ REPEAT = 6
# БУКВЫ НЕ ДОЛЖНЫ ПОВТОРЯТЬСЯ ВО ВХОДНОЙ СТРОКЕ СИМВОЛОВ ДЛЯ ПЕРЕБОРА
from itertools import product

def has_unique_letter(word):
    for el in word:
        if word.count(el) > 1:
            return False
    return True

def good(word):
    if word[0] == "Й" or word.count("ВФ") > 0 or word.count("ФВ") > 0 or not(has_unique_letter(word)):
        return False
    return True

x = list(product("ВАЙФУ", repeat=4))
cnt = 0
for el in x:
    s = "".join(el)
    if good(s):
        cnt += 1
print(cnt)
