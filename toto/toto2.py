import random
import pyexpat

liczby = []

ileliczb = int(input("Ile liczb? "))
maxliczba = int(input("Maksymalna liczba? "))

# print("Wytypuj %s z %s liczb" % (ileliczb, maxliczba))

i = 0
while i < ileliczb:
    liczba = random.randint(1, maxliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

print("Wylosowane liczby:", liczby)

print("Wytypuj %s z %s liczb: " % (ileliczb, maxliczba))
typy = set()

i = 0
while i < ileliczb:
    typ = int(input("Podaj liczbe %s" % (i + 1)))
    if typ not in typy:
        typy.add(typ)
        i = i + 1

trafione = set(liczby) & typy

if trafione:
    print("\nIlosc trafien: ", len(trafione))
    print("Trafione liczby: ", trafione)
else:
    print("Brak trafien")
