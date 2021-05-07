import numpy as np
def szoras(ls):
    lsparos=[]
    lsparatlan=[]
    sum=0
    lista=[]
    for i in range(len(ls)):
        for j in ls[i]:
            for ch in j:
                if ch !="-":
                    lista.append(int(ch))
            sum += lista[0]
            lista.clear()
            if int(j)%2==0:
                lsparos.append(int(j))
            else:
                lsparatlan.append(int(j))
        if len(lsparos)<2:
            print(f"A(z) {i+1}.sor páros számainak nem lehet kiszámolni a szórását.")
            lsparos.clear()
        if len(lsparatlan)<2:
            print(f"A(z) {i+1}.sor páratlan számainak nem lehet kiszámolni a szórását.")
            lsparatlan.clear()
        if len(lsparos)>=2 or len(lsparatlan)>=2:
            lsszorasparos=np.nanstd(lsparos)
            lsszorasparatlan=np.nanstd(lsparatlan)
            lsparatlan.clear()
            lsparos.clear()
            print(f"{i+1}.sor\n"
                  f"Páros számok szórása: {lsszorasparos:2.2f} Páratlan számok szórása: {lsszorasparatlan:.2f}\n"
                  f"Számjegyek összege (legnagyobb helyiértékek): {sum}")
            sum=0
            lsszorasparos=0
            lsszorasparatlan=0
        # [124 25 35 2 -13 9 85 102]
        # [22 4 78 9 -32 -11 5 325 28 8 7 14]
    return ""
try:
    n=int(input("Adja meg hány sort akar beírni: "))
    ls=[]
    for i in range(n):
        line=input("Adjon meg számokat szóközzel elválasztva(lehetőleg 2-nél többet): ")
        ls.append(line.split(" "))
    print(szoras(ls))

except ValueError:
    print("Számokat adjon meg.")