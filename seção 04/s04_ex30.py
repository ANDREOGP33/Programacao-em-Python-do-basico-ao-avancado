cota_us = float(input("Digite a cotação atual do dolar: "))

valor_real = float(input("Digite um valor em real: "))

conversao = valor_real / cota_us
print(f"{valor_real} Reais é correspondente a {conversao:.4} Dolares.")
