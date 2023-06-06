multiplos = []
numeros = 1

while len(multiplos) < 5:
    if numeros % 3 == 0:
        multiplos.append(numeros)
    numeros = numeros +1

print(multiplos)