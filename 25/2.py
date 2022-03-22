a = 312614
b = 312651
for i in range (a, b):
    ds = []
    for d in range (1, i):
        if (i % d == 0):
            ds.append(d)
            if len(ds) > 6:
                break
    if (len(ds) == 6):
        print (ds[0], ds[1], ds[2], ds[3], ds[4], ds[5])
