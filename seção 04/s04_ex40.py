DiasTrabalhados = int(input("Digite os dias trabalhados: "))
ValorDia = 30

SalarioBruto = DiasTrabalhados * ValorDia
SalarioLiquido = SalarioBruto - (SalarioBruto * 8/100)

print(f"Valor do salario liquido: {SalarioLiquido}")
