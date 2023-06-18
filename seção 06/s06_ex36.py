inicio = int(input("Digite um valor para o inicio: "))
fim = int(input("Digite um valor para o fim: "))

soma = 0
for i in range(inicio, fim):
    if i % 2 != 0:
        soma += i
print(f"Soma dos impares neste intervalo: {soma}")
