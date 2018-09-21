import random
convert = {0000:1,0001:2,0003:3}
rows = [[convert[random.randint(1,3)] for i in range(3)] for j in range(3)]
numgood = 25 -sum(e.count(0) for e in rows)
print numgood
