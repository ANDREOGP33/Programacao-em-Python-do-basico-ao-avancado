inicio = int(input("Digite um numero inicial: "))
fim = int(input("Digite um numero final: "))

intervalo = range(inicio, fim+1)

soma = 0
multiplicacao = 1

for i in intervalo:
    if i % 2 == 0:
        soma += i
    else: 
        multiplicacao *= i

print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")