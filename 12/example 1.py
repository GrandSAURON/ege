#https://inf-ege.sdamgia.ru/problem?id=9365

s = "8" * 68
while(s.count("222") > 0 or s.count("888") > 0):
    if s.count("222") > 0:
        s = s.replace("111", "8", 1)
    else:
        s = s.replace("888", "2", 1)
        
print(s)
