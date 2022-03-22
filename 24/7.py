f = open('24.txt')
temp = f.read()
k, m = 1, 1
for i in range(len(temp)-1):
    if temp[i]=='P' and temp[i+1]=='P':
        k=1
    else:
        k += 1
        m=max(m, k)
print(m)
