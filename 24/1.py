#https://inf-ege.sdamgia.ru/problem?id=27421

a = input()
k = 1
maxk = 0
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        k = 1
    else:
        k += 1
    maxk = max(maxk, k)
    
print(maxk)