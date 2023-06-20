fib = [0,1]

num = int(input("Digite um numero positivo: "))

while True:
    if num <= 0:
        print("Numero negativo!!!")
        break
    fib.append(fib[-1] + fib[-2])
    print(fib)
    if fib[-1] > num:
        break