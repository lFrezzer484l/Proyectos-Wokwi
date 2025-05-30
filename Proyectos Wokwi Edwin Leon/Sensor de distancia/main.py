from machine import Pin
import time
from hcsr04 import HCSR04

# Configuración de los pines del HCSR04
medidor = HCSR04(trigger_pin=5, echo_pin=18)

# Configuración del pin para el LED
led = Pin(2, Pin.OUT)

while True:
    try:
        # Obtener la distancia en centímetros
        distancia = medidor.distance_cm()
        print("La distancia es:", distancia, "cm")

        # Encender o apagar el LED basado en la distancia
        if distancia >= 30:
            led.value(1)  # Enciende el LED si la distancia es mayor o igual a 30
            print("Hay algo por ahí")
        else:
            led.value(0)  # Apaga el LED si la distancia es menor a 30
            print("Nada por ahí")

    except Exception as e:
        print("Error al leer el sensor:", e)

    time.sleep(0.5)  # Pausa de medio segundo antes de la siguiente medición
