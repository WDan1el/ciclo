# Generar y mostrar la tabla de multiplicar del 1 al 10
print("Tabla de multiplicar (números alineados a la derecha):")
print()

# Encabezado de la tabla
print("   ", end="")
for i in range(1, 11):
    print(f"{i:>4}", end="")
print()

print("-" * 45)

# Generar filas de la tabla
for i in range(1, 11):
    print(f"{i:>2} |", end="")  # Número de la fila con formato alineado
    for j in range(1, 11):
        print(f"{i * j:>4}", end="")  # Producto alineado a la derecha
    print()
