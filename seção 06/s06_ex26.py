def primeiro_multiplo(n):
    i = n=+1

    while True:
        if i % 11 == 0 or i % 13 == 0 or i % 17 == 0:
            return i
        i += 1
    

n = int(input("Digite um numero: "))
multiplo = primeiro_multiplo(n)
print(multiplo)