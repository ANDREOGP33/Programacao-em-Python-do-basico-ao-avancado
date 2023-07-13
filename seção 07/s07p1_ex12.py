vetor = []

for i in range(0, 5):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)

total = 0

for i in vetor:
    total += i
   
media = total / 5

print(vetor)
print(f"Média: {media}")
print(f"Maior: {max(vetor)}")
print(f"Menor: {min(vetor)}")