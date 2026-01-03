from machine import Pin, ADC
import time

# TECLADO DE INTERÇÃO COM USUÁRIO

adc = ADC(Pin(34) )
adc.atten(ADC.ATTN_11DB)  # Configura o ADC para uma faixa de 0-3.6V

while True:
    value = adc.read()  # Lê o valor do ADC (0-4095)
    print('Valor do ADC:', value)
    time.sleep(0.3)