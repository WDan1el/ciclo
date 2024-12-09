import math

e_approx = 0 
n = 10  #!
diferencia = 1  #
umbral = 0.0001  

while diferencia >= umbral:
   
    factorial = math.factorial(n)
   
    e_approx += 1 / factorial
    
   
    if n > 10:
        diferencia = abs(1 / factorial - 1 / math.factorial(n - 1))
    else:
        diferencia = 1  
    n += 1

print(f"El valor aproximado de e es: {e_approx + 2.71828}")  