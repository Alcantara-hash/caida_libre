import math

def calcular_velocidad_final_gt():
    tiempo = float(input("Ingrese el tiempo transcurrido (en segundos): "))

    velocidad_final = 9.8 * tiempo
    print("La velocidad final es:", velocidad_final, "m/s")

def calcular_posicion_final():
    velocidad_inicial = float(input("Ingrese la velocidad inicial (en m/s): "))
    tiempo = float(input("Ingrese el tiempo transcurrido (en segundos): "))

    print("Seleccione una fórmula:")
    print("1. xf = 1/2 * g * t")
    print("2. xf = Vo * t + 1/2 * g * t^2")

    opcion_formula = int(input("Ingrese el número de la fórmula deseada: "))

    if opcion_formula == 1:
        posicion_final = 0.5 * 9.8 * tiempo
        print("La posición final es:", posicion_final, "metros")
    elif opcion_formula == 2:
        posicion_final = velocidad_inicial * tiempo + 0.5 * 9.8 * tiempo**2
        print("La posición final es:", posicion_final, "metros")
    else:
        print("Opción inválida")

def calcular_tiempo():
    velocidad_inicial = float(input("Ingrese la velocidad inicial (en m/s): "))
    velocidad_final = float(input("Ingrese la velocidad final (en m/s): "))

    tiempo = (velocidad_final - velocidad_inicial) / 9.8
    print("El tiempo transcurrido es:", tiempo, "segundos")

def realizar_conversion():
    opcion_conversion = int(input("Seleccione una opción:\n1. Kilómetro por hora (km/h) a metro por segundo (m/s)\n2. Metro por segundo (m/s) a kilómetro por hora (km/h)\n"))

    if opcion_conversion == 1:
        km_h = float(input("Ingrese la velocidad en kilómetros por hora (km/h): "))
        m_s = km_h * 1000 / 3600
        print("La velocidad en metro por segundo (m/s) es:", m_s)
    elif opcion_conversion == 2:
        m_s = float(input("Ingrese la velocidad en metro por segundo (m/s): "))
        km_h = m_s * 3600 / 1000
        print("La velocidad en kilómetros por hora (km/h) es:", km_h)
    else:
        print("Opción inválida")

while True:
    print("\nSeleccione una opción:")
    print("1. Calcular velocidad final (vf = gt)")
    print("2. Calcular posición final")
    print("3. Calcular tiempo (t = (vf - vo) / g)")
    print("4. Realizar conversiones")
    print("5. Salir")
    
    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        calcular_velocidad_final_gt()
    elif opcion == 2:
        calcular_posicion_final()
    elif opcion == 3:
        calcular_tiempo()
    elif opcion == 4:
        realizar_conversion()
    elif opcion == 5:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida")
