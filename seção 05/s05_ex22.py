idade = int(input("Digite sua idade: "))
anos_trabalhados = int(input("Digite seu tempo trabalhado em anos: "))

if idade >= 65 or anos_trabalhados >= 30 or (idade >= 60 and anos_trabalhados >= 25):
    print("Apto a aposentadoria.")
else:
    print("Não está apto a aposentar.")