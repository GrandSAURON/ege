#https://inf-ege.sdamgia.ru/problem?id=27418
def win(a,b):
    if a + 1 + b >= 77 or a *2 + b >= 77 or b + 1 + a >= 77 or b * 2 + a >= 77:
        return True
    return False


# p1 -> 60 1
# v1 -> 

def p1(a, b):
    if win(a, b):
        return False
    v0 = v1(a * 2, b)
    v2 = v1(a, b * 2)
    v3 = v1(a+1, b)
    v4 = v1(a, b+1)
    return v0[0] and v2[0] and v3[0] and v4[0] and (v0[1] or v2[1] or v3[1] or v4[1])

# 2 value
# [True, False]
# 1 - True - Vanya win 
# 2 - ПОбедил ли он свои 2 ходом?
def v1(a, b):
    if win(a, b):
        return [True, False]
    k = p2(a*2, b) or p2(a, b * 2) or p2(a + 1, b) or p2(a, b + 1)
    if k:
        return [True, True]
    return [False, False]

def p2(a, b):
    if win(a, b):
        return False
    return v2(a*2, b) and v2(a, b * 2) and v2(a + 1, b) and v2(a, b + 1)


def v2(a, b):
    if win(a, b):
        return True
    return False
    
    
for s in range(1, 69+1):
    if (p1(7, s)):
        print(s)
        
print("!#!@")
