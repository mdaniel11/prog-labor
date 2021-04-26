import sys
import matplotlib.pyplot as plt
import string
try:
    fin = open(sys.argv[1],"r")
    evszam = input("Adjon meg egy évszámot: ")
    n = input("Adjon meg egy pozitív egész számot: ")
    for i in fin:
        str = i.split(",")
        print(str[1])
except FileNotFoundError:
    print("A megadott fájl nem található.")