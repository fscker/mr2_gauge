#!/usr/bin/env python
import string
import TM1638
import traceback
import time
import obd
import random
import decimal
import warnings
warnings.filterwarnings("ignore")

DIO = 17
CLK = 27
STB = 22

keys = 2

class Car:
    rpm = 0.0
    boost = 0
    afr = 0.0

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
        car.boost = int(random.randint(0, 20))
        display_print("PSI   %i" % (car.boost) )
	keys = display.get_buttons()
	if keys:
		main_menu(keys)

def tachometer():
    car.rpm = int(random.randint(2000, 4000))
    display_print("REV %i" % (car.rpm) )
    keys = display.get_buttons()
    if keys:
	main_menu(keys)

def afr():
    car.afr = str(random.random()).replace(".", "")
    car.afr = int(car.afr)
    display_print("AFR  %i" % (car.afr))
    keys = display.get_buttons()
    if keys:
	main_menu(keys)
	
def clear():
   for i in range(0,7):
     display.send_char(i,0)

def main_menu( keys ):
	clear()
	while True:
		#keys = display.get_buttons()
		if keys == 1:
			while True:
				boost_gauge()
				time.sleep(0.5)
		elif keys == 2:
			while True:
				tachometer()
				time.sleep(0.5)
		elif keys == 4:
			while True:
				afr()
				time.sleep(0.5)
    
	time.sleep(2)

main_menu(keys)
