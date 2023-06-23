def calcular_notas(saque):
    notas = [100, 50, 20, 10, 5, 2, 1]
    quantidade_notas = {}

    for nota in notas:
        if saque >= nota:
            quantidade = saque // nota
            saque = saque % nota
            quantidade_notas[nota] = quantidade

    return quantidade_notas

valor_saque = int(input("Digite o valor do saque: "))
resultado = calcular_notas(valor_saque)

for nota, quantidade in resultado.items():
    print(f"Notas de {nota}: {quantidade}")