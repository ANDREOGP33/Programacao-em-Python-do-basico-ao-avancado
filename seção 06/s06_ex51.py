salario = 2000
ano_inicial = 1995
aumento = 0.015

while ano_inicial <= 2023:
    if ano_inicial < 1997:
        salario += salario * aumento
    else:
        salario += salario * (aumento * 2)
    
    ano_inicial += 1

print(salario)