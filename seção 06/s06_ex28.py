n = int(input("Digite um numero inteiro positivo: "))

e = 0

for i in range(1, n+1):
    e += 1 + (1/(1*i))

print(e)
