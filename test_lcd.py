from machine import Pin, I2C
import time

# DRIVE MÍNIMO PARA UN LCD 16x2 CON I2C

class LCD:
    def _init_(self, i2c, addr):
        self.i2c = i2c
        self.addr = addr
        time.sleep(0.05)
        self.cmd(0x33)  # Inicialização
        self.cmd(0x32)
        self.cmd(0x28)
        self.cmd(0x0C)
        self.cmd(0x06)
        self.cmd(0x01)

    def cmd(self, cmd):
        self.i2c.writeto(self.addr, bytes( [0x08, cmd & 0xF0, (cmd & 0xF0) | 0x04, (cmd & 0xf0) ] ) )
        self.i2c.writeto(self.addr, bytes( [0x08, (cmd << 4)&0xF0, ((cmd<<4)&0xF0) | 0x04, (cmd<<4)&0xF0] ) )

    def write(self, char):
        self.i2c.writeto(self.addr, bytes( [0x09, char & 0xF0, (char & 0xF0) | 0x04, char & 0xF0] ) )
        self.i2c.writeto(self.addr, bytes( [0x09, (char << 4)&0xF0, ((char<<4)&0xF0) | 0x04, (char<<4)&0xF0] ) )

    def texto(self, mensagem):
        for c in mensagem:
            self.write(ord(c) )

i2c = I2C(0, scl=Pin(22), sda=Pin(21) )
lcd = LCD(i2c, 0x27)

lcd.texto("O Mundo tenta, mas DEus é Verdade!")