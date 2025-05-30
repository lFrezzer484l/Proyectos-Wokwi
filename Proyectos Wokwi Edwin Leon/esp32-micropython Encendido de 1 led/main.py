from machine import Pin
from time import sleep
ledR = Pin(17, Pin.OUT)
i = 0

while (i < 4):
    ledR.value(1)  
    sleep(2)       
    ledR.value(0) 
    sleep(2)
    i+=1
    print("Vuelta", i) W