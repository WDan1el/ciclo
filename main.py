num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

if num1 > num2:
    num1, num2 = num2, num1  

suma = sum(range(num1 + 1, num2))

print(f"La suma de los números entre {num1} y {num2} es: {suma}")
