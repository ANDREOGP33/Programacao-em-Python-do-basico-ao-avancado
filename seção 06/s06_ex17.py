n = int(input("Digite um numero inteiro positivo: "))

soma = 0

if n < 0:
    print("Digite um numero maior que 0!!!")
else:
    for i in range (0, n+1):
        soma = soma + i

print(soma)
