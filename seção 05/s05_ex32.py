preco_antigo = float(input("Digite o valor antigo do produto : "))

if preco_antigo <= 50:
    preco_novo = preco_antigo + (preco_antigo * 0.05)
elif preco_antigo > 50 and preco_antigo <= 100:
    preco_novo = preco_antigo + (preco_antigo * 0.10)
elif preco_antigo > 101:
    preco_novo = preco_antigo + (preco_antigo * 0.15)

if preco_novo < 80:
        print("Barato!")
elif preco_novo >= 80 and preco_novo < 120:
        print("Normal!")
elif preco_novo > 120 and preco_novo <= 200:
        print("Caro!")
elif preco_novo > 201:
        print("Muito caro!")
