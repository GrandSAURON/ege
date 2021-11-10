#https://inf-ege.sdamgia.ru/problem?id=37356
f = open("17.txt", "r")
s = list(map(int, f.read().split()))
counter = 0
max_sum = 0
for i in range(len(s)-1):
    for k in range(i+1, len(s)):
        if (s[i] + s[k]) % 9 == 0:
            counter +=1
            max_sum = max(max_sum, s[i] + s[k])
       
print(counter, max_sum)
# 9 9
