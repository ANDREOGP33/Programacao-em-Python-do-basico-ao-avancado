while True:
    r1 = float(input("Digite o valor de R1: "))
    r2 = float(input("Digite o valor de R2: "))
    r = (r1 *r2)/(r1+r2)
    print(f"Valor de R: {r:.4}")
    if r1 == 0 or r2 == 0:
        break

    
