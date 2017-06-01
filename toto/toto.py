import random

liczba = random.randint(1, 6)
# print("Wylosowana liczba:", liczba)

# print("Twoja odpowiedz:", odpowiedz)
for i in range(3):
    print("Proba", i+1)
    odpowiedz = int(input("Podaj liczbe: "))
    if liczba == odpowiedz:
        print("Zgadles!")
        break
    elif i == 2:
        print("Mialem na mysli:", liczba)
    else:
        print("Sorry... :(")
input()
