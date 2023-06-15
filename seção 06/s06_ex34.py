lista = list(range(1,21))
mmc = 1
divisor = 2

while True:
    dividido = False
    for i in range(len(lista)):
        if lista[i] % divisor == 0:
            lista[i] = lista[i] // divisor
            dividido = True
    if dividido:
        mmc *= divisor
    else:
        divisor += 1
    if max(lista) == 1:
        break

print(mmc)
