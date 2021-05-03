import  numpy as np
#3.feladat
def isrowcolsumeq(v):
    colsum = v.sum(axis=0)
    rowsum = v.sum(axis = 1)
    return
v = np.random.randint(0,6,(4,5))
print(v)