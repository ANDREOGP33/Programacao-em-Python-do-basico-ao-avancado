valor = float(input("Digite o valor da mercadoria: "))
estado = str(input("Digite seu estado(MG, SP, RJ e MS): "))

if estado == "MG" or estado == "mg":
    valor = (valor * 0.07) + valor
    print(f"Valor de venda: R${valor}")
elif estado == "SP" or estado == "sp":
    valor = (valor * 0.12) + valor
    print(f"Valor de venda: R${valor}")
elif estado == "RJ" or estado == "rj":
    valor = (valor * 0.15) + valor
    print(f"Valor de venda: R${valor}")
elif estado == "MS" or estado == "ms":
    valor = (valor * 0.08) + valor
    print(f"Valor de venda: R${valor}")
else:
    print("Estado invalido.")