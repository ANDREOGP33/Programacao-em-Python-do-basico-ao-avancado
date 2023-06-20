maior = 0

while True:
    numero = int(input("Digite um numero inteiro: "))
    if numero <= 0:
        break
    if numero > maior:
        maior = numero

print(f"Maior numero digitato: {maior}")
