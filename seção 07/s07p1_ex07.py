vetor = []

for i in range (0,10):
    numero = int(input())
    vetor.append(numero)

print(vetor)
maior = max(vetor)
print(maior)
indice = vetor.index(maior)
print(indice)