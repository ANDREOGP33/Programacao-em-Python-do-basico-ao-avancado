limite = int(input("Digite um limite máximo para os números: "))

for a in range(1, limite):
    for b in range(a, limite):
        c = (a ** 2 + b ** 2) ** 0.5
        if c.is_integer() and c <= limite:

            print(f"Terno pitagórico encontrado: {a}, {b}, {int(c)}")