soma = 0.0
denominador = 1

for numerador in range(1, 100, 2):
    soma += numerador / denominador
    denominador += 1

print(soma)
