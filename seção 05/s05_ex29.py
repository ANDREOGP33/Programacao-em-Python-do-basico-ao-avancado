print("Quanto é a soma de 45 + 17: ")
# 62
q1 = int(input())

print("Quanto é  52 + 4:")
# 56
q2 = int(input())

print("Quanto é  9 + 4:")
# 13
q3 = int(input())

print("Quanto é  10 + 4:")
# 14
q4 = int(input())

print("Quanto é  24 + 38")
# 62
q5 = int(input())

nota = 0

if q1 == 62:
    nota = nota + 1

if q2 == 56:
    nota = nota + 1

if q3 == 13:
    nota = nota + 1

if q4 == 14:
    nota = nota + 1

if q5 == 62:
    nota = nota + 1

if nota == 5:
    print("Parabens, nota maxima.")
else:
    print(f"Nota: {nota}")

if q1 != 62:
    print("correção: 1) 62")

if q2 != 56:
    print("correção: 2) 56")

if q3 != 13:
    print("correção: 3) 13")

if q4 != 14:
    print("correção: 4) 14")

if q5 != 62:
    print("correção: 5) 62")
