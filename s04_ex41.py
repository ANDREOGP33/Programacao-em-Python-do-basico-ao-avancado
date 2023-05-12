ValorHora = float(input("Digite o valor da hora de trabalho: "))
HorasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

Salario = (ValorHora * HorasTrabalhadas)
Salario = Salario + (Salario * 10/100)

print(f"Salario final: {Salario}")
