lista_fornecida = input("")
print(lista_fornecida)
a = []
lista_fornecida = lista_fornecida.split()
print(lista_fornecida)
for t in lista_fornecida:
    t = int(t)
    if t%2 == 0:
        a.append(t/2)
    else:
        a.append(t+10)
print(a)
