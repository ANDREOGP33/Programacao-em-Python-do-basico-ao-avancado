custo_fabrica = float(input("Digite o custo de fabrica:"))

if custo_fabrica <= 12000:
    comisao = 0.05
    imposto = 0
elif 12000 < custo_fabrica <= 25000:
    comisao = 0.10
    imposto = 0.15
elif custo_fabrica > 25000:
    comisao = 0.15
    imposto = 0.20

print(f"Valor de venda: {(custo_fabrica * comisao)+(custo_fabrica * imposto)+(custo_fabrica)}")