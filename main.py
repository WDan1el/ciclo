import math

# Inicializar variables
e_approx = 0  # Estimación de e
n = 10  # Comenzamos con 10!
diferencia = 1  # Inicializar diferencia alta para entrar al bucle
umbral = 0.0001  # Diferencia mínima entre sumandos consecutivos

while diferencia >= umbral:
   
    factorial = math.factorial(n)
   
    e_approx += 1 / factorial
    
   
    if n > 10:
        diferencia = abs(1 / factorial - 1 / math.factorial(n - 1))
    else:
        diferencia = 1  
    n += 1

print(f"El valor aproximado de e es: {e_approx + 2.71828}")  