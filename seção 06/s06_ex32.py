n = int(input("Quantas veses irar inserir dados: "))
qtd = 0

while n > qtd:
    d1 = int(input("D1: "))
    d2 = int(input("D2: "))
    if d1 > d2:
        print("D1 > D2")
    elif d1 == d2:
        print("D1 = D2")
    else:
        print("D2 > D1")
    qtd += 1
