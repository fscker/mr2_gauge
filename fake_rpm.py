#!/usr/bin/env python
import TM1638
import traceback
import time
import obd
import random

DIO = 17
CLK = 27
STB = 22

display = TM1638.TM1638(DIO, CLK, STB)
display.enable()

#connection = obd.OBD() # auto-connects to USB or RF port


def boost_gauge():
	rpm_count = 0
	boost_count = 0
	while True:
		rpm_count += 1
		boost_count += 1
		#cmd = obd.commands.RPM
		#response = random.random()
		rpm = random.randint(900, 7000)
		#intake_pressure = obd.commands.INTAKE_PRESSURE
		#intake_pressure_response = connection.query(intake_pressure)
		boost =  (random.randint(30, 200) - 100) * .145
		boost_int = int(boost)
		#display.set_text(8-len(boost)+i, int(text[i]), i==dotpos)
		print str(rpm) + "  " + str(boost_int).replace("-","")
		#display.set_text(str(rpm) + "  " + str(boost_int).replace("-",""))
		display.set_text(str(rpm_count) + "  " + str(boost_count))
		if rpm_count < 1000:
			display.set_led(0, 1)
			display.set_led(1, 0)
			display.set_led(2, 0)
			display.set_led(3, 0)
			display.set_led(4, 0)
			display.set_led(5, 0)
			display.set_led(6, 0)
			display.set_led(7, 0)
		if rpm_count > 1000:
			display.set_led(0, 1)
			display.set_led(1, 1)
			display.set_led(2, 0)
			display.set_led(3, 0)
			display.set_led(4, 0)
			display.set_led(5, 0)
			display.set_led(6, 0)
			display.set_led(7, 0)
	        if rpm_count > 2000:
			display.set_led(0, 1)
			display.set_led(1, 1)
			display.set_led(2, 1)
			display.set_led(3, 0)
			display.set_led(4, 0)
			display.set_led(5, 0)
			display.set_led(6, 0)
			display.set_led(7, 0)
	        if rpm_count > 3000:
			display.set_led(0, 1)
			display.set_led(1, 1)
			display.set_led(2, 1)
			display.set_led(3, 1)
			display.set_led(4, 0)
			display.set_led(5, 0)
			display.set_led(6, 0)
			display.set_led(7, 0)
	        if rpm_count > 4000:
			display.set_led(0, 1)
			display.set_led(1, 1)
			display.set_led(2, 1)
			display.set_led(3, 1)
			display.set_led(4, 2)
			display.set_led(5, 0)
			display.set_led(6, 0)
			display.set_led(7, 0)
	        if rpm_count > 5000:
			display.set_led(0, 1)
			display.set_led(1, 1)
			display.set_led(2, 1)
			display.set_led(3, 1)
			display.set_led(4, 2)
			display.set_led(5, 2)
			display.set_led(6, 0)
			display.set_led(7, 0)
	        if rpm_count > 6000:
			display.set_led(0, 2)
			display.set_led(1, 2)
			display.set_led(2, 2)
			display.set_led(3, 2)
			display.set_led(4, 2)
			display.set_led(5, 2)
			display.set_led(6, 2)
			display.set_led(7, 2)
		keys = display.get_buttons()
		if keys == 128:
			main_menu()

def main_menu():
	while True:
	        keys = display.get_buttons()
	        print keys
	        if keys == 1:
	                boost_gauge()
	        if keys == 2:
	                display.set_text(str("12345678"))
	        time.sleep(0.1)

main_menu()
