# https://inf-ege.sdamgia.ru/problem?id=13633
def path(start, finish):
    for i in range(start + 1, finish + 1):
        k = 0
        if i-1 >= start:
            k += dp[i-1]
        if i%2 == 0 and i//2 >= start:
            k += dp[i//2]
        if i%3 == 0 and i//3 >= start:
            k += dp[i//3]
        dp[i] = k
        
dp = [0 for i in range(1000)]
dp[2] = 1
        
path(2, 15)
path(15,30)
print(dp[30])
