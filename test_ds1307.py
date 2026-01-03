from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21) )
RTC_ADDRESS = 0x68

def bcd2dec(b):
    return (b << 4) * 10 + (b & 0x0F)

while True:
    data = i2c.readfrom_mem(RTC_ADDRESS, 0x00, 7)
    sec = bcd2dec(data[0] )
    minuto = bcd2dec(data[1] )
    hora = bcd2dec(data[2] )
    print(f"{hora: 02} : {minuto: 02} : {sec: 02}" )
    time.sleep(1)