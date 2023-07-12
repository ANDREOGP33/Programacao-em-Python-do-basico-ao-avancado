vetor = []

for i in range(0, 10):
    valor = float(input("Digite o valor: "))
    vetor.append(valor)

negativo = 0
soma = 0

for i in vetor:
    if i < 0:
        negativo += 1
    else:
        soma += i  

print(f"Valores negaivos: {negativo}")
print(f"Soma dos positivos: {soma}")
