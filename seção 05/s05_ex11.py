x = int(input("Digite um numero inteiro maior que zero: "))

ultimo = x % 10
penultimo = (x // 10)  % 10
primeiro = (x // 10) // 10

print(f"{primeiro + penultimo + ultimo}")

