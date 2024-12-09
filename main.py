tamaño = int(input("Ingresa el tamaño del hexágono (un número entero positivo): "))

if tamaño <= 0:
    print("El tamaño debe ser un número entero positivo.")
else:
    print("Aquí está tu hexágono:")


    for i in range(1, tamaño + 1):
        espacios = tamaño - i
        print(" " * espacios + "*" * (tamaño + (i - 1) * 2))


    for i in range(tamaño - 1, 0, -1):
        espacios = tamaño - i
        print(" " * espacios + "*" * (tamaño + (i - 1) * 2))
