numero = int(input("Ingresa un número entero para encontrar sus divisores: "))

if numero == 0:
    print("Todos los números enteros son divisores de 0.")
else:

    print(f"Los divisores de {numero} son:")
    for i in range(1, abs(numero) + 1):
        if numero % i == 0:
            print(i)
