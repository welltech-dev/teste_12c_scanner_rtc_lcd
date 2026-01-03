from machine import Pin
import time

# TESTE DE LED's RGB

# RGB1
r1 = Pin(4, Pin.OUT)
g1 = Pin(16, Pin.OUT)
b1 = Pin(17, Pin.OUT)

# RGB2

r2 = Pin(5, Pin.OUT)
g2 = Pin(19, Pin.OUT)
b2 = Pin(23, Pin.OUT)

def off():
    for p in (r1, g1, b1, r2, g2, b2):
        p.value(1)

def on(pin):
    pin.value(0)

off()

while True:
    # RGB1
    on(r1); time.sleep(1); off()
    on(g1); time.sleep(1); off()
    on(b1); time.sleep(1); off()
    
    # RGB2
    on(r2); time.sleep(1); off()
    on(g2); time.sleep(1); off()
    on(b2); time.sleep(1); off()