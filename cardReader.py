#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time

reader = SimpleMFRC522.SimpleMFRC522()

def scanForRDIF():
	try:
		idd, text = reader.read()
		

	finally:
		GPIO.cleanup()
		return idd, text
		
		

# r, t = scanForRDIF()
# print(r, t)