"""
Lista de primos menores a cierto número
"""


# Entradas
limite = int(input("Cuál es el número que quieres probar? "))


# Proceso
numero = 2
primos = []
while numero <= limite:
    divisor = 2
    primo = True
    while divisor < numero:
        if numero % divisor == 0:
            primo = False
            break
        divisor += 1
    if primo:
        primos.append(numero)
    numero += 1


# Salidas
print("Los números primos menores o iguales a", limite, "son", primos)