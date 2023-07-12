notas = []
total = 0

for i in range(0, 10):
    nota = float(input("Digite o valor da nota: "))
    notas.append(nota)

for i in notas:
    total += i

media = total / 10

print(f"media: {media}")