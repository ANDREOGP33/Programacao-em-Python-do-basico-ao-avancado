print("Digite 3 numeros inteiros diferentes: ")

x = input()
y = input()
z = input()

if x < y < z:
    print(f"Ordem crescente {x},{y},{z}")
elif x < z < y:
    print(f"Ordem crescente {x},{z},{y}")
elif z < x < y:
    print(f"Ordem crescente {z},{x},{y}")
elif z < y < x:
    print(f"Ordem crescente {z},{y},{x}")
elif y < z < x:
    print(f"Ordem crescente {y},{z},{x}")
elif y < x < z:
    print(f"Ordem crescente {y},{x},{z}")
