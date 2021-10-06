#https://inf-ege.sdamgia.ru/problem?id=18497
def bin_to_dec(n):
    return(int(n, base=2))

def dec_to_bin(n):
    a = ""
    while n > 0:
        k = n % 7
        a = str(k) + a
        n = n // 7
    return a

n = 6*343**5+5*49**7-50
print(dec_to_bin(n).count("6"))
       
