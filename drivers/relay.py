from machine import Pin
from time import sleep

#默认继电器高电平触发
#工作电路电源正极接公共端（COM）
#用电器正极自常开触点处（NO）引出

class RELAY:
    
    def __init__(self,pin):
        
        self.pin = pin
    
    def set(self,state):
        
        self = Pin(self.pin,Pin.OUT)

        if state == "on":
            
            self.value(1)
            
        else :
            
            self.value(0)
            

