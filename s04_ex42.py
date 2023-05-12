SalarioBase = float(input("Digite o salario base: "))

SalarioLiquido = (SalarioBase +(SalarioBase * 5/100) - (SalarioBase * 7/100))

print(f"O funcionario recebe: {SalarioLiquido}")
