# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=6&mode=print
def bin_to_dec(n):
    return(int(n, base=2))

def dec_to_bin(n):
    a = ""
    while n > 0:
        k = n % 2
        a = str(k) + a
        n = n // 2
    return a

def process(n):
    n = dec_to_bin(n)
    if int(n) % 2 == 0:
        n += "01"
    else:
        n+= "10"
    return bin_to_dec(n)
        
for i in range(1, 100):
    print(i, process(i))
