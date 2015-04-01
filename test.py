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


display.set_text(str("test"))
