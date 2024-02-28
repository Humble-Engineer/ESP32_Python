from machine import Pin
from time import sleep

class LED:
    def __init__(self,pin):
        self.pin = pin
    
    def blink(self,time):

        self = Pin(self.pin,Pin.OUT)

        self.value(1)
        sleep(time)
        self.value(0)
        sleep(time)
