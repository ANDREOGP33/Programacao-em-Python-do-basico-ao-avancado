valor1 = float(input("Digite o valor investido pelo primeiro jogador: "))
valor2 = float(input("Digite o valor investido pelo segundo jogador: "))
valor3 = float(input("Digite o valor investido pelo terceiro jogador: "))

premio = float(input("Digite o valor do preimio:"))

valor_total = valor1 + valor2 + valor3

p1 = ((valor1 / 100) * valor_total)
p2 = ((valor2 / 100) * valor_total)
p3 = ((valor3 / 100) * valor_total)

vp1 = p1 * premio
vp2 = p2 * premio
vp3 = p3 * premio

print(f"O primeiro jogador vai receber {vp1:.2f} Reais\n segundo jogador: {vp2:.2f} Reais\n teerceiro jogador: {vp3:.2f} Reais.")