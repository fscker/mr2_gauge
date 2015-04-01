#!/usr/bin/env python
import TM1638
import traceback
import time
import obd
import random
import warnings
warnings.filterwarnings("ignore")

DIO = 17
CLK = 27
STB = 22

class Car:
    rpm = 0.0
    boost = 0

display = TM1638.TM1638(DIO, CLK, STB)
display.enable(1)
car = Car()

#connection = obd.OBD() # auto-connects to USB or RF port

def display_print(msg): 
    clear()
    msg = msg[0:8]
    for i,v in enumerate(msg):
        if v == ' ':
          display.send_char(i,0)
        else:
          display.send_char(i,display.FONT[v])

def boost_gauge():
    display_print("psi %i" % (car.boost) )

def clear():
   for i in range(0,7):
     display.send_char(i,0)

def main_menu():
    clear()
    while True:
        car.rpm = random.randint(2000, 4000)
        car.boost = random.randint(0, 20)
        keys = display.get_buttons()
        boost_gauge()
    
	time.sleep(2)

main_menu()
