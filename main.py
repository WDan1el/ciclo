tamaño = int(input("Ingresa el tamaño del triángulo (altura): "))


if tamaño <= 0:
    print("El tamaño debe ser un número entero positivo.")
else:
    print("Aquí está tu triángulo:")
 
    for i in range(1, tamaño + 1):
        print("*" * i)
