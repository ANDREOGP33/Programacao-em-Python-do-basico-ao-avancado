print("Digite as dimensões do terreno: ")
largura = float(input("Largura: "))
comprimento = float(input("Comprimento: "))

valor_tela = float(input("Digite o valor do metro da tela: "))

perimetro = (largura * 2) + (comprimento * 2)

valor_total = valor_tela * perimetro

print(f"Para cercar completamente o terreno ira cstar R${valor_total:.2f}")