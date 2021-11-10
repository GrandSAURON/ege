# https://inf-ege.sdamgia.ru/problem?id=37336
f = open("17.txt", "r")
s = list(map(int, f.read().split()))
counter = 0
max_sum = 0
for i in range(len(s) - 1):
    if s[i]%3 == 0 or s[i + 1]%3 == 0:
        counter += 1
        max_sum = max(max_sum, s[i] + s[i + 1])
print(counter, max_sum)
        
