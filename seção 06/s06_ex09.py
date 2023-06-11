print("Quantos numeros voce vai digitar?")
x =int(input())
soma = 0

for i in range (0, x):
    numero = int(input("Digite um numero: "))
    soma = soma + numero
print(f"soma: {soma}")

