n = int(input("Digite um numero positivo:"))
divisores = []

for i in range (1, n):
    if n % i == 0:
        divisores.append(i)

soma = 0

for i in divisores:
    soma += i
    
print(soma)