from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import gc

# Configuración del OLED
ancho = 128
alto = 64
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)

# Prueba de conexión
dispositivos = i2c.scan()
print("Dispositivos I2C encontrados:", dispositivos)
if 60 not in dispositivos:
    raise Exception("El SSD1306 no fue encontrado en la dirección 0x3C")

# Función para cargar iconos
def buscar_icono(ruta):
    gc.collect()  # Libera memoria antes de cargar
    with open(ruta, "rb") as f:
        if f.readline().strip() != b'P4':
            raise ValueError("Formato no soportado, usa PBM binario (P4)")

        # Salta comentarios
        line = f.readline()
        while line.startswith(b'#'):
            line = f.readline()
       
        # Extrae dimensiones
        ancho, alto = map(int, line.strip().split())
        icono = bytearray(f.read())
   
    # Crea el framebuffer para el ícono
    fb = framebuf.FrameBuffer(icono, ancho, alto, framebuf.MONO_HLSB)
    return fb, ancho, alto

# Prueba para mostrar un ícono
try:
    icono, w, h = buscar_icono("icono.txt")  # Asegúrate de usar la extensión correcta
    # Centra el ícono en la pantalla
    x = (ancho - w) // 2
    y = (alto - h) // 2
    oled.framebuf.blit(icono, x, y)
    oled.show()
except Exception as e:
    print("Error cargando el ícono:", e)
