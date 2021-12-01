#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=13&mode=print
f = open("17.txt", "r")
lines = f.readlines()
count = 0

def get_sum(n: str):
    ans = 0
    for el in n:
        ans += int(el)
    return ans

cnt = 0
max_val = 0
for num in lines:
    if (get_sum(num.strip('\n')) % 3 == 0):
        cnt += 1
        max_val = max(max_val, int(num))

print(cnt, max_val)
