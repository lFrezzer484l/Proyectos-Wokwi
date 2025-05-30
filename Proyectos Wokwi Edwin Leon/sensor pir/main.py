from machine import Pin
import utime 

pir = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    estado = pir.value()
    print(estado)
    utime.sleep_ms(500)

    if estado == 0:
        print("alerta esta todo normal")
    else:
        print("alarma hay alguien cerca")