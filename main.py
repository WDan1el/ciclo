total_minutos = 0

print("Ingrese los tiempos de los tramos del viaje en minutos (ingrese 0 para finalizar):")

while True:
    tiempo = int(input("Duración del tramo (en minutos): "))
    if tiempo == 0: 
        break
    if tiempo < 0:  
        print("Por favor, ingrese un valor positivo.")
        continue
    total_minutos += tiempo


horas = total_minutos // 60
minutos = total_minutos % 60

print(f"El tiempo total de viaje es: {horas} horas y {minutos} minutos.")
