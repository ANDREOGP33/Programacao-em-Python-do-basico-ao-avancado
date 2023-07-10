vetor = []

numero = 0
maior = 0
menor = 0

for i in range(0, 10):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

maior = vetor[0]
menor = vetor[0]

for i in vetor:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print("Maior número:", maior)
print("Menor número:", menor)