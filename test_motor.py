from machine import Pin
import time

# MOTOR DE PASSO

pins = [
    Pin(14, Pin.OUT),
    Pin(27, Pin.OUT),
    Pin(26, Pin.OUT),
    Pin(25, Pin.OUT),
]

sequencia = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]

def girar_sentido_horario(delay=0.01):
    for passo in sequencia:
        for pin, val in zip(pins, passo):
            pin.value(val)
        time.sleep(delay)

while True:
    for passo in range(100):
            girar_sentido_horario()
    time.sleep(3)