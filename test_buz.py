from machine import Pin, PWM
import time

# TESTE DE BUZZER

buzzer = PWM(Pin(18))
buzzer.duty(0)

while True:
    buzzer.freq(432)    # está é a frequência que mais agrada meus ouvidos
    buzzer.duty(512)    # volume médio
    time.sleep(1)
    buzzer.duty(0)      # desliga o buzzer
    time.sleep(1)
    buzzer.freq(538)    # frequência mais agradável
    buzzer.duty(512)    # volume médio
    time.sleep(1)
    buzzer.duty(0)      # desliga o buzzer
    time.sleep(1)
