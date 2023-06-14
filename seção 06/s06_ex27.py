n = int(input("Digite um numero: "))
h = 0

for i in range(1, n+1):
    h += 1 + (1/i)

print(h)