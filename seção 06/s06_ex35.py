inicio = int(input("Digite um valor inicial: "))
fim = int(input("Digite um valor final: "))
intervalo = range(inicio, fim)

soma = 0
if fim < inicio:
    print("Intervalos de valores invalido!")
else:
    for i in intervalo:
        if i % 2 != 0:
            soma += i
print(soma)
