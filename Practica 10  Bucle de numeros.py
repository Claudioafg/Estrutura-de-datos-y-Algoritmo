suma = 0

while True:
    numero = float(input("Ingresa un número para la suma (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("La suma total es:", suma)