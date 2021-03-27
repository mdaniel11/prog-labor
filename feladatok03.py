import sys
import  random
#1.feladat
# ls1 = []
# ls2 = []
# counter = 0
# for i in sys.argv[1:]:
#     if i =="L:":
#         counter += 1
#     elif counter == 1:
#         ls1.append(i)
#     elif counter == 2:
#         ls2.append(i)
# newls = []
# for item in ls1:
#     if item not in ls2:
#         newls.append(item)
# print(newls)
#2.feladat
# def elsonosszeg(x):
#     szumma=0
#     s = ""
#     for i in range(1,x+1):
#         szumma+=i
#         s+= str(i) + "+"
#     s = s[:-1] + "="+str(szumma)
#     return s
#
# if len(sys.argv)<3:
#     print("Nincs elegendő input argumentum")
# else:
#     try:
#         x = int(sys.argv[1])
#         outfile = sys.argv[2]
#         fout = open(outfile,"w")
#         print(elsonosszeg(x),file=fout)
#     except ValueError:
#         print("Nem számot adott meg az első argumentumba")
#3.feladat
# def atalakito(n,fout):
#     tmp = n
#     ev = n//(3600*24*365)
#     n = n%(3600*24*365)
#     nap = n//(3600*24)
#     n = n%(3600*24)
#     ora = n//(3600)
#     n = n%(3600)
#     perc = n//60
#     n = n%60
#     print(f"{tmp} masodperc az {ev} ev, {nap} nap, {ora} ora, {perc} perc es {n} masodperc",file=fout)
# if len(sys.argv) < 3:
#     print("Nem megfelelő mennnyiségű argumentumot adott meg.")
# else:
#     try:
#         n = int(sys.argv[1])
#         fout = open(sys.argv[2],"w")
#         atalakito(n,fout)
#         fout.close()
#     except ValueError:
#         print("Nem számot adott meg az első argumentumba!")
#4.feladat
# def sumOfChars(string):
#     sum = 0
#     tmp = ""
#     flag = False
#     for ch in string:
#         if "0" <= ch <="9":
#             tmp +=ch
#             flag=True
#         else:
#             if flag:
#                 sum+= int(tmp)
#                 tmp = ""
#                 flag = False
#     if "0" <= ch <= "9":
#         sum += int(tmp)
# print(sumOfChars(sys.argv[1]))
#5.feladat
# def generaterandomnumber(n,outfile):
#     for i in range(n):
#         print(random.randint(0,101),file=outfile)
# def sumOfNumber(outfile):
#     sum = 0
#     for n in outfile:
#         sum += int(n)
#     return  sum
#
# n = int(sys.argv[1])
# outfile = open(sys.argv[2],"w+")
# generaterandomnumber(n,outfile)
# outfile.seek(0)
# print("Szummája a számoknak: ", sumOfNumber(outfile))
# outfile.close()