#!/usr/bin/env python
import TM1638
import traceback
import time
import obd

DIO = 17
CLK = 27
STB = 22

display = TM1638.TM1638(DIO, CLK, STB)
display.enable()

connection = obd.OBD() # auto-connects to USB or RF port

def rpm_1000():
	display.set_led(0, 1)

while True:
	cmd = obd.commands.RPM
	response = connection.query(cmd)
	rpm = int(response.value)
	intake_pressure = obd.commands.INTAKE_PRESSURE
	intake_pressure_response = connection.query(intake_pressure)
	boost =  int((int(intake_pressure_response.value) - 100) * .145)
	display.set_text(str(rpm) + "  " + str(boost))
	if rpm < 1000:
		display.set_led(0, 1)
		display.set_led(1, 0)
		display.set_led(2, 0)
		display.set_led(3, 0)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
	if rpm > 1000:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 0)
		display.set_led(3, 0)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
        if rpm > 2000:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 0)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
        if rpm > 3000:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 1)
		display.set_led(4, 0)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
        if rpm > 4000:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 1)
		display.set_led(4, 2)
		display.set_led(5, 0)
		display.set_led(6, 0)
		display.set_led(7, 0)
        if rpm > 5000:
		display.set_led(0, 1)
		display.set_led(1, 1)
		display.set_led(2, 1)
		display.set_led(3, 1)
		display.set_led(4, 2)
		display.set_led(5, 2)
		display.set_led(6, 0)
		display.set_led(7, 0)
        if rpm > 6000:
		display.set_led(0, 2)
		display.set_led(1, 2)
		display.set_led(2, 2)
		display.set_led(3, 2)
		display.set_led(4, 2)
		display.set_led(5, 2)
		display.set_led(6, 2)
		display.set_led(7, 2)
	time.sleep(0.1)


