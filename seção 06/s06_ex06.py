print("Digite 10 numeros inteiros: ")
soma = 0
for i in range(1,11):
    numero= int(input(f"{i}° :"))
    soma = soma + numero 
print(f"Soma: {soma}")