total = 0

for i in range (0, 10):
    print("Digite um numero inteiro: ")
    numero = int(input())
    if numero > 0:
        total = total + numero

    media = total / 10

print(f"Media: {media}")