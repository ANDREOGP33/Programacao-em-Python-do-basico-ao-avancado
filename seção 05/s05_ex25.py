a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b ** 2) - 4 * a * c

x1 = (-b + delta ** (1 / 2)) / (2 / a)
x2 = (-b - delta ** (1 / 2)) / (2 / a)

if delta < 0:
    print("Ñ existe raiz.")
elif delta == 0:
    print("Raiz unica.")
elif delta >= 0:
    print(f"Primeira raiz: {x1}\n"
          f"Segunda raiz {x2}")
    