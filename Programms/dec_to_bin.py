def dec_to_bin(n):
    a = ""
    while n > 0:
        k = n % 2
        a = str(k) + a
        n = n // 2
    return a

print(dec_to_bin(10))
