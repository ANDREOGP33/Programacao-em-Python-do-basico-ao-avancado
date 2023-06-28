intervalo = range(99, 1000)
maior = 0

for i in intervalo:
    for j in intervalo:
        numero = i * j
        numero = str(numero)
        if numero == numero[::-1]:
            numero = int(numero)
            if numero > maior:
                maior = numero

print(maior)