from machine import Pin, I2C
import time

I2C = I2C(0, scl=Pin(22), sda=Pin(21) )

while True:
    devices = I2C.scan()
    print("I2C devices encontrados:", [hex(d) for d in devices] )
    time.sleep(2)