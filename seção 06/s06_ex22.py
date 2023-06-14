print("Digite sua notas: ")

total = 0
qtd_notas = 0

while True:
    nota = int(input())
    if 10 <=nota <= 20:
        total = total + nota
        qtd_notas = qtd_notas + 1
    else:
        break

media = total / qtd_notas

print(f"Media = {media}")
