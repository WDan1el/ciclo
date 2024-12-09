from fractions import Fraction

n = int(input("Ingresa el número de términos para calcular las potencias fraccionarias de 2: "))

print(f"{'Potencia':<10} {'Valor Decimal':<20} {'Valor Fraccionario':<20}")

for i in range(1, n + 1):
    potencia = -i  
    valor_decimal = 2 ** potencia  
    valor_fraccionario = Fraction(1, 2 ** i)  #
