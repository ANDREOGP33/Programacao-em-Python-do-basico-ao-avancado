ValorTotal = float(input("Digite o valor da compra: "))

ValorDesconto = ValorTotal - (ValorTotal * 10/100)
ValorParcela = ValorTotal / 3
ComissaoAvista = ValorDesconto * 5/100
ComissaoParcela = ValorTotal * 5/100

print(f"Valor da compra a vista: {ValorDesconto:.5}\n"
      f"Valor da compra parcelada: 3 de {ValorParcela:.5}\n"
      f"Valor da comissão a vista : {ComissaoAvista:.5}\n"
      f"Valor da comissao parcelada: {ComissaoParcela:.5}")
