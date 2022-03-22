with open('24.doc') as f:
    print(sum(1 for line in f if line.count('A') < line.count('E')))
