import  numpy as np
#2.feladat
b = np.array(np.ceil(100*np.random.random(30)),dtype="uint8")
print(b)
minB = b.min()
maxB = b.max()
print(minB,maxB)
ind = np.where((b == minB) | (b == maxB))
print(ind)