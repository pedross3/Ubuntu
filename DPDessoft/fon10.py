arquivo = open("arquivo.txt", "w")
d = dict()
while True:
    a = input("")
    b = input("")
    if a == "":
        break
    else:
        d[a] = b
        arquivo.write(a)
arquivo.close()

