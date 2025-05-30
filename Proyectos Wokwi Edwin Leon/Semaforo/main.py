from machine import Pin
from time import sleep

ledR = Pin(17, Pin.OUT)
ledA = Pin(16, Pin.OUT)
ledV = Pin(4, Pin.OUT)
ciclo = 0

while(ciclo < 4):  # El bucle se ejecutará 4 veces
    if (ciclo == 0):
      print("Inicio el semáforo")

    ledR.value(1)  # Enciende el LED rojo
    sleep(2)       # Espera 2 segundos
    ledR.value(0)  # Apaga el LED rojo
    
    ledA.value(1)  # Enciende el LED amarillo
    sleep(2)       # Espera 2 segundos
    ledA.value(0)  # Apaga el LED amarillo
    
    ledV.value(1)  # Enciende el LED verde
    sleep(2)       # Espera 2 segundos
    ledV.value(0)  # Apaga el LED verde
    
    ciclo += 1  # Incrementa el ciclo
    print("Vuelta", ciclo)