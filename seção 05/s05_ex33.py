cod = int(input("Digite o codigo do produto: "))
qtd = int(input("Digite a quantidade do produto: "))

if cod == 100:
    valor = 1.2 * qtd
    print(f"produto escolhido: Cachorro quente, valor total: {valor}")
elif cod == 101:
    valor = 1.3 * qtd
    print(f"produto escolhido: Bauru simples, valor total: {valor}")
elif cod == 102:
    valor = 1.5 * qtd
    print(f"produto escolhido: Bauru com ovo, valor total: {valor}")
elif cod == 103:
    valor = 1.2 * qtd
    print(f"produto escolhido: Hamburguer, valor total: {valor}")
elif cod == 104:
    valor = 1.7 * qtd
    print(f"produto escolhido: Cheseburguer, valor total: {valor}")
elif cod == 105:
    valor = 2.2 * qtd
    print(f"produto escolhido: Suco, valor total: {valor}")
elif cod == 105:
    valor = 1 * qtd
    print(f"produto escolhido: Refrigerante, valor total: {valor}")
