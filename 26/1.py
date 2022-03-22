f = open('26.txt')
n = int(f.readline())
temp = []
o = []
for i in range(n):
    x = int(f.readline())
    if x % 2 == 0:
        temp.append(x)
    else:
        o.append(x)
k = 0
m = 0
set_e = set(temp)
set_temp = set(o)
for i in range(len(temp)):
    for j in range(len(o)):
        sm = temp[i]+o[j]
        if sm in set_e or sm in set_temp:
            k += 1
            if sm > m:
                m = sm
print(k, m)
