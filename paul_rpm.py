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

RC = 0

class Car:
    rpm = 0.0
    boost = 0

display = TM1638.TM1638(DIO, CLK, STB)
display.enable()
car = Car()

#connection = obd.OBD() # auto-connects to USB or RF port

#def display():
#    boost_gauge()

def boost_gauge():
   out = "RPM : " + str(car.rpm)
   display.set_text(str(out))

def boost_gauge():
    out = "psi" + str(car.boost)
#    out = str[0:8]
    display.set_text(str(out))

def main_menu():
    while True:
        car.rpm = random.randint(2000, 4000)
        car.boost = random.randint(0, 20)
        keys = display.get_buttons()
            
        if keys == 1:
		boost_gauge()
        if keys == 2:
		display.set_text(str("12345678"))
  
	time.sleep(0.1)

boost_gauge()
