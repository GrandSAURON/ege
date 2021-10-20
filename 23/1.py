# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=10&mode=print
def path(start, finish):
    for i in range(start + 1, finish + 1):
        k = 0
        if i == 10 or i == 15:
            continue
        if i-1 >= start:
            k += dp[i-1]
        if i-2 >= start:
            k += dp[i-2]
        if i-3 >= start:
            k += dp[i-3]
        dp[i] = k
        
dp = [0 for i in range(1000)]
dp[5] = 1
        
path(5, 11)
path(11,18)
print(dp[18])
