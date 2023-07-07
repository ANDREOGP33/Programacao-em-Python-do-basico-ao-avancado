vetor = []
par = 0

for i in range(0, 10):
    numero = int(input("Digite um valor: "))
    vetor.append(numero)

for i in vetor:
    if i % 2 == 0:
        par += 1

print(f"O vetor tem {par} numeros pares")