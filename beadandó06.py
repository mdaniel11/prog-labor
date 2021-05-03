import sys
import matplotlib.pyplot as plt
import string
try:
    fin = open(sys.argv[1],"r")
    evszam = input("Adjon meg egy évszámot: ")
    n = input("Adjon meg egy pozitív egész számot: ")
    for i in fin:
        str = i.split(",")
    avg= sum(int(str[1]))/56
    print(avg)
except FileNotFoundError:
    print("A megadott fájl nem található.")
test