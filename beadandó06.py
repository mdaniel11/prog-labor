import sys
import matplotlib.pyplot as plt
import numpy as np


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
            print(atl)


            fin.close()

except FileNotFoundError:
    print("A megadott fájl nem található.")
