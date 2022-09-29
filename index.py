C = int(input("Ingrese la cantidad de capital: "))

m = 0
suma = C

while suma < 2*C:
    suma += (suma*5)/100
    m +=1

print("En", m, "meses se duplicó el capital")
