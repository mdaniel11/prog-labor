#1.feladat
# while True:
#     try:
#         x = int(input("Adjon meg egy számot"))
#         print(x)
#         break
#     except ValueError:
#         print("Nem megfelelő szám")
#2.feladat
# try:
#     fout = open("input.txt","r")
#     for str in fout:
#         print(str)
#     fout.close()
# except FileNotFoundError:
#     print("Nem található a fájl")
#3.faladat
# def Lannister(fout):
#     db = 0
#     for i in fout:
#         tmp = i.split(" ")
#         for j in tmp:
#             if "Lannister" in j:
#                 db+=1
#     return db
# try:
#     fout = open("input.txt","r")
#     print(Lannister(fout))
# except FileNotFoundError:
#     print("Nem található a fájl")
#4.feladat
# def Letterchanger(fin):
#     str = ""
#     for i in fin:
#         if "A" <= i <= "Z":
#             str += i.lower()
#         elif "a" <= i <= "z":
#             str += i.upper()
#         else:
#             str += i
#     return str
#
# try:
#     fin = open("input.txt","r")
#     fout = open("output.txt", "w")
#     for i in fin:
#         print(Letterchanger(i),file=fout)
#     fin.close()
#     fout.close()
# except FileNotFoundError:
#     print("Nem található a fájl!")
# def Leghosszabb(fin,fout):
#     max = -1
#     ls = []
#     for i in fin:
#         tmp = i.split(" ")
#         for j in tmp:
#             if len(j)>max:
#                 ls = []
#                 max = len(j)
#                 ls.append(j)
#             if len(j)==max:
#                 ls.append(j)
#     for tmp in ls:
#         print(tmp,file=fout)
#
#
# try:
#     fin =open("input.txt","r")
#     fout = open("Longesword.txr","w")
#     Leghosszabb(fin,fout)
#     fin.close()
#     fout.close()
# except FileNotFoundError:
#     print("Nem található a fájl!")
