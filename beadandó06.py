import sys
import matplotlib.pyplot as plt
import numpy as np
import random
# def szingeneralas(n):
#     szinek=[]
#     while n!=0:
#         random_number = random.randint(0, 16777215)
#         hex_number = str(hex(random_number))
#         hex_number = '#' + hex_number[2:]
#         hex_number=str(hex_number)
#         szinek.append(hex_number)
#         n-=1
#     return szinek
def inttealakitas(ls):
    newls=[]
    for i in ls:
        newls.append(int(i))
    return newls

try:

    evesszam = input("Adjon meg egy évszámot és egy számot(pl.: 2013 4): ")
    lsinput= evesszam.split(" ")
    if lsinput[0].isdigit()==False or lsinput[1].isdigit()==False:
        print("Az input csak számokat tartalmazhat.")
    else:
        n = int(lsinput[1])
        ev = int(lsinput[0])
        if ev<2005 or ev>2015:
            print("Csak 2005 és 2015 közötti adatokat tud feldolgozni.")
        elif n>20:
            print("Csak 20 megyénk van.")
        else:
            fin = open(sys.argv[1], "r")
            elsosor = fin.readline()
            lselsosor = elsosor.split(",")
            oszam = len(lselsosor)
            sorszam=0
            for i in fin:
                lssorbol=i.split(",")
                date = lssorbol[0].split("/")
                if int(date[2])==ev:
                    sorszam+=1
            sorszam+=1
            fin.seek(0)
            matrix = np.empty((sorszam,oszam),dtype=object)
            elsoelso = fin.readline()
            elsoelso = elsoelso.strip()
            lselsoelso = elsoelso.split(",")

            a = 0
            for i in range(len(lselsoelso)):
                matrix[a,i]=lselsoelso[i]
            a = 1
            for i in fin:
                i = i.strip()
                ls = i.split(",")
                date=ls[0].split("/")
                if int(date[2])==ev:
                    for j in range(len(ls)):
                        matrix[a,j]=ls[j]
                    a+=1

            atl=[]
            for i in range(oszam):
                sum = 0
                for j in range(sorszam):
                    if i>0 and j >0:
                        sum += int(matrix[j,i])
                atlag = sum/(sorszam-1)
                if i>0:
                    atl.append((matrix[0,i],atlag))
            atl.sort(key=lambda tup: tup[1], reverse=True)
            atl=atl[:n]
            mydict={}
            for i in range(n):
                mydict["ls"+str(i)]=[]
            for i in range(n):
                for osz in range(oszam):
                    for sor in range(sorszam):
                        if osz>0 and sor>0:
                            if matrix[0,osz]==atl[i][0]:
                                mydict["ls"+str(i)].append(matrix[sor,osz])
            x=[]
            for i in range(len(mydict["ls0"])):
                x.append(i)
            szinek = ["green","goldenrod","blue","black","orange","red","purple","pink","brown","cyan","teal","crimson","grey","magenta","yellow","darkblue","lime","lavender","turquoise","ivory"]
            for i in range(n):
                plt.plot(x,inttealakitas(mydict["ls"+str(i)]),color=szinek[i],label=atl[i][0])
                plt.legend()
            plt.xlabel(f"Hetek száma {ev}-ben/ban.")
            plt.ylabel("Fertőzések száma/hét.")
            plt.title(f"Bárányhimlő esetek {ev}-ben/ban abban az {n} megyénkben, ahol az éves átlag a legmagasabb volt.")
            plt.show()
            fin.close()

except FileNotFoundError:
    print("A megadott fájl nem található.")
except IndexError:
    print("Csak 2005 és 2015 között dolgozható fel az adat és csak 20 megyénk van.")