#https://inf-ege.sdamgia.ru/problem?id=27689

a = input()
k = 0
str1 = "XYZ"
maxk = 0
for i in range(len(a)):
    if str1[k % 3] == a[i]:
        k += 1
    else:
        k = 0
        if a[i] == "X":
            k = 1
        
    maxk = max(maxk, k)
    
print(maxk)