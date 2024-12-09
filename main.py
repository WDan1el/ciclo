n = int(input("Ingresa un número para generar las potencias de 2 hasta la n-ésima: "))

print(f"Potencias de 2 desde la 0-ésima hasta la {n}-ésima:")
for i in range(n + 1):
    print(f"2^{i} = {2 ** i}")
