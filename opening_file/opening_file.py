f = open("test.txt", 'r')
lista = []
for line in f:
    lista.append(line.strip())

print(lista)
