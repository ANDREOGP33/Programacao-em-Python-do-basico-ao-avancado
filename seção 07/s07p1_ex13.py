vetor = []

for i in range(0, 5):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)

maior = max(vetor)

print(f"Index do maior valor: {vetor.index(maior)}")