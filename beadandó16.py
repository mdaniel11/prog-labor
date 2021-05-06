def feladat(K,N):
    if len(K)<len(N):
        K,N=N,K
    lenK=len(K)
    lenN=len(N)
    lsK= [0]*karakterek
    lsN=[0]*karakterek
    for i in range(lenN):
        lsN[ord(N[i])]+=1
    s=0
    sindex=-1
    min=float("inf")
    db = 0
    for i in range(lenK):
        lsK[ord(K[i])] += 1
        if lsK[ord(K[i])] <= lsN[ord(K[i])]:
            db += 1
        if db==lenN:
            while lsK[ord(K[s])] > lsN[ord(K[s])] or lsN[ord(K[s])]==0:
                if lsK[ord(K[s])] > lsN[ord(K[s])]:
                    lsK[ord(K[s])] -=1
                s+=1
            minkarakter=i-s+1
            if min>minkarakter:
                min=minkarakter
                sindex=s
    if sindex == -1:
        print("Nincs a K sztringnek,olyan legrövidebb rész sztringje, amely tartalmazza az N sztring minden karakterét")
        return ""
    return K[sindex: sindex+min ]
try:
    karakterek = 256
    K="aaffhkksemckelloe"
    N="fhea"
    print(feladat(K,N))


except TypeError:
    print("A paraméterek nem stringek.")