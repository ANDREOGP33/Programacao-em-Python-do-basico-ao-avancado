vetor = []

for i in range(0, 8):
    numero = int(input("Digite um valor: "))
    vetor.append(numero)


x = int(input("Digite o valor de X entre 0 e 7: "))

y = int(input("Digite o valor de Y entre 0 e 7: "))

soma = vetor[x] + vetor[y]

print(soma)

