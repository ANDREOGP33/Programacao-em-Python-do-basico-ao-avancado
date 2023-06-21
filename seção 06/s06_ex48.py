fib = [0,1]

while True:
    fib.append(fib[-1] + fib[-2])
    print(fib)
    if fib[-1] > 4000000:
        break