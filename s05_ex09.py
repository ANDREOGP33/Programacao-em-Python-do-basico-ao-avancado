salario = float(input("Digite o seu salario: "))
valor_prestacao = float(input("Digite o valor da prestação: "))

if valor_prestacao > 0.2 * salario:
    print("mprestimo não concedido.")
else:
    print("Emprestimo concedido.")
