from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time 

ancho = 128
alto = 64

i2c = I2C(0 , scl = Pin(22), sda = Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)

print(i2c.scan())
print(i2c)

while True:
    oled.text("/--------------/",0,0)
    oled.text("",0,0)
    oled.text("Hola", 50, 10)
    oled.text("Chicos", 40, 20)
    oled.text("de @ las cosas 2", -2, 40)
    oled.text("",0,0)
    oled.text("/--------------/",0,50)
    oled.show()
    print("paso")
    time.sleep(3)
