Segundos = int(input("Digite um valor em segundos: "))

horas = Segundos // 3600
minutos = (Segundos % 3600) // 60
segundos = Segundos % 60 

print(f"{horas}:{minutos}:{segundos}")