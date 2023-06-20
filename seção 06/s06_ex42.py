while True:
    n1 = float(input("Digite um numero n1: "))
    if n1 == 0:
        break

    n2 = float(input("Digite um numero n2: "))
    if n2 == 0:
        break

    print(f"n1 ao Quadrado {n1**2}")
    print(f"n1 ao Cubo {n1**3}")
    print(f"n1 raiz quadrada:  {n1**0.5:.2}")    

    print(f"n2 ao Quadrado {n2**2}")
    print(f"n2 ao Cubo {n2**3}")
    print(f"n2 raiz quadrada: {n2**0.5:.2}")