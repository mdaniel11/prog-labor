import sys
import matplotlib.pyplot as plt
import string
try:

    evesszam = input("Adjon meg egy évszámot és egy számot(pl.: 2013 4): ")
    lsinput= evesszam.split(" ")
    fin = open(sys.argv[1], "r")
    elsosor=fin.readline()
    lselsosor=elsosor.split(",")
    oszam = len(lselsosor)
    # print(oszam)
    # print(lsinput)
except FileNotFoundError:
    print("A megadott fájl nem található.")
