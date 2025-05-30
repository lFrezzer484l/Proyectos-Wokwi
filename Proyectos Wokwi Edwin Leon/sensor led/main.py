from machine import Pin
import utime

pir = Pin(15, Pin.IN, Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)

while True:
    estado = pir.value()
    print(estado)
    utime.sleep_ms(500)

    if estado == 0:
        print("No detecta Objeto")
        led.value(0)
    else:
        print("Objeto a 30 cm")
        while True:
            led.value(1)
            utime.sleep_ms(500)
            led.value(0)
            utime.sleep_ms(500)