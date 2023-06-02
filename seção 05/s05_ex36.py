valor_venda = float(input("Digite o valor de sua venda: "))

if valor_venda >= 100000:
    print(f"Comissão: {700 + ((0.16 * valor_venda) + valor_venda)}")
elif 100000 > valor_venda >= 80000:
    print(f"Comissão: {650 + ((0.14 * valor_venda) + valor_venda)}")
elif 80000 > valor_venda >= 60000:
    print(f"Comissão: {600 + ((0.14* valor_venda) + valor_venda)}")
elif 60000 > valor_venda >= 40000:
    print(f"Comissão: {550 + ((0.14 * valor_venda) + valor_venda)}")
elif 40000 > valor_venda >= 20000:
    print(f"Comissão: {500 + ((0.14 * valor_venda) + valor_venda)}")
elif 20000 > valor_venda:
    print(f"Comissão: {400 + ((0.14* valor_venda) + valor_venda)}")

