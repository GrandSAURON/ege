#https://inf-ege.sdamgia.ru/problem?id=27686

a = input()
k = 0
maxk = 0
for i in range(len(a)):
    if a[i] == "X":
        k += 1
    else:
        k = 0
        
    maxk = max(maxk, k)
    
print(maxk)