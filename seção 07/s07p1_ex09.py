vetor = []

for i in range(0, 6):
    valor = int(input("Digite um valor par: "))
    if valor % 2 != 0:
        while True:
            valor = int(input("Digite um valor par: "))
            if valor % 2 == 0:
                vetor.append(valor)
            break
    else:
        vetor.append(valor)

print(vetor)

