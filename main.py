n = int(input("Ingresa el número de términos de la serie para estimar π: "))


pi_estimado = 0


for i in range(n):
    
    signo = (-1) ** i
    
    pi_estimado += signo / (2 * i + 1)


pi_estimado *= 4


print(f"La estimación de π usando {n} términos es: {pi_estimado}")
