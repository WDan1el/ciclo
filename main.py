altura = int(input("Ingresa la altura del rectángulo: "))
ancho = int(input("Ingresa el ancho del rectángulo: "))


if altura <= 0 or ancho <= 0:
    print("La altura y el ancho deben ser números enteros positivos.")
else:
    print("Aquí está tu rectángulo:")

    for _ in range(altura):
        print("*" * ancho)
##