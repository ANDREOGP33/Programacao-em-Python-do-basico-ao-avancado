qtd = 0
numero = 0
total = 0
print("Digite um numero inteiro: ")
numero = int(input())
while qtd < 10:
    print("Digite outro numero inteiro: ")
    numero = int(input())
    numero = int(input())
    total = total + numero
    qtd += 1


print(f"Media dos numeros digitados: {total / qtd+1}")
