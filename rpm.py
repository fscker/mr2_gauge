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
connection = obd.OBD()

DIO = 17
CLK = 27
STB = 22

keys = 2
revs = 3000
psi = 0

class Car:
    rpm_cmd = obd.commands.RPM
    rpm_response = connection.query(rpm_cmd)
    rpm = rpm_response.value
    boost_cmd =  obd.commands.INTAKE_PRESSURE
    boost_response = connection.query(boost_cmd)
    boost = boost_response.value
    afr_cmd = obd.commands.O2_B1S1
    afr_response = connection.query(afr_cmd)
    afr = afr_response.value
    print afr

display = TM1638.TM1638(DIO, CLK, STB)
display.enable(1)
car = Car()

connection = obd.OBD() # auto-connects to USB or RF port

def display_print(msg): 
    clear()
    msg = msg[0:8]
    for i,v in enumerate(msg):
        if v == ' ':
          display.send_char(i,0)
        else:
          display.send_char(i,display.FONT[v])

def boost_light( psi,revs):
	#if revs are under 2500, chances are we aren't boosting
	if revs < 2500:
		return
	if psi > 2:
		display.set_led(0, 1)
		display.set_led(1, 0)
		display.set_led(2, 0)
		display.set_led(3, 0)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
	if psi > 4:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 0)
		display.set_led(3, 0)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
	if psi > 6:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 0)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
	if psi > 8:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 1)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
	if psi > 10:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 1)
		display.set_led(4, 1)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
	if psi > 12:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 1)
		display.set_led(4, 1)
		display.set_led(5, 2)
		display.set_led(6, 0)
		display.set_led(7, 0)
	if psi > 14:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 1)
		display.set_led(4, 1)
		display.set_led(5, 2)
		display.set_led(6, 2)
		display.set_led(7, 0)
	if psi > 16:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 1)
		display.set_led(4, 1)
		display.set_led(5, 2)
		display.set_led(6, 2)
		display.set_led(7, 2)
	if psi > 17:
		display.set_led(0, 2)
		display.set_led(1, 2)
		display.set_led(2, 2)
		display.set_led(3, 2)
		display.set_led(4, 2)
		display.set_led(5, 2)
		display.set_led(6, 2)
		display.set_led(7, 2)


def boost_gauge():
    	revs_cmd = obd.commands.RPM
    	revs_response = connection.query(revs_cmd)
    	revs = revs_response.value
    	boost_cmd =  obd.commands.INTAKE_PRESSURE
    	boost_response = connection.query(boost_cmd)
    	boost = boost_response.value
        display_print("PSI   %i" % (boost) )
	boost_light( boost,revs )
	keys = display.get_buttons()
	if keys:
		main_menu(keys)

def shift_light( revs ):
	if revs < 1000:
		display.set_led(0, 1)
		display.set_led(1, 0)
		display.set_led(2, 0)
		display.set_led(3, 0)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
	if revs > 1000:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 0)
		display.set_led(3, 0)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
        if revs > 2000:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 0)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
        if revs > 3000:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 1)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
        if revs > 4000:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 1)
		display.set_led(4, 2)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
        if revs > 5000:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 1)
		display.set_led(4, 2)
		display.set_led(5, 2)
		display.set_led(6, 0)
		display.set_led(7, 0)
        if revs > 6000:
		display.set_led(0, 2)
		display.set_led(1, 2)
		display.set_led(2, 2)
		display.set_led(3, 2)
		display.set_led(4, 2)
		display.set_led(5, 2)
		display.set_led(6, 2)
		display.set_led(7, 2)

def tachometer():
    rpm_cmd = obd.commands.RPM
    rpm_response = connection.query(rpm_cmd)
    rpm = rpm_response.value
    display_print("REV %i" % (rpm) )
    revs = rpm
    shift_light( revs )
    keys = display.get_buttons()
    if keys:
	main_menu(keys)

def afr():
    afr_cmd = obd.commands.O2_S1_WR_VOLTAGE
    afr_response = connection.query(afr_cmd)
    afr = afr_response.value
    afr = int(car.afr)
    display_print("AFR  %i" % (afr))
    keys = display.get_buttons()
    if keys:
	main_menu(keys)
	
def clear():
   for i in range(0,7):
     display.send_char(i,0)

def clear_led():
   for i in range(0,7):
     display.set_led(i,0)

def main_menu( keys ):
	clear()
	while True:
		#keys = display.get_buttons()
		if keys == 1:
			clear_led()
			while True:
				boost_gauge()
				time.sleep(0.1)
		elif keys == 2:
			clear_led()
			while True:
				tachometer()
				time.sleep(0.1)
		elif keys == 4:
			clear_led()
			while True:
				afr()
				time.sleep(0.1)
    
	time.sleep(2)

main_menu(keys)
