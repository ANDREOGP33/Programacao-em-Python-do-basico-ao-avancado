print("Digite 3 numeros inteiros: ")

x = int(input())
y = int(input())
z = int(input())

print(f"Geometrica: {(x * y * z) ** (1 / 3):.3}")
print(f"Ponderada: {(x + 2 * y + 3 * z) / 6:.3}")
print(f"Aritimética : {(x + y + z) / 3}")