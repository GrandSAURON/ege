#https://inf-ege.sdamgia.ru/problem?id=27803
def P1(a):
    if a + 1 >= 68 or a + 4 >= 68 or a * 5 >= 68:
        return False
    return V1(a + 1) or V1(a + 4) or V1(a * 5)
    
def V1(a):
    if a + 1 >= 68 or a + 4 >= 68 or a * 5 >= 68:
        return False
    return P2(a + 1) and P2(a + 4) and P2(a * 5)

def P2(a):
    if a + 1 >= 68 or a + 4 >= 68 or a * 5 >= 68:
        return True
    return False


for s in range(1, 67 + 1):
    if (P1(s)):
        print(s)
