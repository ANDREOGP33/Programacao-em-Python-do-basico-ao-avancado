lista_idade = []
total = 0

while True:
    idade = int(input("Digite uma idade: "))
    if idade <= 0:
        break
    lista_idade.append(idade)

for i in lista_idade:
        total += i

total_idades = lista_idade.__len__()

media = total / total_idades

print(f"Média das idades digitadas: {media}")