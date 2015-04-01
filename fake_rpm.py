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

display = TM1638.TM1638(DIO, CLK, STB)
display.enable()

#connection = obd.OBD() # auto-connects to USB or RF port


def boost_gauge():
	display.send_char(0, 0b01110011)
	display.send_char(1, 0b01101101)
	display.send_char(2, 0b00000110)
	boost = random.randint(0, 20)
	print boost

def main_menu():
	while True:
	        keys = display.get_buttons()
	        if keys == 1:
	                boost_gauge()
	        if keys == 2:
	                display.set_text(str("12345678"))
	        time.sleep(0.1)

boost_gauge()
