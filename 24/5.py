#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=15&mode=print
def get_letter(line):
    letter = {}
    for el in line:
        if el not in letter.keys():
            letter[el] = 0
        letter[el] += 1
    return letter

def get_max_value_from_dict(letter: dict):
    max_cnt = 0
    max_letter = 'p'
    for el in letter:
        if letter[el] > max_cnt:
            max_cnt = letter[el]
            max_letter = el
        elif letter[el] == max_cnt:
            max_letter = min(max_letter, el)
    return max_letter

def get_line(lines):
    max_temp = 0
    max_line = ""
    idx = 1
    for line in lines:
        temp = 1
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                temp += 1
                if temp > max_temp:
                    max_temp = temp
                    max_line = line
            else:
                temp = 1
        print(idx, temp)
        idx += 1
    print(max_temp)
    return max_line

f = open("24.txt", "r")
lines = f.readlines()
line = get_line(lines)
print(line)
p = get_letter(line)
print(p)
latter = get_max_value_from_dict(p)
print(latter)
ans = 0
for el in lines:
    ans += el.count(latter)
print(ans)
