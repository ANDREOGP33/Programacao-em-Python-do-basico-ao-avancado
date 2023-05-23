x = int(input("Digite um numero inteiro: "))
y = int(input("Digite outro numero inteiro: "))

if x > y:
    print(f"Maior = {x}")
    print(f"Diferença = {x - y}")
else:
    print(f"Maior = {y}")
    print(f"Diferença = {y - x}")