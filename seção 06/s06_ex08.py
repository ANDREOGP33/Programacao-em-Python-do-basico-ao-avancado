maior = 0
for i in range(0, 10):
    print(f"digite o {i+1}° numero: ")
    x = int(input())
    if x > maior:
        maior = x

print(f"maior: {maior}")